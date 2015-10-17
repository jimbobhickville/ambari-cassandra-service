from resource_management.libraries.script.script import Script

from cassandra import Cassandra


class Server(Script):

    def install(self, env):
        self.install_packages(env)

    def stop(self, env, rolling_restart=False):
        Cassandra().stop(env)

    def start(self, env, rolling_restart=False):
        self.configure(env)
        Cassandra().start(env)

    def status(self, env):
        Cassandra().status(env)

    def configure(self, env):
        import params
        env.set_params(params)

        Cassandra().configure(env)


if __name__ == '__main__':
    Server().execute()
