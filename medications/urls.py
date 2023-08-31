from django.urls import path
from . import views

app_name = "medications"

urlpatterns = [
    path("create/", views.CreateMedicationView.as_view(), name="create-medications"),
    path("<slug:slug>/", views.ListUserMedicationsView.as_view(), name="list-user-medication"),
    path("<slug:slug>/<int:pk>/delete/", views.DeleteUserMedicationView.as_view(), name="delete-user-medication"),
]
