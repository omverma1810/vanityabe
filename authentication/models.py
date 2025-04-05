from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.conf import settings

# Language choices
LANGUAGE_CHOICES = (
    ('hindi', 'Hindi'),
    ('telugu', 'Telugu'),
    ('tamil', 'Tamil'),
    ('english', 'English'),
)

# Proficiency choices
PROFICIENCY_CHOICES = (
    ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ('advanced', 'Advanced'),
)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)

    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)

    def __str__(self):
        return self.username


class LanguagePreference(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='language_preferences'
    )
    known_language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    learning_language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    proficiency = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES) 
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'known_language', 'learning_language')

    def __str__(self):
        return f"{self.user.username}: {self.known_language} ➝ {self.learning_language} ({self.proficiency})"
