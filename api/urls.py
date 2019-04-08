from django.urls import path , include
from .views import CreateBookingView ,ListBookingView
urlpatterns = [
    #to creat new booking
    path('newbooking/',CreateBookingView.as_view() ),
    #to get all bookings
    path('getallbookings/',ListBookingView.as_view() ),
]
