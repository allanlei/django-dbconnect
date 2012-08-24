import django.dispatch


connection_created_to = django.dispatch.Signal(providing_args=['alias', 'connection', 'wrapper'])