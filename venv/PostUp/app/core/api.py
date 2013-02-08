#PostUp API

from tastypie.resources import ModelResource
from tastypie.serializers import Serializer

from account.models import PostAccount
from post.models import GeoPost
from django.forms.models import model_to_dict


class PostAccountResource(ModelResource):
    class Meta:
        queryset = PostAccount.objects.all()
        serializer = Serializer(formats=['json'])
        resource_name = 'postAccount'
    
    def alter_list_data_to_serialize(self, request, data):
        """
        A hook to alter list data just before it gets serialized & sent to the user.
    
        Useful for restructuring/renaming aspects of the what's going to be
        sent.
    
        Should accommodate for a list of objects, generally also including
        meta data.
        """
        
        response = []
        for element in data[ 'objects' ]:
            print type(element), type(element.obj)
            response.append(model_to_dict(element.obj))
        
        return { 'objects' : response}
    
    
class GeoPostResource(ModelResource):
    class Meta:
        queryset = GeoPost.objects.all()
        serializer = Serializer(formats=['json'])

        resource_name ='geoPost'
        
            
    def alter_list_data_to_serialize(self, request, data):
        
        response = []
        for element in data[ 'objects' ]:
            print type(element), type(element.obj)
            response.append(model_to_dict(element.obj))
        
        return { 'objects' : response}