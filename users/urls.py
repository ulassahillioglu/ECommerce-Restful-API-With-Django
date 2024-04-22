from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path('login/',views.login,name="login"),
    re_path('signup/',views.signup,name="sign_up"),
    re_path('test_token/',views.test_token,name="test_token"),
    re_path('is_superuser/', views.is_superuser, name='is_superuser'),
]
