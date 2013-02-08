from django.db import models
from core.models import UserProfile
from core.utils import generate_slug
from django.contrib.auth.models import User

# Create your models here.

class GeoPost(models.Model):

    slug = models.SlugField(default=generate_slug)
    text = models.CharField(max_length = 200)
    created = models.DateTimeField('Date published')
    creator = models.ForeignKey(User)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    def to_dict(self):
        store = {}

        store['id'] = self.id
        store['created'] = self.created.strftime('%Y-%m-%dT%H:%M:%S-000')
        store['creator'] = self.creator.username
        store['text'] = self.text
        store['latitude'] = self.latitude
        store['longitude'] = self.longitude
        return store


    def __unicode__(self):
        return u"$s $s" % (self.text, self.user.username)

