import ciso8601

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import HttpResponse
from django.template import loader

# from .models import Article
from .services import get_measurement_list

class Meter(APIView):
    def get(self, request):
        start_query = request.query_params["start"]
        end_query = request.query_params["end"]

        try:
            start_date = ciso8601.parse_datetime(start_query)
            end_date = ciso8601.parse_datetime(end_query)

            if end_date.hour == 0 and end_date.minute == 0 and end_date.second == 0:
                end_date = end_date.replace(hour=23, minute=59, second=59)
            
        except Exception as ex:
            print(f"exception: {ex}")
            return Response({"error": "wrong parameter"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            result = get_measurement_list(start_date, end_date)
            print(f"Result: {result['start']} until {result['end']}")
        except Exception as ex:
            print(f"exception: {ex}")
            return Response({"error": "internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(result)

