from django.dispatch import receiver
from django.db.backends.signals import connection_created

from signals import connection_created_to
from utils import reverse


@receiver(connection_created)
def send_connection_created(sender, connection, signal=None, **kwargs):
    alias = reverse(connection)
    connection_created_to.send(sender=alias, wrapper=sender, connection=connection, alias=alias, **kwargs)