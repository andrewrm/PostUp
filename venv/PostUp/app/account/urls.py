from django.conf.urls import patterns, include, url


urlpatterns = patterns('account.views',
    # Examples:
    # url(r'^$', 'argos.views.home', name='home'),

    url(r'^mobile/createAccount/?$', 'mobileCreateAccount', name='mobileCreateAccount'),

)