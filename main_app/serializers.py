from rest_framework import serializers
from .models import FamilyMember, LifeEvent

class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = '__all__'

class LifeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifeEvent
        fields = '__all__'
        read_only_fields = ('family_member',)