from django.conf import settings
from django.test import Client, SimpleTestCase, TestCase, override_settings

from .models import Click, Url
from .services import get_stats


class ShortenerSettingsTests(SimpleTestCase):
    def test_default_base_url_is_configured(self):
        self.assertEqual(getattr(settings, 'BASE_URL', None), 'http://localhost:8000')


@override_settings(DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory:'}})
class StatsServiceTests(TestCase):
    def test_get_stats_returns_stats_for_existing_url(self):
        url_obj = Url.objects.create(short_code='abc123', long_url='https://example.com', is_active=True)
        Click.objects.create(url=url_obj, referrer='https://ref.example', ip_address='127.0.0.1', user_agent='test-agent')

        data = get_stats('abc123')

        self.assertEqual(data['shortCode'], 'abc123')
        self.assertEqual(data['totalClicks'], 1)
        self.assertEqual(data['topReferrers'][0]['referrer'], 'https://ref.example')


class IndexViewTests(TestCase):
    def test_root_view_returns_html_page(self):
        response = Client().get('/', HTTP_HOST='localhost')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'SHORTWIRE')
