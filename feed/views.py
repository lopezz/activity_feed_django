# from django.template.response import SimpleTemplateResponse
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import TemplateView
from django.db.models import Q

from .models import FeedItem, RegisteredUser

import json


def home(request):
    pass

class Home(TemplateView):
    template_name = 'feed/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        
        #Pass all registered users to allow filtering
        registered_users = RegisteredUser.objects.all()
        context['registered_users'] = registered_users
        return context

class GetAllFeedItems(View):
    """ Returns a list containing all Feed items (not filtered) """
    def get(self, request):
        query_set = FeedItem.objects.all()
        responseData = serialize_feed_data(query_set)
        return JsonResponse(responseData, safe=False)

class GetUserFeed(View):
    """ If the parameter 'tracked' is passed, includes all tracked users's posts
    otherwhise, includes only the posts of the user specified """
    def get(self, request, user_id):
        include_tracked = request.GET.get('tracked',False)
        query_set = FeedItem.objects.filter(user__pk__contains = user_id)
        responseData = serialize_feed_data(query_set)

        # Include tracked users feed items:
        if(include_tracked):
            tracked_users = RegisteredUser.objects.get(pk=user_id).tracking.all()
            for user in tracked_users:
                user_items = FeedItem.objects.filter(user__pk__contains = user.pk)
                responseData += serialize_feed_data(user_items)
        
        return JsonResponse(responseData, safe=False)

def serialize_feed_data(feed_data):
    """ Here we can define the structure each feed item should have. """
    responseData = []
    for item in feed_data:
        responseData.append({
            'user': {'id': item.user.pk, 'name':str(item.user)},
            'content': item.content,
            'date': str(item.date_modified),
        })
    return responseData
