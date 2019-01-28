from django.db import models
from django.contrib.postgres.fields import JSONField
from multiselectfield import MultiSelectField
import uuid
import secrets
from django.contrib.auth.models import User
from itertools import islice


class UserLoginManager(models.Manager):
    def create_token(self):
        token = secrets.token_hex(20)
        if super().get_queryset().filter(api_token=token).exists():
            return self.create_token()
        return token
    def save_token(self, user):
        token = self.create_token()
        if UserLogin.objects.filter(user=user).exists():
            raise ValueError('Token Already Exist.')
        userlogin = UserLogin(api_token=token, user=user)
        userlogin.save()

class StudentDetail(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    student_code = models.CharField(max_length=10)
    detail_data = JSONField()


class Color(models.Model):
    RED = 'RED'
    WHITE = 'WHITE'
    BLUE = 'BLUE'

    COLOR_CHOICES = (
        (RED, 'RED'),
        (WHITE, 'WHITE'),
        (BLUE, 'BLUE')
    )
    MY_CHOICES = (('item_key1', 'Item title 1.1'),
                  ('item_key2', 'Item title 1.2'),
                  ('item_key3', 'Item title 1.3'),
                  ('item_key4', 'Item title 1.4'),
                  ('item_key5', 'Item title 1.5'))

    color = models.CharField(max_length=5, choices=COLOR_CHOICES, default=RED)

    my_field = MultiSelectField(choices=MY_CHOICES)

    class Meta:
        db_table = 'color'

    def __str__(self):
        return self.color + ' ' + self.my_field


class StudentManager(models.Manager):
    def update_student(self):
        pass


class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = models.IntegerField(null=True)
    student_object = StudentManager()

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.name + ' ' + self.last_name


class RandomUserManager(models.Manager):
    def create_code(self):
        code = uuid.uuid4()
        if super().get_queryset().filter(code=code).exists():
            return self.create_code()
        return code

    def save_data(self, data):
        for obj in data:
            obj.code = self.create_code()
        RandomUser.user_obj.bulk_create(data)


class RandomUser(models.Model):
    name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    mobile_number = models.CharField(max_length=50, null=False)
    age = models.CharField(max_length=3)
    code = models.UUIDField(unique=True)
    user_obj = RandomUserManager()

    class Meta:
        db_table = 'randomuser'

    def __str__(self):
        return self.name + ' ' + self.last_name + ' -> ' + str(self.code)

class UserLogin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    api_token = models.CharField(max_length=100)
    objects = UserLoginManager()
