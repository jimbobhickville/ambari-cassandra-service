from resource_management.libraries.script.script import Script

CONFIG = Script.get_config()
CONFIGS = CONFIG['configurations']
HOST_INFO = CONFIG['clusterHostInfo']
CASSANDRA_CONF = CONFIGS['cassandra-conf']

cassandra_conf_dir = '/etc/cassandra/conf'
cassandra_user = 'cassandra'
