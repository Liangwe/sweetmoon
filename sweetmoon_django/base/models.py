from django.db import models

# Create your models here.
from sweetmoon_django.utils.field_methods import UnixTimestampField, CustomCharField


class BaseDatabase(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = UnixTimestampField()
    last_modify_time = UnixTimestampField(auto_created=True)

    class Meta:
        abstract = True


class UserInfo(BaseDatabase):
    username = CustomCharField(max_length=100)
    nickname = CustomCharField(max_length=50, null=True)
    password = models.TextField()
    salt = CustomCharField(max_length=50)
    note = models.TextField(null=True)  # 个人简述
    phone = CustomCharField(max_length=11, null=True)
    email = CustomCharField(max_length=255, null=True)
    github = models.TextField(null=True)
    last_login_time = models.DateTimeField(null=True)

    class Meta:
        db_table = "user_info"
