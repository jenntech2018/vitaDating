from django.urls import path
from vibe_user import views

urlpatterns = [
    path('@<str:username>', views.vibe_user_profile_view, name='profile'),
    path('edit/@<str:username>', views.EditProfileView.as_view(), name='edit_profile'),
    path('settings', views.settings_page, name='settings'),
    path('delete-account/', views.delete_account, name="delete_account"),
    path('search/', views.search_accounts, name="search_accounts")
]