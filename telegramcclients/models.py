from django.db import models
from masjid.models import Masjid

class User(models.Model):
    telegram_id = models.CharField(max_length=255, unique=True)  # Ensuring unique Telegram IDs
    district = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    masjid = models.ForeignKey(
        Masjid,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        self.district = self.district.title()
        self.region = self.region.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"User {self.telegram_id} - {self.region}, {self.district}"
