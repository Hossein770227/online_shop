from django.db import models
from django.utils.translation import gettext_lazy as _

class Prouduct(models.Model):
    name = models.CharField(_("name"), max_length=100)
    description = models.TextField(_("description"))
    short_description = models.CharField(_("short text"), blank=True, max_length=200)
    price = models.PositiveIntegerField(_("price"))
    price_with_discount = models.PositiveIntegerField(_("price with discount"), blank=True, null=True)
    active = models.BooleanField(_("active"), default=True)
    date_time_created = models.DateTimeField(_("date time created"), auto_now_add=True)
    date_time_modified = models.DateTimeField(_("date time modified"), auto_now=True)

    def __str__(self):
        return self.name


