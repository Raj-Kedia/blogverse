from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("postComment", views.postComment, name="postComment"),
    path("", views.blogHome, name="bloghome"),
    path("<str:slug>", views.blogPost, name="blogPost"),
    path("createblog", views.create_blog, name='createblog')
    # path("viewprofile", views.viewprofile, name="viewprofile"),
]
