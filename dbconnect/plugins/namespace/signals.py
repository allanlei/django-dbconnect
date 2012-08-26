import django.dispatch


namespace_changed = django.dispatch.Signal(providing_args=['alias', 'connection', 'namespace'])