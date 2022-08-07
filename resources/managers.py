from django.db import models


class ResourceManager(models.Manager):
    """ Custom queryset manager for resources """
    def manager_only_method(self):
        print(self)
