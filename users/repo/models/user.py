from gando.models import AbstractBaseModelFaster

from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models


@deconstructible
class UnicodePhoneNumberValidator(validators.RegexValidator):
    regex = r"^([0-9]){10}$"
    message = _(
        "Enter a valid phone_number.\n"
        "Sample 9123456789"
    )
    flags = 0


class User(AbstractUser, AbstractBaseModelFaster):
    profileimageid = models.PositiveBigIntegerField(
        verbose_name=_('Profile Image ID'),
        blank=True,
        null=True,
    )

    username_validator = UnicodePhoneNumberValidator()

    username = models.CharField(
        verbose_name=_('Username'),
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        db_index=True,
        help_text=_(
            'Required.\nSample 9123456789'
        ),
        validators=[username_validator],
        error_messages={
            'unique': _('A user with that username already exists.'),
        },
    )

    def __str__(self):
        return f'{self.username}'

    @property
    def profileimage(self):
        from mediamanagers.services import image_loader

        return image_loader(self.profileimageid)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        swappable = 'AUTH_USER_MODEL'
