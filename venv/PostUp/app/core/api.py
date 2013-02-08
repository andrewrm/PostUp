#PostUp API

from tastypie.resources import ModelResource
from account.models import PostAccount

class PostAccountResource(ModelResource):
    class Meta:
        queryset = PostAccount.objects.all()
        resource_name = 'postAccount'
