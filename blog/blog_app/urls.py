from django.urls import path

from blog_app.views import *


urlpatterns = [
    path('about', AboutView.as_view() , name='about'),
    path('', PostListView.as_view() ,name ='post_list'),
    path('post< int:pk >', PostDetails.as_view() , name ='post_details'),
    path('post/new' , createPostview.as_view() ,name='post_new'),
    path('post/<int:pk>/edit' , UpdatePostview.as_view() ,name='post_update'),
    path('post/<int:pk>/remove' , POstDeleteView.as_view() ,name='post_remove'),
    path('draft' , DraftListView.as_view() ,name='post_draft'),


]
