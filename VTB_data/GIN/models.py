from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    ROLE = (("common", "Common"), ("admin", "Admin"), ("company", "Company"))
    role = models.CharField(max_length=20, choices=ROLE, default="common", db_column='role')
    login = models.CharField(max_length=255, unique=True, db_column='login')
    password = models.CharField(max_length=100, db_column='password')
    name = models.CharField(max_length=150, db_column='name')
    surname = models.CharField(max_length=250, db_column='surname')

    class Meta:
        managed = True
        db_table = 'User'

class Categories(models.Model):
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        managed = True
        db_table = 'Category'

class File(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    _data = models.TextField(
        db_column='data',
        blank=True)

    def set_data(self, data):
        self._data = base64.encodestring(data)

    def get_data(self):
        return base64.decodestring(self._data)

    data = property(get_data, set_data)

    class Meta:
        managed = True
        db_table = 'File'