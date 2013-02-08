from django.db import models
from django.contrib.auth.models import User, UserManager
from core.utils import generate_slug
from tastypie.models import create_api_key

class UserProfile(models.Model):
    slug = models.SlugField(max_length=30, default=generate_slug)
    user = models.OneToOneField(User)
    objects = UserManager()
    
    class Meta:
        abstract = True
    
    def __unicode__(self):
        return u'%s' % str(self.user)


