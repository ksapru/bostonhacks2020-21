from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider


class DB:
    keyspace = 'bostonhacks'
    tables = ['Users', 'Research','Images']

    def __init__(self):
        cloud_config = {
            'secure_connect_bundle': 'secure-connect-bostonhacks20.zip'
        }
        auth_provider = PlainTextAuthProvider('smarangk', 'bostonhacks21')
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = cluster.connect()
