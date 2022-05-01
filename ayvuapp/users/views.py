from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView
from django.urls import reverse

from .models import UserProfile

import logging

logger = logging.getLogger(__name__)


class UserProfileCreate(LoginRequiredMixin, CreateView):
    model = UserProfile
    fields = [
        'bio', 'website', 'birth_date', 'gender', 'education', 'marital_status',
        'first_language', 'speaks'
    ]

    def get_success_url(self):
        return reverse('profile:detail',
                       kwargs={'username': self.object.user.username})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserProfileDetail(LoginRequiredMixin, DetailView):
    model = UserProfile
    slug_field = 'user__username'
    slug_url_kwarg = 'username'
    context_object_name = 'profile'

    def get_queryset(self):
        """User can only see their own profile."""
        logger.warning('Test logging')
        return super().get_queryset().select_related(
            'user',
            'first_language').filter(user__username=self.request.user.username)
