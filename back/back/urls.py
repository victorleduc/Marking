
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login
from django.views.static import serve
from . import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'back.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    url(r'^marks/', include('marks.urls', namespace="marks")),
    url(r'^$', 'back.views.index'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),
    url(r'^accounts/logout/$', "back.views.logout_view")
)
