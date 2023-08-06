from ravendb.documents.operations.definitions import MaintenanceOperation
from ravendb.http.raven_command import RavenCommand
from ravendb.exceptions import exceptions


class PullReplicationDefinition:
    def __init__(self, name, certificates, mentor_node=None, delayed_replication_for=None):
        self.DelayedReplicationFor = delayed_replication_for
        self.Name = name
        self.MentorNode = mentor_node
        self.Certificates = certificates


class ExternalReplication:
    def __init__(
        self,
        name,
        connection_string_name,
        mentor_node=None,
        delayed_replication_for=None,
    ):
        self.DelayedReplicationFor = delayed_replication_for
        self.Name = name
        self.ConnectionStringName = connection_string_name
        self.MentorNode = mentor_node


class PullReplicationAsSink:
    def __init__(
        self,
        hub,
        connection_string_name,
        certificate_base64,
        certificate_password,
        mentor_node=None,
        delayed_replication_for=None,
    ):
        self.DelayedReplicationFor = delayed_replication_for
        self.HubDefinitionName = hub
        self.ConnectionStringName = connection_string_name
        self.MentorNode = mentor_node


class ConnectionString:
    @staticmethod
    def raven(name, database, urls):
        return {
            "Type": "Raven",
            "Name": name,
            "Database": database,
            "TopologyDiscoveryUrls": urls,
        }

    @staticmethod
    def sql(name, factory, connection_string):
        return {
            "Type": "Raven",
            "FactoryName": factory,
            "ConnectionString": connection_string,
        }


class UpdatePullReplicationAsSinkOperation(MaintenanceOperation):
    def __init__(self, definition):

        if definition is None:
            raise ValueError("definition cannot be None")

        super(UpdatePullReplicationAsSinkOperation, self).__init__()
        self._definition = definition

    def get_command(self, conventions):
        return self._UpdatePullReplicationAsSinkCommand(self._definition)

    class _UpdatePullReplicationAsSinkCommand(RavenCommand):
        def __init__(self, definition):
            if definition is None:
                raise ValueError("definition cannot be None")

            super(
                UpdatePullReplicationAsSinkOperation._UpdatePullReplicationAsSinkCommand,
                self,
            ).__init__(method="POST", is_raft_request=True)
            self._definition = definition

        def create_request(self, server_node):
            self.url = "{0}/databases/{1}/admin/tasks/sink-pull-replication".format(
                server_node.url, server_node.database
            )
            self.data = {"PullReplicationAsSink": self._definition}

        def set_response(self, response):
            try:
                response = response.json()
                if "Error" in response:
                    raise exceptions.InvalidOperationException(response["Message"], response["Type"], response["Error"])
            except ValueError:
                raise response.raise_for_status()
            return {"raft_command_index": response["RaftCommandIndex"]}


class PutPullReplicationAsHubOperation(MaintenanceOperation):
    def __init__(self, definition):

        if definition is None:
            raise ValueError("definition cannot be None")

        super(PutPullReplicationAsHubOperation, self).__init__()
        self._definition = definition

    def get_command(self, conventions):
        return self._PutPullReplicationAsHubCommand(self._definition)

    class _PutPullReplicationAsHubCommand(RavenCommand):
        def __init__(self, definition):
            if definition is None:
                raise ValueError("definition cannot be None")

            super(PutPullReplicationAsHubOperation._PutPullReplicationAsHubCommand, self).__init__(
                method="PUT", is_raft_request=True
            )
            self._definition = definition

        def create_request(self, server_node):
            self.url = "{0}/databases/{1}/admin/tasks/pull-replication/hub".format(
                server_node.url, server_node.database
            )
            self.data = self._definition

        def set_response(self, response):
            try:
                response = response.json()
                if "Error" in response:
                    raise exceptions.InvalidOperationException(response["Message"], response["Type"], response["Error"])
            except ValueError:
                raise response.raise_for_status()
            return {"raft_command_index": response["RaftCommandIndex"]}


class UpdateExternalReplicationOperation(MaintenanceOperation):
    def __init__(self, watcher):

        if watcher is None:
            raise ValueError("watcher cannot be None")

        super(UpdateExternalReplicationOperation, self).__init__()
        self._watcher = watcher

    def get_command(self, conventions):
        return self._UpdateExternalReplicationCommand(self._watcher)

    class _UpdateExternalReplicationCommand(RavenCommand):
        def __init__(self, watcher):
            if watcher is None:
                raise ValueError("watcher cannot be None")

            super(
                UpdateExternalReplicationOperation._UpdateExternalReplicationCommand,
                self,
            ).__init__(method="POST", is_raft_request=True)
            self._watcher = watcher

        def create_request(self, server_node):
            self.url = "{0}/databases/{1}/admin/tasks/external-replication".format(
                server_node.url, server_node.database
            )
            self.data = {"Watcher": self._watcher}

        def set_response(self, response):
            try:
                response = response.json()
                if "Error" in response:
                    raise exceptions.InvalidOperationException(response["Message"], response["Type"], response["Error"])
            except ValueError:
                raise response.raise_for_status()
            return {"raft_command_index": response["RaftCommandIndex"]}


class PutConnectionStringOperation(MaintenanceOperation):
    def __init__(self, connection_string_def):

        if connection_string_def is None:
            raise ValueError("connection_string_def cannot be None")

        super(PutConnectionStringOperation, self).__init__()
        self._connection_string_def = connection_string_def

    def get_command(self, conventions):
        return self._PutConnectionStringCommand(self._connection_string_def)

    class _PutConnectionStringCommand(RavenCommand):
        def __init__(self, connection_string_def):
            if connection_string_def is None:
                raise ValueError("connection_string_def cannot be None")

            super(PutConnectionStringOperation._PutConnectionStringCommand, self).__init__(
                method="PUT", is_raft_request=True
            )
            self._connection_string_def = connection_string_def

        def create_request(self, server_node):
            self.url = "{0}/databases/{1}/admin/connection-strings".format(server_node.url, server_node.database)
            self.data = self._connection_string_def

        def set_response(self, response):
            try:
                response = response.json()
                if "Error" in response:
                    raise exceptions.InvalidOperationException(response["Message"], response["Type"], response["Error"])
            except ValueError:
                raise response.raise_for_status()
            return {"raft_command_index": response["RaftCommandIndex"]}
