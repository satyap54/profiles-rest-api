from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password = None):
        """Create a new user profile"""
        if not email :
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email = email, name = name)

        #Hash the password
        user.set_password(password)

        #Save the user's data.
        #Django supports multiple dbs, kw : "using"
        user.save(using = self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True # This field is provided by default in PermissionMixin
        user.is_staff = True
        user.save(using = self.db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    email= models.EmailField(max_length=255, unique=True)
    name= models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserProfileManager()

    #For working with django authentication sys
    USERNAME_FIELD = 'email' # during login
    REQUIRED_FIELDS = ['name'] # Auxiliary fields for user creation

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name
    
    def get_short_name(self):
        return self.name

    def __str__(self):
        """ Return string representation of our user"""
        return self.email


class ProfileFeedItem(models.Model):
    """ Profile status update """
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    status_text = models.CharField(max_length = 255)
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.status_text

