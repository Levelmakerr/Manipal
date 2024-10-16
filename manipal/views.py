from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


def index(request):
    all_locations = Location.objects.all()  # Fetch all locations from the database 
    return render(request, 'manipal/index.html', {'locations': all_locations})
    
def page(request):
    all_specialities = Speciality.objects.all()
    selected_location_id = request.GET.get('location', None)
    all_locations = Location.objects.all()

    selected_location = None
    if selected_location_id:
        try:
            selected_location = Location.objects.get(id=selected_location_id)
        except Location.DoesNotExist:
            selected_location = None

    return render(request, 'manipal/page.html', {
        'specialities': all_specialities,
        'locations': all_locations,
        'location_name': selected_location.locationname if selected_location else '',
    })


class LocationList(APIView):
    def get(self, request):
        locations = Location.objects.all()  # Fetch all locations
        serializer = LocationSerializer(locations, many=True)  # Serialize the data
        return Response(serializer.data)  # Return JSON response

class SpecialityList(APIView):
    def get(self,request):
        specialities = Speciality.objects.all()
        serializer = SpecialitySerializer(specialities, many=True)
        return Response(serializer.data)