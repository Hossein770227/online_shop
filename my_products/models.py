
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class Product(models.Model):
    name = models.CharField(_("name"), max_length=100)
    description = models.TextField(_("description"))
    short_description = models.CharField(_("short text"), blank=True, max_length=200)
    image = models.ImageField(_("image"), upload_to='cover',blank=True)
    price = models.PositiveIntegerField(_("price"))
    price_with_discount = models.PositiveIntegerField(_("price with discount"), blank=True, null=True)
    active = models.BooleanField(_("active"), default=True)
    date_time_created = models.DateTimeField(_("date time created"), auto_now_add=True)
    date_time_modified = models.DateTimeField(_("date time modified"), auto_now=True)

    class Meta:
        verbose_name = _('products')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("products:product_detail", args=[self.id])


class Comment(models.Model):
    STARS_CHOICES = [
        (1 , _("very bad")),
        (2 , _(" bad")),
        (3 , _("normal")),
        (4 , _("good")),
        (5 , _("prefect")),
    ]

    author = models.ForeignKey(get_user_model(), verbose_name=_(""), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    stars = models.CharField(_("star"), max_length=50, choices=STARS_CHOICES)
    active = models.BooleanField(_("active"), default=True)
    date_time_created = models.DateTimeField(_("date time created"), auto_now_add=True)
    date_time_modified = models.DateTimeField(_("date time modified"), auto_now=True)

    class Meta:
        verbose_name = _('comments')
        verbose_name_plural = _('comments')

    def __str__(self):
        return f'{self.author} : comment for {self.product}' 