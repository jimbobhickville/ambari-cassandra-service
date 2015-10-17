import os.path
from resource_management.core.resources.system import File, Execute
import yaml

# pylint: disable=unused-argument
class Cassandra(object):

    def configure(self, env):
        import params

        File(os.path.join(params.cassandra_conf_dir, 'cassandra.yaml'),
             content=yaml.safe_dump(params.cassandra_configs),
             mode=0644,
             owner=params.cassandra_user)

    def start(self, env):
        Execute(('service', 'cassandra', 'start'))

    def stop(self, env):
        Execute(('service', 'cassandra', 'stop'))

    def status(self, env):
        Execute(('service', 'cassandra', 'status'))
