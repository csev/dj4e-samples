from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomeView.as_view() ),
    # Uncomment this below if you have setup base_bootstrap.html and configured social login
    # path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login)),
]

# The obtuse code below can be ignored - It dynamically switches
# between non-social login.html and social_login.html when we notice
# that social login has been configured in settings.py (later in the course)
# Or just uncomment the path above when you enable social login

from django.conf import settings
try:
    if len(settings.SOCIAL_AUTH_GITHUB_KEY) > 0 :
        social_login = 'registration/login_social.html'
        urlpatterns += [
            path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login)),
        ]
        print('Using',social_login,'as the login template for',settings.LOGIN_URL)
except:
    print('Using registration/login.html as the login template for',settings.LOGIN_URL)

