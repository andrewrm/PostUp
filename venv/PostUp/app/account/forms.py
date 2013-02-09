#from account.models import UserAccount
from django import forms
from django.contrib.auth.models import User
from account.utils import create_user
from core.utils import generate_unique_slug
from account.models import PostAccount



class ProfileImageUploadForm(forms.Form):
    api_token = forms.CharField(max_length=100)
    slug = forms.SlugField(max_length=50)
#    file = forms.ImageField()


class UserAccountCreateForm(forms.ModelForm):
    pass

class PostAccountCreateForm(forms.ModelForm):
    email = forms.EmailField(max_length=256)
    username = forms.CharField(max_length=75)
    password = forms.CharField(widget=forms.PasswordInput())
#    password_confirm = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = PostAccount
        exclude = ('user', 'slug')


    def clean_email(self):
        data = self.cleaned_data.get('email','').strip()
        try:
            User.objects.get(email=data)
            raise forms.ValidationError(u'Email %s already exists, please choose another' % data )
        except User.DoesNotExist:
            return data
        
        
    def clean_username(self):
        data = self.cleaned_data.get('username','').strip()
        try:
            User.objects.get(username=data)
            raise forms.ValidationError(u'Userame %s already exists, please choose another' % data )
        except User.DoesNotExist:
            return data        

#    def clean(self):
#        data = self.cleaned_data.get('password','').strip()
#        data_confirm = self.cleaned_data.get('password_confirm','').strip()
#        
#        if data and data_confirm and data != data_confirm:
#            self._errors["password"] = self.error_class([u'Passwords do not match' ])
#        
#        return self.cleaned_data
    
    
    def save(self, commit=True):
        """
        - Extracts form data
        - Searches User database for user with same email
          - Found email, reuse the User object for new Role
          - Did not find email, create the User object for new Role 
        """
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        # Create user for new role
        user = create_user(email, username, password, is_active=True)
        user.save()
        print user
        
        # Create each role
        user_account = PostAccount.objects.create(
               user=user,
               slug=generate_unique_slug('account','PostAccount')
        )
        
        user_account.save()
        print user_account
        
        return user_account
    
    