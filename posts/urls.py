from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='detail'),
    path('search_results/', views.post_search, name='search_results'),
    path('filter_results/', views.filter_results, name='filter_results'),
    path('post_comments/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_comment, name='post_comments'),
]
