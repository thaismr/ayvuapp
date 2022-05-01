from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView
from django.urls import reverse

from .models import Vocabulary


class VocabularyCreateView(LoginRequiredMixin, CreateView):
    model = Vocabulary
    fields = ['word', 'definition', 'public', 'language', 'level', 'synonyms']

    def get_success_url(self):
        return reverse('vocabulary:detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)


class VocabularyDetailView(LoginRequiredMixin, DetailView):
    model = Vocabulary
    context_object_name = 'vocabulary'

    def get_queryset(self):
        """Verify user has access to vocabulary."""
        return super().get_queryset().select_related(
            'publisher', 'language').prefetch_related('materials')
