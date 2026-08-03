# Create your models here.
from django.db import models

class Url(models.Model):
    short_code = models.CharField(max_length=10, unique=True, db_index=True, blank=True)
    long_url = models.CharField(max_length=2048)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True, db_index=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'urls'

class Click(models.Model):
    url = models.ForeignKey(Url, on_delete=models.CASCADE, related_name='clicks')
    clicked_at = models.DateTimeField(auto_now_add=True)
    referrer = models.CharField(max_length=512, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        db_table = 'clicks'
        indexes = [
            models.Index(fields=['url', 'clicked_at'], name='idx_url_id_clicked_at'),
        ]