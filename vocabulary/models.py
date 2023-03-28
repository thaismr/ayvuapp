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


class PartOfSpeech(models.Model):
    """
    Part of speech data structure
    """
    part_of_speech = models.CharField(_('Part of speech'), max_length=150)
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name='part_of_speech',
        verbose_name=_('Language')
    )

    class Meta:
        ordering = ['language', 'part_of_speech']
        verbose_name = _('part of speech')
        verbose_name_plural = _('part of speeches')
        unique_together = ['part_of_speech', 'language']

    def __str__(self):
        return f'{self.part_of_speech} ({self.language})'


class Vocabulary(models.Model):
    """
    Each vocabulary data structure
    """
    word = models.CharField(_('Word'), max_length=150)
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


class VocabularyDefinition(models.Model):
    """
    Vocabulary definition data structure
    """
    definition = models.TextField(_('Definition'))
    usage = models.TextField(_('Usage'))
    part_of_speech = models.ForeignKey(
        PartOfSpeech,
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name='definitions',
        verbose_name=_('Part of speech')
    )
    vocabulary = models.ForeignKey(
        Vocabulary,
        on_delete=models.CASCADE,
        related_name='definitions',
        verbose_name=_('Vocabulary')
    )
    history = HistoricalRecords()


class VocabularyExample(models.Model):
    """
    Vocabulary example data structure
    """
    example = models.TextField(_('Example'))
    definition = models.ForeignKey(
        VocabularyDefinition,
        on_delete=models.CASCADE,
        related_name='examples',
        verbose_name=_('Definition')
    )
