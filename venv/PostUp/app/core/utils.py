import random

from django.forms.forms import NON_FIELD_ERRORS
from django.forms.util import ErrorDict
from django.shortcuts import _get_queryset
from django.http import Http404
from django.db.models.loading import get_model
import string




def add_form_error(form, message):
    if not form._errors:
        form._errors = ErrorDict()
    if not NON_FIELD_ERRORS in form._errors:
        form._errors[NON_FIELD_ERRORS] = form.error_class()
    form._errors[NON_FIELD_ERRORS].append(message)
    
         
            
def generate_slug(length=10, *args, **kwargs):
    return ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWYXZ') for i in range(length))
    
def token_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))         
      
def generate_unique_slug(app, klass, length=16):
    
    model = get_model(app, klass)
    #model = _get_queryset(klass)
    print model, app, klass
    
    while True:
        # Generate new slug
        slug = generate_slug(16)
        try:
            model.objects.get(slug=slug)
        except model.DoesNotExist:
            # Return unique slug
            return slug
    
                
                
                
                
                        
            
def get_object_or_None(klass, *args, **kwargs):
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        return None
    
    
    
