from rest_framework import serializers 
from .models import UserBooking , Service
import datetime 
class UserBookingSerializer(serializers.ModelSerializer):
    #to vaidate against time passed
    status = serializers.SerializerMethodField()
    service = serializers.StringRelatedField()
    class Meta:
        model = UserBooking
        fields = ('__all__')
    #custome validation for phone number
    def validate_phone_number(self,phone_number):
        if phone_number[0:4] != "+973" or len(phone_number) != 14 :
            raise serializers.ValidationError("Phone Number Must be In The Following Foramt +973 XX XXXX XXXX")
        return phone_number    
    #get_<SerializerMethodField name>
    def get_status(self,data):
        data.status =  "Not Available"  if data.end_date < datetime.date.today()  else "Available"
        return data.status

class ServiceSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Service   