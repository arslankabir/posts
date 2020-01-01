from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.post_list,name='posts'),
    path('CreatePost/',views.posts_create,name='CreatePost'),
    path('author/',views.authors_create,name="author"),
    url(r'^(?P<slug>[\w-]+)/update/$',views.posts_update,name="updateform"),
    url(r'^(?P<slug>[\w-]+)/delete/$',views.posts_delete,name="deletepost"),
    url(r'^(?P<slug>[\w-]+)/$',views.posts_slug)
]