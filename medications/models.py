from django.db import models
from users.models import User


class Medication(models.Model):
    name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=20)
    quantity = models.SmallIntegerField(blank=True, null=True)
    times_taken = models.SmallIntegerField(help_text="Times taken per day.")
    refills = models.SmallIntegerField(blank=True, null=True)
    prescriber = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="medications")

    def __str__(self) -> str:
        return self.name

    class Meta:
        indexes = [models.Index(fields=["name", "user"], name="medication_name_user_idx")]
