from django.dispatch import receiver
from django.core.urlresolvers import get_callable

from dbconnect.signals import connection_created_to

from signals import namespace_changed
from dbconnect.plugins.namespace.conf import settings


@receiver(connection_created_to)
def switch_namepsace(sender, alias=None, connection=None, wrapper=None, *args, **kwargs):
    if not wrapper.vendor in settings.DBCONNECT_NAMESPACE_SUPPORTED_BACKENDS:
        return

    search_paths = get_callable(settings.DBCONNECT_NAMESPACE_ALIAS_MAPPER)(alias=alias, connection=connection, wrapper=wrapper)
    
    if search_paths is None:
        search_paths = []
    else:
        search_paths = list(search_paths)

    if settings.DBCONNECT_NAMESPACE_FALLBACK_PATH:
        search_paths = search_paths + list(settings.DBCONNECT_NAMESPACE_FALLBACK_PATH)
    if not search_paths:
        return

    cursor = connection.cursor()

    if settings.DBCONNECT_NAMESPACE_PRECHECK:
        cursor.execute('SHOW search_path')
        paths = cursor.fetchall()[0][0].split(',')
        if paths == search_paths:
            return
            
    cursor.execute('SET search_path = %s;' % ','.join(['%s'] * len(search_paths)), search_paths)
    namespace_changed.send(sender=sender, alias=alias, connection=connection, namespace=search_paths, **kwargs)