from django.urls import path
from . import views
urlpatterns = [
    path('blog/<int:blog_id>/view', views.single_blog, name='single_blog'),
    path('blog/<int:blog_id>/leave_comment_to_blog', views.leave_comment_to_blog, name='leave_comment_to_blog'),
    path('blog/<int:blog_id>/comment/<int:comment_id>/delete', views.delete_comment, name='delete_comment'),
    path('blog/<int:blog_id>/add_or_remove_like', views.add_or_remove_like, name='add_or_remove_like'),
    path('blog/like_ajax', views.add_or_remove_like_ajax, name='add_or_remove_like_ajax'),
    ]