from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns("",
	url(r"^$", "lawdiff.views.index", name="home"),
	url(r'^admin/', include(admin.site.urls)),
	(r'^sentry/', include('sentry.web.urls')),
)
