from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError("You must provide valid email")
    def create_user(self, email, username = None, password = None, **extra_fields):
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError("Base User: and email address is required")
        user = self.model(username = username, email = email, **extra_fields)
        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", False)
        user.save(using = self._db)
        return user
    def create_superuser(self, email, username = None, password = None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_superuser") is not True:
           raise ValueError("Superusers must have is_superuser=True")
        if extra_fields.get("is_staff") is not True:
           raise ValueError("Superusers must have is_staff=True") 
        if not password:
           raise ValueError("Superusers must have a password")    
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError("Admin User: and email address is required")
        user = self.model(email = email, username = username, **extra_fields)
        user.set_password(password)
        user.save()
        return user