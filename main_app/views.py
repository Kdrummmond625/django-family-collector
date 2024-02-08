from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import FamilyMember, LifeEvent, Comment
from .serializers import FamilyMemberSerializer, LifeEventSerializer, CommentSerializer, UserSerializer

# Define the home view
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, *kwargs)
        user = User.objects.get(username=response.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': response.data
        })


# Define the login view
class LoginView(APIView):
    permissions_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refesh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            })
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
# Define the verify user view
class VerifyUserView(APIView):
    permissions_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = User.object.get(username=request.user)
        refresh = RefreshToken.for_user(request.user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        })
    
class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the Family Collector API Home Page!'}
        return Response(content)

class FamilyMemberList(generics.ListCreateAPIView):
    serializer_class = FamilyMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # this allows us to filter the family members by the current user
        user = self.request.user
        return FamilyMember.objects.filter(user=user)
    
    def perform_create(self, serializer):
        # this allows us to set the user field on the family member to the current user
        serializer.save(user=self.request.user)

class FamilyMemberDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FamilyMemberSerializer
    lookup_field = 'id'

    def get_queryset(self):
        # this allows us to filter the family members by the current user
        user = self.request.user
        return FamilyMember.objects.filter(user=user)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        comments_serializer = CommentSerializer(instance.comments.all(), many=True)


        return Response({
            'family_member': serializer.data,
            'comments': comments_serializer.data
        })
    
    def perform_update(self, serializer):
        family_member = self.get_object()
        if family_member.user != self.request.user:
            raise PermissionDenied('You do not have permission to modify this family member')
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied('You do not have permission to delete this family member')
        instance.delete()



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