from django.urls import path
from blog.views import AboutView, PostListView, PostDetailView, PostCreateView, PostUpdateView

# Template tag
app_name = 'blog'

urlpatterns = [
    path('about', AboutView.as_view(), name='about'),
    path('', PostListView.as_view(), name='post_list'),
    path('post/new', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit', PostUpdateView.as_view(), name='post_edit'),
]
