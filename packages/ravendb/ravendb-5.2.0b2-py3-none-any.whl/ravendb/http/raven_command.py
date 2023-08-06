from __future__ import annotations

import datetime
import http
from http import HTTPStatus
from abc import abstractmethod
from typing import Union, Optional, Callable, Generic, TypeVar, Dict, Type
from enum import Enum

import requests
from ravendb.extensions.http_extensions import HttpExtensions
from ravendb.http.http_cache import HttpCache
from ravendb.http.misc import ResponseDisposeHandling
from ravendb.http.server_node import ServerNode


class RavenCommandResponseType(Enum):
    EMPTY = "Empty"
    OBJECT = "Object"
    RAW = "Raw"

    def __str__(self):
        return self.value


ResultClass = TypeVar("ResultClass")

# todo: check what's wrong with this generic. it doesnt work e.g. in HiloCommand


class RavenCommand(Generic[ResultClass]):
    # void_command is rarely used arg that determine if the user didn't pass result_class due to copying RavenCommand
    # or if user wants to create VoidRavenCommand that inherits from this class and its' result type is None
    def __init__(self, result_class: type = None, copy: RavenCommand = None, void_command: Optional[bool] = False):
        if not ((result_class is not None or void_command) ^ (copy is not None)):
            raise ValueError("Pass either result_class or RavenCommand copy.")
        is_not_copy = result_class or void_command
        self._result_class: Type[ResultClass] = result_class if is_not_copy else copy._result_class
        self.result: Union[None, ResultClass] = None
        self.status_code: Union[None, int] = None

        self._response_type: RavenCommandResponseType = (
            RavenCommandResponseType.OBJECT if is_not_copy else copy.response_type
        )

        self.timeout: Union[None, datetime.timedelta] = None
        self._can_cache: bool = True if is_not_copy else copy.can_cache
        self._can_cache_aggressively: bool = True if is_not_copy else copy.can_cache_aggressively
        self._selected_node_tag: Union[None, str] = None if is_not_copy else copy.selected_node_tag
        self._number_of_attempts: Union[None, int] = None

        self.failover_topology_etag = -2

        self.on_response_failure: Callable[[requests.Response], None] = lambda resp: None

        self.failed_nodes: Dict[ServerNode, Exception] = {}

    @abstractmethod
    def is_read_request(self) -> bool:
        pass

    @abstractmethod
    def create_request(self, node: ServerNode) -> requests.Request:
        pass

    @property
    def response_type(self) -> RavenCommandResponseType:
        return self._response_type

    @property
    def can_cache(self):
        return self._can_cache

    @property
    def can_cache_aggressively(self):
        return self._can_cache_aggressively

    @property
    def selected_node_tag(self):
        return self._selected_node_tag

    @property
    def number_of_attempts(self) -> int:
        if self._number_of_attempts is None:
            self._number_of_attempts = 0
        return self._number_of_attempts

    @number_of_attempts.setter
    def number_of_attempts(self, value: int):
        self._number_of_attempts = value

    @abstractmethod
    def set_response(self, response: str, from_cache: bool) -> None:
        if self._response_type == RavenCommandResponseType.EMPTY or RavenCommandResponseType.RAW:
            self._throw_invalid_response()
        raise RuntimeError(
            f"{self.response_type.name} command must override the set_response method which "
            f"expects response with the following type {self.response_type}"
        )

    def send(self, session: requests.Session, request: requests.Request) -> requests.Response:
        return session.request(
            request.method,
            url=request.url,
            data=request.data,
            files=request.files,
            cert=session.cert,
            headers=request.headers,
        )

    def set_response_raw(self, response: requests.Response, stream: bytes) -> None:
        raise RuntimeError(
            f"When {self.response_type} is set to Raw then please override this method to handle the response "
        )

    def _url_encode(self, value: str) -> bytes:
        return value.encode("utf-8")

    @staticmethod
    def ensure_is_not_null_or_string(value: str, name: str) -> None:
        if not value:
            raise ValueError(f"{name} cannot be None or empty")

    def is_failed_with_node(self, node: ServerNode) -> bool:
        return self.failed_nodes and node in self.failed_nodes

    def process_response(self, cache: HttpCache, response: requests.Response, url) -> ResponseDisposeHandling:
        # todo: check if response is a dict here from beginning
        if not response:
            return ResponseDisposeHandling.AUTOMATIC

        if self.response_type == RavenCommandResponseType.EMPTY or response.status_code == HTTPStatus.NO_CONTENT:
            return ResponseDisposeHandling.AUTOMATIC

        try:
            if self.response_type == RavenCommandResponseType.OBJECT:
                content_length = len(response.content)
                if content_length == 0:
                    response.close()
                    return ResponseDisposeHandling.AUTOMATIC

                json_content = response.content.decode("utf-8")
                if cache is not None:
                    self._cache_response(cache, url, response, json_content)
                self.set_response(json_content, False)
                return ResponseDisposeHandling.AUTOMATIC
            else:
                self.set_response_raw(response, response.content)
        except Exception as e:
            raise e
        finally:
            response.close()
        return ResponseDisposeHandling.AUTOMATIC

    def _cache_response(self, cache: HttpCache, url: str, response: requests.Response, response_json: str) -> None:
        if not self.can_cache:
            return

        change_vector = HttpExtensions.get_etag_header(response)
        if change_vector is None:
            return
        cache.set(url, change_vector, response_json)

    @staticmethod
    def _throw_invalid_response(cause: Optional[BaseException] = None) -> None:
        raise ValueError(f"Response is invalid{f': {cause.args[0]}' if cause else ''}")

    def _add_change_vector_if_not_none(self, change_vector: str, request: requests.Request):
        if change_vector:
            if request.headers is not None:
                request.headers["If-Match"] = f'"{change_vector}"'
            else:
                request.headers = {"If-Match": f'"{change_vector}'}


class VoidRavenCommand(RavenCommand[None]):
    def __init__(self):
        super().__init__(void_command=True)
        self._response_type = RavenCommandResponseType.EMPTY

    @abstractmethod
    def create_request(self, node: ServerNode) -> requests.Request:
        pass

    def is_read_request(self) -> bool:
        return False

    def set_response(self, response: str, from_cache: bool) -> None:
        pass
