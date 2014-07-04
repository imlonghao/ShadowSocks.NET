from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('shadowsocks.web.views',
    # Examples:
    # url(r'^$', 'shadowsocks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'index'),
    url(r'^get$', 'get'),
    url(r'^share$', 'share'),
    url(r'^link$', 'link'),
    url(r'^code$', 'code'),
    url(r'^api$', 'api'),
    url(r'^email/(.+)$', 'email'),
)
