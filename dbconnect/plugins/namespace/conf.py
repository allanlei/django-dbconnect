from django.conf import settings
from appconf import AppConf

class DbConnectAppConf(AppConf):
    SUPPORTED_BACKENDS = ('postgresql', )
    PRECHECK = False
    ALIAS_MAPPER = 'dbconnect.plugins.namespace.resolvers.default'
    FALLBACK_PATH = None

    class Meta:
        prefix = 'dbconnect_namespace'