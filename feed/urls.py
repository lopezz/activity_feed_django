from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('get_feed', views.GetAllFeedItems.as_view(), name="get_feed"),
    re_path(r'^get_feed/(?P<user_id>[0-9]{1,})', views.GetUserFeed.as_view(), name="get_user_feed"),
]