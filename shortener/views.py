from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect
from django.conf import settings

from .serializers import ShortenRequestSerializer
from .services import create_short_url, resolve_short_code, record_click, get_stats
from .exceptions import InvalidUrlError, UrlNotFoundError


class IndexView(APIView):
    def get(self, request):
        return render(request, 'shortener/index.html')


class ShortenView(APIView):
    def post(self, request):
        serializer = ShortenRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            result = create_short_url(serializer.validated_data['longUrl'])
        except InvalidUrlError as e:
            return Response({"error": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        short_url = f"{settings.BASE_URL}/{result['shortCode']}"
        return Response(
            {"shortCode": result['shortCode'], "shortUrl": short_url},
            status=status.HTTP_201_CREATED,
            headers={"Location": short_url},
        )

class RedirectView(APIView):
    def get(self, request, short_code):
        try:
            url_obj = resolve_short_code(short_code)
        except UrlNotFoundError:
            return Response(status=status.HTTP_404_NOT_FOUND)

        record_click(url_obj, request)
        return HttpResponseRedirect(url_obj.long_url)

class StatsView(APIView):
    def get(self, request, short_code):
        try:
            data = get_stats(short_code)
        except UrlNotFoundError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(data, status=status.HTTP_200_OK)