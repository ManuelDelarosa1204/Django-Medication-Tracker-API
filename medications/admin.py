from django.contrib import admin
from .models import Medication


@admin.register(Medication)
class MedicationModelAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "dosage",
        "quantity",
        "times_taken",
        "refills",
        "prescriber",
        "user",
    ]

    search_fields = ["user"]
