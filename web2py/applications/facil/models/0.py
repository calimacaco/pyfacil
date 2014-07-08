from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'FACIL'
settings.subtitle = 'Filtro ACtivo de Impresion Laser'
settings.author = 'Marco Antonio Castro C.'
settings.author_email = 'soportesimplesoft@gmail.com'
settings.keywords = 'facil'
settings.description = 'Filtro activo de impresion'
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://facil.sqlite'
settings.security_key = '8b8ac17c-fa10-4953-b694-37cbb3f037c5'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = ['']
