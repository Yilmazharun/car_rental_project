from contactmessages.api import views
from django.urls import path

urlpatterns = [
    path("visitors/", views.MessageCreateAPIView.as_view(), name="create_message"),
    path("", views.MessageListAPIView.as_view(), name="list_all_messages"),
    path("request/", views.MessageListAPIView.as_view(), name="list_request_messages"),
    path("pages/", views.MessageListAPIView.as_view(), name="message_list_pages"),
    path("<int:pk>/", views.MessageDetail.as_view(), name="message_detail"),
]