from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db import models

from simple_history.models import HistoricalRecords

from languages.models import Language
from vocabulary.models import Level, Vocabulary

from .managers import ResourceManager


class Resource(models.Model):
    """
    Model for language learning resources
    """
    title = models.CharField(_('Title'), max_length=250)
    description = models.TextField(_('Description'))
    url = models.URLField(_('URL'), null=True, blank=True, default=None)
    public = models.BooleanField(_('Public'), default=False)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name='user_resources',
        verbose_name=_('Owner'),
    )
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name='resources',
        verbose_name=_('Language')
    )
    level = models.CharField(
        _('Level'),
        max_length=4,
        choices=Level.choices,
        default=None,
        blank=True,
        null=True
    )
    vocabulary = models.ManyToManyField(
        Vocabulary,
        blank=True,
        related_name='resources',
        verbose_name=_('Vocabulary'),
    )
    history = HistoricalRecords()

    objects = ResourceManager()

    class Meta:
        verbose_name = _('resource')
        verbose_name_plural = _('resources')
        unique_together = ['title', 'owner', 'language']

    def __str__(self):
        return self.title
