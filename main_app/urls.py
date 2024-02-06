from django.urls import path
from .views import Home, FamilyMemberList, FamilyMemberDetail, LifeEventListCreate, LifeEventDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('familymembers/', FamilyMemberList.as_view(), name='familymember_list'),
    path('familymembers/<int:pk>/', FamilyMemberDetail.as_view(), name='familymember_detail'),
    path('familymembers/<int:family_member_id>/lifeevents/', LifeEventListCreate.as_view(), name='lifeevent_list'),
    path('familymembers/<int:family_member_id>/lifeevents/<int:pk>/', LifeEventDetail.as_view(), name='lifeevent_detail'),
]
