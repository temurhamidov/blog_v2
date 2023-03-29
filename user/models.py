from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# def validate_check_birth(value):
#     if 1900 >= value or value >= 2023:
#         raise ValidationError(f"Siz to\'g\'ilgan yilingizni xato kiritdingiz",
#             params={'value' : value}
#         )


class User(AbstractUser):
    image = models.ImageField(upload_to='user/')
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return None