from django.db import connections

from exceptions import DatabaseAliasNotFound


def reverse(connection, mapping=connections):
    for alias in mapping:
        if mapping[alias] == connection:
            return alias
    raise DatabaseAliasNotFound()