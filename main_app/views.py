from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics
from .models import FamilyMember, LifeEvent
from .serializers import FamilyMemberSerializer, LifeEventSerializer

# Define the home view
class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the Family Collector API Home Page!'}
        return Response(content)

class FamilyMemberList(generics.ListCreateAPIView):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer

class FamilyMemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer
    lookup_field = 'id'

class LifeEventListCreate(generics.ListCreateAPIView):
    serializer_class = LifeEventSerializer

    def get_queryset(self):
        family_member_id = self.kwargs['family_member_id']
        return LifeEvent.objects.filter(family_member=family_member_id)
    
    def perform_create(self, serializer):
        family_member_id = self.kwargs['family_member_id']
        family_member = FamilyMember.objects.get(id=family_member_id)
        serializer.save(family_member=family_member)

class LifeEventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LifeEventSerializer
    lookup_field = 'id'

    def get_queryset(self):
        family_member_id = self.kwargs['family_member_id']
        return LifeEvent.objects.filter(family_member=family_member_id)
