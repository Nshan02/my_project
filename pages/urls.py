from django.urls import path
from .views import HomePageView,DetailPageView,PostCreateView,PostDelateView,PostUpdateView

urlpatterns =[
    path('',HomePageView.as_view(),name = 'home'),
    path('post/<int:pk>/', DetailPageView.as_view(),name = "detail"),
    path('post/delete/<int:pk>/',PostDelateView.as_view(),name= 'delete'),
    path('post/update/<int:pk>/',PostUpdateView.as_view(),name= 'update'),
    path("new/",PostCreateView.as_view(),name="create_post"),
]
