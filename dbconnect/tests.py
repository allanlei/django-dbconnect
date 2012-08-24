from django.utils import unittest
from django.contrib.auth.models import User
from django.conf import settings
from django.core.management import call_command

import random


class DBConnectTestCase(unittest.TestCase):
    def setUp(self):
        db = settings.DATABASES['default'].copy()
        db['name'] = 'dynamic.db'
        settings.DATABASES['dynamic'] = db
        call_command('syncdb', interactive=False, database='dynamic', verbosity=0)
        self.databases = settings.DATABASES.keys()
        self.stats = {}

    def testConnect(self):
        for database in self.databases:
            self.stats[database] = User.objects.using(database).count()

    def testConnectRandom(self):
        for i in range(len(self.databases)):
            database = random.choice(self.databases)
            self.stats[database] = User.objects.using(database).count()