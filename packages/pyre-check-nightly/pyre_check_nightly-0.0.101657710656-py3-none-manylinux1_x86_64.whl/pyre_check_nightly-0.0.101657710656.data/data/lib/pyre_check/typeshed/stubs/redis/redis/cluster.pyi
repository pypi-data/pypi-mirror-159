from typing import Any, ClassVar, Generic

from redis.client import PubSub
from redis.commands import RedisClusterCommands
from redis.commands.core import _StrType
from redis.connection import DefaultParser
from redis.exceptions import RedisError

def get_node_name(host, port): ...
def get_connection(redis_node, *args, **options): ...
def parse_scan_result(command, res, **options): ...
def parse_pubsub_numsub(command, res, **options): ...
def parse_cluster_slots(resp, **options): ...

PRIMARY: str
REPLICA: str
SLOT_ID: str
REDIS_ALLOWED_KEYS: Any
KWARGS_DISABLED_KEYS: Any
READ_COMMANDS: Any

def cleanup_kwargs(**kwargs): ...

class ClusterParser(DefaultParser):
    EXCEPTION_CLASSES: Any

class RedisCluster(RedisClusterCommands[_StrType], Generic[_StrType]):
    RedisClusterRequestTTL: ClassVar[int]
    PRIMARIES: ClassVar[str]
    REPLICAS: ClassVar[str]
    ALL_NODES: ClassVar[str]
    RANDOM: ClassVar[str]
    DEFAULT_NODE: ClassVar[str]
    NODE_FLAGS: ClassVar[set[str]]
    COMMAND_FLAGS: ClassVar[Any]
    CLUSTER_COMMANDS_RESPONSE_CALLBACKS: ClassVar[dict[str, Any]]
    RESULT_CALLBACKS: ClassVar[Any]
    ERRORS_ALLOW_RETRY: ClassVar[tuple[type[RedisError], ...]]
    user_on_connect_func: Any
    encoder: Any
    cluster_error_retry_attempts: Any
    command_flags: Any
    node_flags: Any
    read_from_replicas: Any
    reinitialize_counter: int
    reinitialize_steps: Any
    nodes_manager: Any
    cluster_response_callbacks: Any
    result_callbacks: Any
    commands_parser: Any
    def __init__(
        self,
        host: Any | None = ...,
        port: int = ...,
        startup_nodes: Any | None = ...,
        cluster_error_retry_attempts: int = ...,
        require_full_coverage: bool = ...,
        reinitialize_steps: int = ...,
        read_from_replicas: bool = ...,
        url: Any | None = ...,
        **kwargs,
    ) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def __del__(self) -> None: ...
    def disconnect_connection_pools(self) -> None: ...
    @classmethod
    def from_url(cls, url, **kwargs): ...
    def on_connect(self, connection) -> None: ...
    def get_redis_connection(self, node): ...
    def get_node(self, host: Any | None = ..., port: Any | None = ..., node_name: Any | None = ...): ...
    def get_primaries(self): ...
    def get_replicas(self): ...
    def get_random_node(self): ...
    def get_nodes(self): ...
    def get_node_from_key(self, key, replica: bool = ...): ...
    def get_default_node(self): ...
    def set_default_node(self, node): ...
    def monitor(self, target_node: Any | None = ...): ...
    def pubsub(self, node: Any | None = ..., host: Any | None = ..., port: Any | None = ..., **kwargs): ...
    def pipeline(self, transaction: Any | None = ..., shard_hint: Any | None = ...): ...
    def keyslot(self, key): ...
    def determine_slot(self, *args): ...
    def reinitialize_caches(self) -> None: ...
    def get_encoder(self): ...
    def get_connection_kwargs(self): ...
    def execute_command(self, *args, **kwargs): ...
    def close(self) -> None: ...

class ClusterNode:
    host: Any
    port: Any
    name: Any
    server_type: Any
    redis_connection: Any
    def __init__(self, host, port, server_type: Any | None = ..., redis_connection: Any | None = ...) -> None: ...
    def __eq__(self, obj): ...
    def __del__(self) -> None: ...

