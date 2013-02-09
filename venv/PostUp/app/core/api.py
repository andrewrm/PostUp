##PostUp API
#
#from tastypie.resources import ModelResource
#from tastypie.serializers import Serializer
#
#from account.models import PostAccount
#from post.models import GeoPost
#from django.forms.models import model_to_dict
#from tastypie.models import create_api_key
#from django.contrib.auth.models import User
#from tastypie.constants import ALL
#
#
#
#class PostAccountResource(ModelResource):
#    class Meta:
#        queryset = PostAccount.objects.all()
#        serializer = Serializer(formats=['json'])
#        resource_name = 'postAccount'
#        filtering = {
#                     'userid': ALL
#                     'query': ['icontains',],
#                     }
#        
#        def apply_filters(self, request, applicable_filters):
#            base_object_list = super(PostAccountResource, self).apply_filters(request, applicable_filters)
#            query  = request.META.get('HTTP_AUTHORIZATION')
#            if query:
#                qset = Q(api_key=query)
#                base_object_list = base_object_list.filter(qset).distinct()
#
#            return base_object_list
#        
#        def get_object_list(self, request):
#            return super(PostAccountResource, self).get_object_list(request).filter(slug = request.slug)
#
#    
#    def alter_list_data_to_serialize(self, request, data):
#        """
#        A hook to alter list data just before it gets serialized & sent to the user.
#    
#        Useful for restructuring/renaming aspects of the what's going to be
#        sent.
#    
#        Should accommodate for a list of objects, generally also including
#        meta data.
#        """
#        
#        response = []
#        for element in data[ 'objects' ]:
#            print type(element), type(element.obj)
#            response.append(model_to_dict(element.obj))
#        
#        return { 'objects' : response}
#    
#    
#class GeoPostResource(ModelResource):
#    class Meta:
#        queryset = GeoPost.objects.all()
#        serializer = Serializer(formats=['json'])
#
#        resource_name ='geoPost'
#        
#            
#    def alter_list_data_to_serialize(self, request, data):
#        
#        response = []
#        for element in data[ 'objects' ]:
#            print type(element), type(element.obj)
#            response.append(model_to_dict(element.obj))
#        
#        return { 'objects' : response}