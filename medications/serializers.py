from rest_framework import serializers
from .models import Medication


class MedicationBulkCreate(serializers.ListSerializer):
    def create(self, validated_data):
        medications = [Medication(**items) for items in validated_data]
        return Medication.objects.bulk_create(medications)


class MedicationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Medication
        fields = "__all__"
        list_serializer_class = MedicationBulkCreate
