from django.urls import path
from.import views


urlpatterns = [
        path('api/lead/', views.CarosalListCreate.as_view()),
        path('api/about/', views.AboutListCreate.as_view()),
        path('api/users/', views.CurrentUserViewSet.as_view({'get': 'list'})),
]
