from django.urls import path
from . import views
app_name = 'my_app_name'

urlpatterns = [
    path('', views.login_page, name='main'),
    path('all_items', views.get_all_items, name='all_items'),
    path('users', views.get_my_profile, name='userinfo'),
    path('add_new_item/', views.add_item, name='add'),
    path('my_profile/', views.get_my_profile, name='myprofile'),
    path('signup_information/', views.user_signup_details, name='user_signup_details'),
    path('/all_items/<slug:slug>/', views.get_item_details, name='item_details')
]
