from django.db import models

class Masjid(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    district = models.CharField(max_length=255, blank=False, null=False)
    region = models.CharField(max_length=255, blank=False, null=False)
    location_url = models.CharField(max_length=1000, blank=False, null=False)
    contact = models.CharField(max_length=255, blank=True, null=True, default="ma'lumot yo'q")

    bomdod = models.CharField(max_length=255, blank=False, null=False, default="vaqt")
    quyosh = models.CharField(max_length=255, blank=False, null=False, default="vaqt")
    peshin = models.CharField(max_length=255, blank=False, null=False, default="vaqt")
    asr = models.CharField(max_length=255, blank=False, null=False, default="vaqt")
    shom = models.CharField(max_length=255, blank=False, null=False, default="vaqt")
    xufton = models.CharField(max_length=255, blank=False, null=False, default="vaqt")

    def save(self, *args, **kwargs):
        self.district = self.district.title()
        self.region = self.region.title()
        self.name = self.name.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}. {self.name}"
