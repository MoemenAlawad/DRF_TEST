from django.shortcuts import render
from .serializer import UserBookingSerializer
from .models import UserBooking
from rest_framework import generics
import datetime
# Create your views here.
def valide_date(date):
    year,month,day = date.split('-')
    try:
        datetime.datetime(int(year),int(month),int(day))
        return True 
    except ValueError:
        return False    

class ListBookingView(generics.ListAPIView):
    serializer_class = UserBookingSerializer
    def get_queryset(self):
        queryset = UserBooking.objects.all()
        start_date = self.request.query_params.get('startdate')
        end_date =self.request.query_params.get('enddate')
        service =self.request.query_params.get('service')
        if start_date and valide_date(start_date):
            queryset = queryset.filter(start_date = start_date)
        if end_date and valide_date(end_date):
            queryset = queryset.filter(end_date = end_date)
        if service:
            queryset = queryset.filter(service = service)
        return queryset

class CreateBookingView(generics.CreateAPIView):
    serializer_class = UserBookingSerializer
    