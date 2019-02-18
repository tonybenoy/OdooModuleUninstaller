import xmlrpclib
url = "http://localhost:8069"

db = "databasename"
username = "admin"
password = "admin"

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
uid = common.authenticate(db, username, password, {})
modulename = "purchase_association"
res_ids = models.execute(db, uid, password,'ir.module.module', 'search', [('name', '=', modulename)])
models.execute_kw(db, uid, password, 'ir.module.module',"button_immediate_uninstall", res_ids)

