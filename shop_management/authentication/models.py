
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from authentication.managers import CustomUserManager
from django.utils import timezone
import uuid
import datetime

class UserModel(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    profile = models.ImageField(upload_to="profile", null=True, blank=True)
    position = models.CharField(max_length=100, null=True,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    last_active = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email or "User"
    
    # admin panel pernissin off

    # def has_permission(self, perm_codename):
    #     return (
    #         self.role and self.role.permissions.filter(codename=perm_codename).exists()
    #     )

    # def has_module_perms(self, app_label):
    #     return (
    #         self.role
    #         and self.role.permissions.filter(content_type__app_label=app_label).exists()
    #     )




