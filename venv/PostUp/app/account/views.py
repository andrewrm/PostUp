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
#from account.forms import UserAccountCreateForm, ProfileImageUploadForm
from account.utils import auto_login_user, get_post_account
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
#from bet.forms import BetAccountCreateForm, BetUserLoginForm, BetAccountForm
#from bet.json import EncodeJSON
#from account.models import BetAccount
from django.forms.models import model_to_dict


def account(request, slug):
    print 'request Account %s ' % slug

    context = {'path':request.path}
    t = loader.get_template('account.html')
    c = RequestContext(request, context)
    return HttpResponse(t.render(c))
