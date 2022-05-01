from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db import models

from simple_history.models import HistoricalRecords

from languages.models import Language


class Level(models.TextChoices):
    """Common European Framework of Reference (CEFR)"""
    A1 = 'A1', _('A1')
    A2 = 'A2', _('A2')
    B1 = 'B1', _('B1')
    B2 = 'B2', _('B2')
    C1 = 'C1', _('C1')
    C2 = 'C2', _('C2')


class Vocabulary(models.Model):
    """
    Each vocabulary data structure
    """
    word = models.CharField(_('Word'), max_length=150)
    definition = models.TextField(_('Definition'))
    public = models.BooleanField(_('Public'), default=False)

    publisher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name='user_vocabulary',
        verbose_name=_('Publisher'),
    )
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name='vocabulary',
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
    #: https://stackoverflow.com/questions/1968596/django-limit-choices-to-is-this-correct
    synonyms = models.ManyToManyField(
        'self',
        blank=True,
        verbose_name=_('Synonyms'),
    )
    history = HistoricalRecords()

    class Meta:
        verbose_name = _('vocabulary')
        verbose_name_plural = _('vocabularies')
        unique_together = ['word', 'publisher', 'language']

    def __str__(self):
        return self.word
