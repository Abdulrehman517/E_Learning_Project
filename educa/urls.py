from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_viws

urlpatterns = [
    path('accounts/login/', auth_viws.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_viws.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('course/', include('courses.urls')),
]