class LoadBalancer:
    primary_to_idx: Any
    start_index: Any
    def __init__(self, start_index: int = ...) -> None: ...
    def get_server_index(self, primary, list_size): ...
    def reset(self) -> None: ...

class NodesManager:
    nodes_cache: Any
    slots_cache: Any
    startup_nodes: Any
    default_node: Any
    from_url: Any
    connection_kwargs: Any
    read_load_balancer: Any
    def __init__(
        self, startup_nodes, from_url: bool = ..., require_full_coverage: bool = ..., lock: Any | None = ..., **kwargs
    ) -> None: ...
    def get_node(self, host: Any | None = ..., port: Any | None = ..., node_name: Any | None = ...): ...
    def update_moved_exception(self, exception) -> None: ...
    def get_node_from_slot(self, slot, read_from_replicas: bool = ..., server_type: Any | None = ...): ...
    def get_nodes_by_server_type(self, server_type): ...
    def populate_startup_nodes(self, nodes) -> None: ...
    def check_slots_coverage(self, slots_cache): ...
    def create_redis_connections(self, nodes) -> None: ...
    def create_redis_node(self, host, port, **kwargs): ...
    def initialize(self) -> None: ...
    def close(self) -> None: ...
    def reset(self) -> None: ...

class ClusterPubSub(PubSub):
    node: Any
    cluster: Any
    def __init__(
        self, redis_cluster, node: Any | None = ..., host: Any | None = ..., port: Any | None = ..., **kwargs
    ) -> None: ...
    def set_pubsub_node(self, cluster, node: Any | None = ..., host: Any | None = ..., port: Any | None = ...) -> None: ...
    def get_pubsub_node(self): ...
    def execute_command(self, *args, **kwargs) -> None: ...
    def get_redis_connection(self): ...

class ClusterPipeline(RedisCluster[_StrType], Generic[_StrType]):
    command_stack: Any
    nodes_manager: Any
    refresh_table_asap: bool
    result_callbacks: Any
    startup_nodes: Any
    read_from_replicas: Any
    command_flags: Any
    cluster_response_callbacks: Any
    cluster_error_retry_attempts: Any
    reinitialize_counter: int
    reinitialize_steps: Any
    encoder: Any
    commands_parser: Any
    def __init__(
        self,
        nodes_manager,
        result_callbacks: Any | None = ...,
        cluster_response_callbacks: Any | None = ...,
        startup_nodes: Any | None = ...,
        read_from_replicas: bool = ...,
        cluster_error_retry_attempts: int = ...,
        reinitialize_steps: int = ...,
        **kwargs,
    ) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def __del__(self) -> None: ...
    def __len__(self): ...
    def __nonzero__(self): ...
    def __bool__(self): ...
    def execute_command(self, *args, **kwargs): ...
    def pipeline_execute_command(self, *args, **options): ...
    def raise_first_error(self, stack) -> None: ...
    def annotate_exception(self, exception, number, command) -> None: ...
    def execute(self, raise_on_error: bool = ...): ...
    scripts: Any
    watching: bool
    explicit_transaction: bool
    def reset(self) -> None: ...
    def send_cluster_commands(self, stack, raise_on_error: bool = ..., allow_redirections: bool = ...): ...
    def eval(self) -> None: ...
    def multi(self) -> None: ...
    def immediate_execute_command(self, *args, **options) -> None: ...
    def load_scripts(self) -> None: ...
    def watch(self, *names) -> None: ...
    def unwatch(self) -> None: ...
    def script_load_for_pipeline(self, *args, **kwargs) -> None: ...
    def delete(self, *names): ...

def block_pipeline_command(func): ...

class PipelineCommand:
    args: Any
    options: Any
    position: Any
    result: Any
    node: Any
    asking: bool
    def __init__(self, args, options: Any | None = ..., position: Any | None = ...) -> None: ...

class NodeCommands:
    parse_response: Any
    connection_pool: Any
    connection: Any
    commands: Any
    def __init__(self, parse_response, connection_pool, connection) -> None: ...
    def append(self, c) -> None: ...
    def write(self) -> None: ...
    def read(self) -> None: ...
