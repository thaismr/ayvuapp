from django.utils.translation import gettext_lazy as _
from django.db import models

#: custom user model
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from simple_history.models import HistoricalRecords
from languages.models import Language


class User(AbstractUser):
    """
    Allow for updatable User models without breaking foreign keys.
    """
    is_premium = models.BooleanField(_('Premium'), default=False)
    ux_enabled = models.BooleanField(_('Participate in Research'), default=False)
    active_language = models.ForeignKey(Language,
                                        default=1,
                                        on_delete=models.SET(1))


class ProxyUser(User):
    """Custom user proxy model for digested admin management."""

    class Meta:
        verbose_name = _('Digested user')
        verbose_name_plural = _('Digested users')
        proxy = True


class UserProfile(models.Model):
    """Extra profile data for default users."""

    class Gender(models.TextChoices):
        FEMALE = 'F', _('Female')
        MALE = 'M', _('Male')
        OTHER = 'O', _('Other')

    class Education(models.TextChoices):
        NO_SCHOOL = 'NONE', _('No schooling completed')
        EIGHTH = 'EIGH', _('Nursery school to 8th grade')
        SOME_SCHOOL = 'SCHO', _('Some high school, no diploma')
        HIGH_SCHOOL = 'HIGH', _('High school equivalent')
        SOME_COLLEGE = 'SOME', _('Some college, no degree')
        TECHNICAL = 'TECH', _('Technical training')
        ASSOCIATE = 'ASSO', _('Associate degree')
        BACHELOR = 'BACH', _('Bachelor’s degree')
        MASTERS = 'MAST', _('Master’s degree')
        PROFESSIONAL = 'PROF', _('Professional degree')
        DOCTORATE = 'DOCT', _('Doctorate degree')

    class MaritalStatus(models.TextChoices):
        SINGLE = 'S', _('Single, never married')
        MARRIED = 'M', _('Married or domestic partnership')
        WIDOWED = 'W', _('Widowed')
        DIVORCED = 'D', _('Divorced')

    #: User pk as profile pk
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name='user_profile',
    )
    bio = models.CharField(_('Bio'), max_length=50, blank=True)
    website = models.URLField(_('Website'), max_length=255, blank=True)
    birth_date = models.DateField(_('Birth date'), null=True, blank=True)
    gender = models.CharField(
        _('Gender'),
        max_length=1,
        choices=Gender.choices,
        default=None,
        blank=True,
        null=True
    )
    education = models.CharField(
        _('Education'),
        max_length=4,
        choices=Education.choices,
        default=None,
        blank=True,
        null=True
    )
    marital_status = models.CharField(
        _('Marital Status'),
        max_length=1,
        choices=MaritalStatus.choices,
        default=None,
        blank=True,
        null=True
    )
    first_language = models.ForeignKey(
        Language,
        null=True,
        blank=True,
        default=None,
        on_delete=models.SET_NULL,
        verbose_name=_('First language')
    )
    speaks = models.ManyToManyField(
        Language,
        related_name='speakers',
        verbose_name=_('Languages spoken')
    )
    history = HistoricalRecords()

    def __str__(self):
        return str(self.user)
