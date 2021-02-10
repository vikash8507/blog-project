from django.urls import path
from blog import views
from blog.views import AboutView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDetailView, PostDraftView

# Template tag
app_name = 'blog'

urlpatterns = [
    path('about', AboutView.as_view(), name='about'),
    path('', PostListView.as_view(), name='post_list'),
    path('post/new', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/remove', PostDetailView.as_view(), name='post_remove'),
    path('drafts', PostDraftView.as_view(), name='post_draft_list'),

    # Comment urls
    path('post/<int:pk>/comment', views.add_comment_post, name='add_comment_post'),
    path('comment/<int:pk>/approve', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove', views.comment_remove, name='comment_remove'),
    path('post/<int:pk>/publish', views.post_publish, name='post_publish'),
]
