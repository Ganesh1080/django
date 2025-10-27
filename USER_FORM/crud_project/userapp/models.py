from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, FileExtensionValidator


def validate_profile(value):
    print(value)
    max_size = 5 * 1024 * 1024
    if value.size > max_size:
        raise ValidationError("Image size should not excced in 5 MB")


class UserForm(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    phone = models.CharField(
        max_length=13,
        validators=[
            RegexValidator(
                regex=r"^\+?91[6-9]\d{9}$",
                message="phone must be start with +91 or 91 and after this must be 9/8/7/6",
            )
        ],
        unique=True,
    )
    profile = models.FileField(
        upload_to="profiles/",
        validators=[validate_profile, FileExtensionValidator(["jpeg", "png", "jpg"])],
    )

    def __str__(self):
        return self.name


# Create your models here.
