from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from django.db.models import Q
from django.urls import reverse

from .models import Resource


class ResourceCreateView(LoginRequiredMixin, CreateView):
    model = Resource
    fields = [
        'title', 'description', 'url', 'public', 'language', 'level',
        'vocabulary'
    ]

    def get_success_url(self):
        return reverse('resource:detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ResourceDetailView(LoginRequiredMixin, DetailView):
    model = Resource
    context_object_name = 'resource'

    def get_queryset(self):
        """Verify user has access to resource."""
        user_id = self.request.user.pk
        return self.model.objects.select_related(
            'owner', 'language').prefetch_related('vocabulary').filter(
                Q(owner=user_id) | Q(public=True))


class ResourceListView(LoginRequiredMixin, ListView):
    model = Resource
    paginate_by = 15

    def get_queryset(self):
        """Verify user has access to resources."""
        user_id = self.request.user.pk
        return self.model.objects.select_related(
            'owner', 'language').prefetch_related('vocabulary').filter(
                Q(owner=user_id) | Q(public=True))
