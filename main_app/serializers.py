from rest_framework import serializers
from .models import FamilyMember, LifeEvent, Comment

class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LifeEventSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = LifeEvent
        fields = '__all__'
        read_only_fields = ('family_member',)
