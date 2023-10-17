from django.contrib import admin
from django.urls import path
from .views import Home_Page,category_business_list,add_review,user_login_view,register,register_reviewer,add_business,edit_business,delete_business
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView

urlpatterns = [
    path('', Home_Page, name='Home_Page'),
    path('category/<int:category_id>/', category_business_list, name='category_business_list'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change/done', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change/done', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/register/', register
         , name='register'),
    path('accounts/register_reviewer/', register_reviewer
         , name='register_reviewer'),
    path('accounts/add_business/', add_business
         , name='add_business'),
    path('accounts/edit_business/<int:passed_id>/', edit_business
         , name='edit_business'),
    path('accounts/delete_business/<int:passed_id>/', delete_business
         , name='delete_business'),
    path('accounts/add_review/<int:passed_id>/', add_review, name='add_review'),
]