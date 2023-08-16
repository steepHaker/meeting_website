from . import views
from django.urls import path

urlpatterns = [    
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('acquaintance/<int:user_id>/', views.user_details, name='user_details'),
    path('acquaintance/', views.acquaintance_get, name='acquaintance'),
    path('create-user-info/', views.CreateUserInfoView.as_view(), name='create_user_info'),
    path('edit-user-info/<int:pk>/', views.EditUserInfoView.as_view(), name='edit-user-info'),
    path('', views.UserRegistr, name='registration'),  
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('delete_account/', views.delete_account, name='delete_account'),
]


