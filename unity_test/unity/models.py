from django.db import models

# Create your models here.


class EmailSubscription(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    is_subscribed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Email Subscriptions"
