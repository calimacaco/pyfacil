# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL('sqlite://facil.sqlite')
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore')
    ## store sessions and tickets there
    session.connect(request, response, db = db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db, hmac_key=Auth.get_or_create_key())
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables

########################################
db.define_table('auth_user',
    Field('username', type='string',
          label=T('Username')),
    Field('first_name', type='string',
          label=T('First Name')),
    Field('last_name', type='string',
          label=T('Last Name')),
    Field('email', type='string',
          label=T('Email')),
    Field('password', type='password',
          readable=False,
          label=T('Password')),
    Field('created_on','datetime',default=request.now,
          label=T('Created On'),writable=False,readable=False),
    Field('modified_on','datetime',default=request.now,
          label=T('Modified On'),writable=False,readable=False,
          update=request.now),
    Field('registration_key',default='',
          writable=False,readable=False),
    Field('reset_password_key',default='',
          writable=False,readable=False),
    Field('registration_id',default='',
          writable=False,readable=False),
    format='%(username)s',
    migrate=settings.migrate)


db.auth_user.first_name.requires = IS_NOT_EMPTY(error_message=auth.messages.is_empty)
db.auth_user.last_name.requires = IS_NOT_EMPTY(error_message=auth.messages.is_empty)
db.auth_user.password.requires = CRYPT(key=auth.settings.hmac_key)
db.auth_user.username.requires = IS_NOT_IN_DB(db, db.auth_user.username)
db.auth_user.email.requires = (IS_EMAIL(error_message=auth.messages.invalid_email),
                               IS_NOT_IN_DB(db, db.auth_user.email))
auth.define_tables(migrate = settings.migrate)

## configure email
mail=auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth,filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################


mail.settings.server = settings.email_server
mail.settings.sender = settings.email_sender
mail.settings.login = settings.email_login


#base de datos
db.define_table("tbl_estado",
    Field("idgrupo", "integer", notnull=True, default=None),
    Field("valor", "integer", notnull=True, default=None),
    Field("descripcion", "string", notnull=True, default=None),
    Field("orden", "integer", notnull=True, default=0))

db.define_table("tbl_pdl",
    Field("descripcion", "text", notnull=True, default=None))

db.define_table("tbl_impresora",
    Field("nombre", "string", notnull=True, default=None),
    Field("salidapdl", db.tbl_pdl),
    Field("idestado", db.tbl_estado))

db.define_table("tbl_spool",
    Field("idestado", db.tbl_estado),
    Field("idimpresora", db.tbl_impresora),
    Field("cups_usuario", "string", notnull=True, default=None),
    Field("cups_nombrejob", "string", notnull=True, default=None),
    Field("cups_jobid", "integer", default=None),
    Field("cups_copias", "integer", notnull=True, default=None),
    Field("fecha", "date", notnull=True, default=None))

db.define_table("tbl_correo",
    Field("estado", db.tbl_estado),
    Field("htmlcontenido", "text", default=None),
    Field("txtcontenido", "text", default=None),
    Field("puerto", "integer", default=None),
    Field("usuario", "text", default=None),
    Field("clave", "text", default=None),
    Field("servidor", "text", default=None),
    Field("tls", "text", length=1, default=None),
    Field("bandera", "text", default=None),
    Field("enviado", "text", default=None),
    Field("rutafinal", "text", default=None),
    Field("rutaanexo", "text", default=None),
    Field("archivoanexo", "text", default=None),
    Field("confirmar", "text", default=None))

db.define_table("tbl_adjuntos",
    Field("nombre", "text", notnull=True, default=None),
    Field("dirpdf", "text", notnull=True, default=None),
    Field("estado", db.tbl_estado),
    Field("dirpcl", "text", notnull=True, default=None))

db.define_table("tbl_cliente",
    Field("busqueda", "text", notnull=True, default=None),
    Field("dircorreo", "text", notnull=True, default=None),
    Field("imprimir", "integer", notnull=True, default=None),
    Field("pdf", "integer", notnull=True, default=None),
    Field("correo", "integer", notnull=True, default=None),
    Field("estado", db.tbl_estado))

db.define_table("tbl_logenvio",
    Field("estado", db.tbl_estado),
    Field("idjob", db.tbl_spool),
    Field("fecha", "date", notnull=True, default=None),
    Field("enviar", "text", notnull=True, default=None),
    Field("copia", "text", notnull=True, default=None),
    Field("bscopia", "text", notnull=True, default=None),
    Field("asunto", "text", notnull=True, default=None),
    Field("adjunto", "text", notnull=True, default=None),
    Field("bandera", "text", notnull=True, default=None),
    Field("rutafinal", "text", notnull=True, default=None))

db.define_table("tbl_archivo",
    Field("archivo", "text", notnull=True, default=None),
    Field("funcion", db.tbl_estado),
    Field("descripcion", "text", notnull=True, default=None),
    Field("idjob", db.tbl_spool),
    Field("fecha", "date", notnull=True, default=None))

""" Relations between tables (remove fields you don't need from requires) """
db.tbl_impresora.salidapdl.requires=IS_IN_DB( db, 'tbl_pdl.id', ' %(descripcion)s')
db.tbl_impresora.idestado.requires=IS_IN_DB( db, 'tbl_estado.id', ' %(idgrupo)s %(valor)s %(descripcion)s %(orden)s')
db.tbl_spool.idestado.requires=IS_IN_DB( db, 'tbl_estado.id', ' %(idgrupo)s %(valor)s %(descripcion)s %(orden)s')
db.tbl_spool.idimpresora.requires=IS_IN_DB( db, 'tbl_impresora.id', ' %(nombre)s %(salidapdl)s %(idestado)s')
db.tbl_correo.estado.requires=IS_IN_DB( db, 'tbl_estado.id', ' %(idgrupo)s %(valor)s %(descripcion)s %(orden)s')
db.tbl_adjuntos.estado.requires=IS_IN_DB( db, 'tbl_estado.id', ' %(idgrupo)s %(valor)s %(descripcion)s %(orden)s')
db.tbl_cliente.estado.requires=IS_IN_DB( db, 'tbl_estado.id', ' %(idgrupo)s %(valor)s %(descripcion)s %(orden)s')
db.tbl_logenvio.estado.requires=IS_IN_DB( db, 'tbl_estado.id', ' %(idgrupo)s %(valor)s %(descripcion)s %(orden)s')
db.tbl_logenvio.idjob.requires=IS_IN_DB( db, 'tbl_spool.id', ' %(idestado)s %(idimpresora)s %(cups_usuario)s %(cups_nombrejob)s %(cups_jobid)s %(cups_copias)s %(fecha)s')
db.tbl_archivo.funcion.requires=IS_IN_DB( db, 'tbl_estado.id', ' %(idgrupo)s %(valor)s %(descripcion)s %(orden)s')
db.tbl_archivo.idjob.requires=IS_IN_DB( db, 'tbl_spool.id', ' %(idestado)s %(idimpresora)s %(cups_usuario)s %(cups_nombrejob)s %(cups_jobid)s %(cups_copias)s %(fecha)s')
