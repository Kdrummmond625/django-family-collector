from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics
from .models import FamilyMember, LifeEvent, Comment
from .serializers import FamilyMemberSerializer, LifeEventSerializer, CommentSerializer

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

class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'

class AddCommentToLifeEvent(APIView):
    def post(self, request, life_event_id, comment_id):
        life_event = LifeEvent.objects.get(id=life_event_id)
        comment = Comment.objects.get(id=comment_id)
        life_event.comments.add(comment)
        return Response({'message': 'Comment added successfully!'})