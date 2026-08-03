from django.db import models

from .models import Url, Click
from django.utils import timezone

class UrlRepository:
    @staticmethod
    def creat_pending(long_url: str) -> Url:
        return Url.objects.create(long_url=long_url, short_code='')

    @staticmethod
    def set_short_code(url_obj: Url, code: str) -> None:
        url_obj.short_code = code
        url_obj.save(update_fields=['short_code'])

    @staticmethod
    def get_active_by_code(code: str) -> Url | None:
        return Url.objects.filter(
            short_code = code, is_active = True
        ).filter(
            models.Q(expires_at__isnull = True) | models.Q(expires_at__gt = timezone.now())
        ).first()

class ClickRepository:
    @staticmethod
    def record(url_obj:Url, referrer:str, ip:str, user_agent:str) -> Click:
        return Click.objects.create(
            url = url_obj, referrer = referrer, ip_address = ip, user_agent = user_agent
        )

    @staticmethod
    def stats_for_url(url_obj:Url):
        return Click.objects.filter(url = url_obj)
