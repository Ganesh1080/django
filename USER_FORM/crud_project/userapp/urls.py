from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.user_details,name='list'),
    path("register/", views.user_register,name='register'),
    path("update/<int:id>/", views.user_update, name='update'),
    path("delete/<int:id>/", views.user_delete,name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
