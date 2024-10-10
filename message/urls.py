from django.urls import path, include
from rest_framework.routers import DefaultRouter
from message.views.message_view import MessageViewSet

router = DefaultRouter()
router.register(r'message', MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)),
]