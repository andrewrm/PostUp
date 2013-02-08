from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.template import loader
from django.template.context import RequestContext
from django.core.context_processors import csrf

import mimetypes
from django.conf import settings
#from boto.s3.connection import S3Connection
#from boto.s3.key import Key



from core.utils import add_form_error, generate_slug
#from core.forms import UserLoginForm
from core.views import view_404, view_error
from account.forms import UserAccountCreateForm, ProfileImageUploadForm
from account.utils import auto_login_user, get_post_account
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from account.forms import PostAccountCreateForm
#from bet.forms import BetAccountCreateForm, BetUserLoginForm, BetAccountForm
from core.json import EncodeJSON
#from account.models import BetAccount
from django.forms.models import model_to_dict


def account(request, slug):
    print 'request Account %s ' % slug

    context = {'path':request.path}
    t = loader.get_template('account.html')
    c = RequestContext(request, context)
    return HttpResponse(t.render(c))


@csrf_exempt
def mobile_account_create(request):
    print 'Account create request'
    
    print request.POST
    
    if request.method == 'POST':
        form = PostAccountCreateForm(request.POST)
        if form.is_valid():
            print u'Account Form is valid'
            
            user_account = form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            if auto_login_user(request, username, password):
                
                response = EncodeJSON()
                response.add('user', user_account.to_dict())
                return HttpResponse(response.encode()) 
                
            else:
                view_error(request, u'There was an error in creating your account')
        else:
            print u'Account Form is invalid'
            response = EncodeJSON()
            response.add('errors', form.errors)
            return HttpResponse(response.encode()) 
    else:
        form = PostAccountCreateForm()
    
    
#    context = {'path':request.path, 'form':form}
#    t = loader.get_template('account-create.html')
#    c = RequestContext(request, context)
#    return HttpResponse(t.render(c))
    return HttpResponse()


def account_create(request):
    
    print 'Account create request'
    
    if request.method == 'POST':
        form = UserAccountCreateForm(request.POST)
        if form.is_valid():
            print u'Account Form is valid'
            
            user_account = form.save()
            
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            if auto_login_user(request, username, password):
                return redirect('account', user_account.slug)
            else:
                view_error(request, u'There was an error in creating your account')
        else:
            print u'Account Form is invalid'
    else:
        form = UserAccountCreateForm()
    
    
    context = {'path':request.path, 'form':form}
    t = loader.get_template('account-create.html')
    c = RequestContext(request, context)
    return HttpResponse(t.render(c))

