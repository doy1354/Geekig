"""Accounting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# DJANGO IMPORTS
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from core.views import (
    SignupView, LoginView, EmailVerification, activate, test_email_view,
    update_session_language, IndexView, CustomPasswordResetView
)


urlpatterns = [
    # index url ---------------------------------------------------------------
    path('', IndexView.as_view(), name='index'),
    # prometheus url ----------------------------------------------------------
    path('', include('django_prometheus.urls')),

    # admin urls --------------------------------------------------------------
    path(f'{settings.ADMIN_URL}/', admin.site.urls),

    # Core urls ---------------------------------------------------------------
    path('core/', include('core.urls')),

    # Core urls ---------------------------------------------------------------
    path('price/', include('price.urls')),
    # API urls ----------------------------------------------------------------

    # auth urls ---------------------------------------------------------------
    path('signup/', SignupView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/verification/', EmailVerification.as_view(),
         name='email_verification'),
    path('auth/', include('django.contrib.auth.urls')),

    # ajax --------------------------------------------------------------------

    # all auth urls ------------------------------------------------
    path('', include('allauth.urls')),
    path('', include('allauth.socialaccount.urls')),

    # drf api auth ------------------------------------------------------------
    path('api-auth/', include('rest_framework.urls')),
    path('update-session-language/', update_session_language,
         name='update_session_language'),

    path('auth/password_reset/', CustomPasswordResetView.as_view(),
         name='password_reset'),
    path('auth/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('auth/reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('auth/reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    
    # allauth urls ------------------------------------------------------------
    path('test-email/', test_email_view),
]
# serve media files in development environment --------------------------------
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

# debug toolbar ---------------------------------------------------------------
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

# admin site customizations ---------------------------------------------------
admin.sites.AdminSite.site_header = "Accounting Administration"
admin.sites.AdminSite.site_title = "Accounting Administration"
admin.sites.AdminSite.index_title = "Accounting Admin Panel"
