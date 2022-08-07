from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from django.db.models import Q
from django.urls import reverse

from .models import Material


class MaterialCreateView(LoginRequiredMixin, CreateView):
    model = Material
    fields = [
        'title', 'description', 'url', 'public', 'language', 'level',
        'vocabulary'
    ]

    def get_success_url(self):
        return reverse('material:detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)


class MaterialDetailView(LoginRequiredMixin, DetailView):
    model = Material
    context_object_name = 'material'

    def get_queryset(self):
        """Verify user has access to material."""
        user_id = self.request.user.pk
        return self.model.objects.select_related(
            'publisher', 'language').prefetch_related('vocabulary').filter(
                Q(publisher=user_id) | Q(public=True))


class MaterialListView(LoginRequiredMixin, ListView):
    model = Material
    paginate_by = 15

    def get_queryset(self):
        """Verify user has access to material."""
        user_id = self.request.user.pk
        return self.model.objects.select_related(
            'publisher', 'language').prefetch_related('vocabulary').filter(
                Q(publisher=user_id) | Q(public=True))
