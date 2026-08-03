from .repositories import UrlRepository, ClickRepository
from .validators import is_valid_url
from .utils import encode_base62
from .exceptions import InvalidUrlError, UrlNotFoundError, UrlExpiredError


def create_short_url(long_url:str) -> dict:
    if not is_valid_url(long_url):
        raise InvalidUrlError(f"'{long_url}' is not a valid http/https URL")

    url_obj = UrlRepository.creat_pending(long_url)
    code = encode_base62(url_obj.id)
    UrlRepository.set_short_code(url_obj, code)

    return {'shortCode': code, 'longUrl':long_url}

def resolve_short_code(code:str) -> str:
    url_obj = UrlRepository.get_active_by_code(code)
    if url_obj is None:
        raise UrlNotFoundError(f'No active URL for code "{code}"')
    return url_obj

def record_click(url_obj, request) -> None:
    ClickRepository.record(
        url_obj=url_obj,
        referrer=request.META.get('HTTP_REFERER'),
        ip=request.META.get('REMOTE_ADDR'),
        user_agent=request.META.get('HTTP_USER_AGENT', '')[:256],
    )
def get_stats(code:str) -> dict:
    url_obj = UrlRepository.get_active_by_code(code)
    if url_obj is None:
        raise UrlNotFoundError(f'No active URL for code "{code}"')
    clicks = ClickRepository.stats_for_url(url_obj)
    total = clicks.count()
    from django.db.models.functions import TruncDate
    from django.db.models import Count

    per_day = (
        clicks.annotate(day=TruncDate('clicked_at'))
        .values('day')
        .annotate(count=Count('id'))
        .order_by('day')
    )
    referrers = (
        clicks.exclude(referrer__isnull=True)
        .values('referrer')
        .annotate(count=Count('id'))
        .order_by('-count')
    )

    return {
        "shortCode": code,
        "totalClicks": total,
        "clicksPerDay": list(per_day),
        "topReferrers": list(referrers),
    }