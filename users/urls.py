from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("", views.UserListCreateView.as_view(), name="list-create-users"),
    path("<slug:slug>/", views.UserRetrieveDestroyView.as_view(), name="retrieve-destroy-user"),
]
