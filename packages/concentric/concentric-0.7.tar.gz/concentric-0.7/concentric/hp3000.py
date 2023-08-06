import urllib.parse

from waddle import ParamBunch

from .jdbc import JdbcConnector
from .odbc import OdbcConnector
from pyodbc import connect


# class Hp3000(OdbcConnector):
#     jdbc_class = 'com.minisoft.jdbc.MSJDBCDriver'
#     default_port = 32233
#     default_driver = 'hp3000'
#
#     @classmethod
#     def connect(cls, conf: ParamBunch, *args, **kwargs):
#         cls.ensure('driver', kwargs, conf)
#         driver = kwargs['driver']
#         server = kwargs.get('server') or conf.host
#         port = kwargs.get('port') or conf.port
#         user = kwargs.get('user') or conf.user
#         account = kwargs.get('account') or conf.password
#         pieces = [
#             f'server={server}',
#             f'server port={port}',
#             f'user={user}',
#             f'account={account}',
#             f'driver={driver}',
#         ]
#         schemae = kwargs.get('schema') or conf.schema or []
#         for i, x in enumerate(schemae, 1):
#             pieces.append(f'schema{i}={x}.SCHEMA.{account}')
#         st = ';'.join(pieces)
#         print(st)
#         connection = connect(st)
#         return connection
#
#
#     @classmethod
#     def jdbc_connection_string(cls, conf: ParamBunch, *args, **kwargs):
#         port = f"{conf.get('port', cls.default_port)}"
#         server_type = f"{conf.get('server_type', 0)}"
#         lock_retries = f"{conf.get('lock_retries', 10)}"
#         schema = {
#             f'Schema{i}': f'{x}.SCHEMA.{conf.password}'
#             for i, x in enumerate(conf.get('schema') or [])
#         }
#         params = dict(
#             Server=conf.host,
#             ServerPort=port,
#             ServerType=server_type,
#             LockRetries=lock_retries,
#             User=conf.user,
#             Account=conf.password,
#             Group='PUB',
#             **schema,
#         )
#         params = urllib.parse.urlencode(params)
#         url = f'jdbc:MSJDBC:///?{params}'
#         return url

class Hp3000(JdbcConnector):
    jdbc_class = 'com.minisoft.jdbc.MSJDBCDriver'
    default_port = 32233

    @classmethod
    def connect(cls, conf: ParamBunch, *args, **kwargs):
        jars = kwargs.pop('jars', None) or conf.jars
        return super().connect(conf, jars=jars, **kwargs)

    @classmethod
    def jdbc_connection_string(cls, conf: ParamBunch, *args, **kwargs):
        port = f"{conf.get('port', cls.default_port)}"
        server_type = f"{conf.get('server_type', 0)}"
        lock_retries = f"{conf.get('lock_retries', 10)}"
        schema = {
            f'Schema{i}': f'{x}.SCHEMA.{conf.password}'
            for i, x in enumerate(conf.get('schema') or [])
        }
        params = dict(
            Server=conf.host,
            ServerPort=port,
            ServerType=server_type,
            LockRetries=lock_retries,
            User=conf.user,
            Account=conf.password,
            Group='PUB',
            **schema,
        )
        params = urllib.parse.urlencode(params)
        url = f'jdbc:MSJDBC:///?{params}'
        return url
