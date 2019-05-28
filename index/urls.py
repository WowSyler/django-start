from django.urls import path
from . import views


urlpatterns = [
    path('startstory/<int:id>/',views.start_story),
    path('storydetail/<int:id>/',views.story),
    path('', views.get_story),
]