from django.urls import path

from chat_app.web.views import ChatView

urlpatterns = [
    path('', ChatView.as_view(), name='chat view'),
]
