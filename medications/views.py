from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Medication
from .serializers import MedicationSerializer


class CreateMedicationView(generics.CreateAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [IsAuthenticated]

    #  Allow multiple Medication object creation with one API call
    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True

        return super().get_serializer(*args, **kwargs)

    # Set the authenticated user as the user foreign key
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListUserMedicationsView(generics.ListAPIView):
    serializer_class = MedicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_slug = self.kwargs["slug"]

        # Ensure that the authenticated user matches the requested username
        if self.request.user.username == user_slug:
            return Medication.objects.filter(user__slug=user_slug)
        else:
            # Return an empty queryset if the authenticated user is different
            return Medication.objects.none()


class DeleteUserMedicationView(generics.DestroyAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        medication = generics.get_object_or_404(Medication, id=self.kwargs["pk"])

        # Ensure that the authenticated user matches the user of the medication
        if medication.user == self.request.user:
            return medication
        else:
            raise PermissionError("You do not have permission to delete this medication")
