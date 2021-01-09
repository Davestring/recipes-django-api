"""Core model modules."""

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class CustomUserManager(BaseUserManager):
    """CustomUserManager.

    Implements utilities for the CustomUser Model.

    Methods
    -------
    create_user(email='', password='', **kwargs)
        Create a new user and persists it into the database.

    """

    def create_user(self, email: str, password: str, **kwargs: dict):
        """Create User.

        Create a new user and persists it into the database.

        Parameters
        ----------
        email : str
            User email address.
        password : str
            User custom password
        kwargs : dict

        """
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """CustomUser Model.

    Extends the AbstractBaseUser class and defines the custom fields for a
    new application User.

    Attributes
    ----------
    email : str
        User email address.
    name : str
        User name.
    lastname : str
        User lastname.
    is_active : bool
        True if the user is active, otherwise False.
    objects : CustomUserManager
        Utility methods.
    USERNAME_FIELD : str
        Name descriptor of the field on the user model that will be used as
        unique identifier.

    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
