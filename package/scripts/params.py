from resource_management.libraries.script.script import Script

CONFIG = Script.get_config()
CONFIGS = CONFIG['configurations']
HOST_INFO = CONFIG['clusterHostInfo']
CASSANDRA_CONF = CONFIGS['cassandra-conf']

cassandra_conf_dir = '/etc/cassandra/conf'
cassandra_user = 'cassandra'

config_defaults = {
    'cross_node_timeout': False,
    'inter_dc_tcp_nodelay': False,
    'rpc_server_type':  'sync',
    'disk_failure_policy': 'stop',
    'authorizer': 'AllowAllAuthorizer',
    'tombstone_warn_threshold': 1000,
    'internode_compression': 'all',
    'truncate_request_timeout_in_ms': 60000,
    'cluster_name': 'Test Cluster',
    'read_request_timeout_in_ms': 5000,
    'ssl_storage_port': 7001,
    'listen_address': 'localhost',
    'request_scheduler': 'org.apache.cassandra.scheduler.NoScheduler',
    'range_request_timeout_in_ms': 10000,
    'hinted_handoff_enabled': True,
    'max_hint_window_in_ms': 10800000,
    'authenticator': 'AllowAllAuthenticator',
    'tombstone_failure_threshold': 100000,
    'commitlog_directory': '/var/lib/cassandra/commitlog',
    'column_index_size_in_kb': 64,
    'trickle_fsync_interval_in_kb': 10240,
    'start_native_transport': True,
    'snapshot_before_compaction': False,
    'concurrent_reads': 32,
    'counter_write_request_timeout_in_ms': 5000,
    'endpoint_snitch': 'SimpleSnitch',
    'data_file_directories': [
        '/var/lib/cassandra/data'
    ],
    'start_rpc': True,
    'dynamic_snitch_update_interval_in_ms': 100,
    'commitlog_segment_size_in_mb': 32,
    'trickle_fsync': False,
    'rpc_address': 'localhost',
    'concurrent_counter_writes': 32,
    'counter_cache_save_period': 7200,
    'commitlog_sync_period_in_ms': 10000,
    'thrift_framed_transport_size_in_mb': 15,
    'counter_cache_size_in_mb': None,
    'commit_failure_policy': 'stop',
    'compaction_large_partition_warning_threshold_mb': 100,
    'index_summary_resize_interval_in_minutes': 60,
    'compaction_throughput_mb_per_sec': 16,
    'key_cache_size_in_mb': None,
    'row_cache_size_in_mb': 0,
    'dynamic_snitch_badness_threshold': 0.10000000000000001,
    'rpc_keepalive': True,
    'num_tokens': 256,
    'row_cache_save_period': 0,
    'permissions_validity_in_ms': 2000,
    'dynamic_snitch_reset_interval_in_ms': 600000,
    'seed_provider': [{
        'class_name': 'org.apache.cassandra.locator.SimpleSeedProvider',
        'parameters': [{'seeds': '127.0.0.1'}]
    }],
    'batchlog_replay_throttle_in_kb': 1024,
    'storage_port': 7000,
    'rpc_port': 9160,
    'incremental_backups': False,
    'saved_caches_directory': '/var/lib/cassandra/saved_caches',
    'max_hints_delivery_threads': 2,
    'commitlog_sync': 'periodic',
    'key_cache_save_period': 14400,
    'server_encryption_options': {
        'keystore': 'conf/.keystore',
        'keystore_password': 'cassandra',
        'truststore': 'conf/.truststore',
        'truststore_password': 'cassandra',
        'internode_encryption': 'none'
    },
    'sstable_preemptive_open_interval_in_mb': 50,
    'write_request_timeout_in_ms': 2000,
    'index_summary_capacity_in_mb': None,
    'cas_contention_timeout_in_ms': 1000,
    'request_timeout_in_ms': 10000,
    'concurrent_writes': 32,
    'auto_snapshot': True,
    'native_transport_port': 9042,
    'client_encryption_options': {
        'keystore': 'conf/.keystore',
        'keystore_password': 'cassandra',
        'enabled': False
    },
    'partitioner': 'org.apache.cassandra.dht.Murmur3Partitioner',
    'hinted_handoff_throttle_in_kb': 1024,
    'batch_size_warn_threshold_in_kb': 5,
    'memtable_allocation_type': 'heap_buffers'
}


def build_config(defaults, path=None):
    configs = {}
    if path is None:
        path = []

    for default_key, default_value in defaults.iteritems():
        config_key = default_key
        if path:
            config_key = '.'.join(path + [default_key])
        if isinstance(default_value, list):
            value = CASSANDRA_CONF.get(config_key, "")
            if value:
                configs[default_key] = value.split(',')
            else:
                configs[default_key] = default_value
        elif isinstance(default_value, dict):
            configs[default_key] = build_config(defaults[default_key], path=path + [default_key])
        else:
            configs[default_key] = CASSANDRA_CONF.get(config_key, default_value)
    return configs

cassandra_configs = build_config(config_defaults)