from django.urls import path
from .views import Home, FamilyMemberList, FamilyMemberDetail, LifeEventListCreate, LifeEventDetail, CommentListCreate, CommentDetail, AddCommentToLifeEvent

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('familymembers/', FamilyMemberList.as_view(), name='familymember_list'),
    path('familymembers/<int:pk>/', FamilyMemberDetail.as_view(), name='familymember_detail'),
    path('familymembers/<int:family_member_id>/lifeevents/', LifeEventListCreate.as_view(), name='lifeevent_list'),
    path('familymembers/<int:family_member_id>/lifeevents/<int:pk>/', LifeEventDetail.as_view(), name='lifeevent_detail'),
    path('lifeevents/<int:life_event_id>/add_comment/<int:comment_id>/', AddCommentToLifeEvent.as_view(), name='add_comment_to_life_event'),
    path('comments/', CommentListCreate.as_view(), name='comment_list'),
    path('comments/<int:id>/', CommentDetail.as_view(), name='comment_detail'),
]
