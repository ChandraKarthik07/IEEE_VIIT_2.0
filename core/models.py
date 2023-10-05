from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission
from django.utils import timezone
import uuid

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(default=uuid.uuid4, null=True, unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField("email address", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    # Specify unique related names for groups and user_permissions
    groups = models.ManyToManyField(Group, related_name='users')
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='users',
        verbose_name='user permissions',
        blank=True,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Event(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='event_images/')
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.title} on {self.date}"

from django.db import models

# Constants for Committee Roles
EXECUTIVE_ROLES = (
    ('Chair', 'Chair'),
    ('Vice Chair', 'Vice Chair'),
    ('Secretary', 'Secretary'),
    ('Treasurer', 'Treasurer'),
    # Add other Executive Committee roles here
)

OPERATING_ROLES = (
    ('Program Committee', 'Program Committee'),
    ('Publicity Committee', 'Publicity Committee'),
    ('Membership Committee', 'Membership Committee'),
    ('Nominating Committee', 'Nominating Committee'),
    ('Social Media Committee', 'Social Media Committee'),
    ('Assistant Committee', 'Assistant Committee'),
    ('Volunteers and Regular Branch members', 'Volunteers and Regular Branch members'),
    # Add other Operating Committee roles here
)
# DEFAULT_FACULTY_LEVEL = 'FACULTY'


class ExecutiveBody(models.Model):
    name= models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='profiles/',default='profiles/default.jpg')
    level = models.IntegerField()
    role = models.CharField(max_length=50, choices=EXECUTIVE_ROLES)  # Use choices here
    description = models.TextField()
    instagram_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.name

class OperatingBody(models.Model):
    name= models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='profiles/',default='profiles/default.jpg')
    level = models.IntegerField()
    role = models.CharField(max_length=50, choices=OPERATING_ROLES)  # Use choices here
    description = models.TextField()
    instagram_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.name

class Faculty(models.Model):
    name= models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='profiles/',default='profiles/default.jpg')
    level = models.IntegerField()
    description = models.TextField()
    instagram_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.name
