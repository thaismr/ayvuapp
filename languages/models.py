from django.utils.translation import gettext_lazy as _
from django.db import models


class Language(models.Model):
    # TODO: Add language code!
    name = models.CharField(max_length=50, verbose_name=_("Language"))
    slug = models.SlugField(unique=True)
    flag = models.ImageField(null=True, blank=True, upload_to='images/flags')
    summary = models.CharField(blank=True, max_length=255)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
