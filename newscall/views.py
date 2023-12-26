from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from dotenv import load_dotenv

import os

load_dotenv()

RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')

class StoriesAPIView(APIView):
    def get(self, request):
        cached_data = cache.get('stories_list')
        if not cached_data:
            url = "https://bb-finance.p.rapidapi.com/stories/list"
            querystring = {"id":"usdjpy","template":"CURRENCY"}
            headers = {
                "X-RapidAPI-Key": RAPIDAPI_KEY,
                "X-RapidAPI-Host": "bb-finance.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)
            cached_data = response.json()
            cache.set('stories_list', cached_data, timeout=3600)  # Cache for 1 hour
        return Response(cached_data)

class StoryDetailAPIView(APIView):
    def get(self, request, internalID):
        cache_key = f'story_detail_{internalID}'
        cached_data = cache.get(cache_key)
        
        if not cached_data:
            url = "https://bb-finance.p.rapidapi.com/stories/detail"
            querystring = {"internalID": internalID}
            headers = {
                "X-RapidAPI-Key": RAPIDAPI_KEY,
                "X-RapidAPI-Host": "bb-finance.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)
            cached_data = response.json()
            cache.set(cache_key, cached_data, timeout=3600)  # Cache for 1 hour
        
        return Response(cached_data)
