from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
from django.http import HttpResponseRedirect

from Lisculea import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
#    (r'^accounts/', include('registration.urls')),
   
    (r'^$', lambda x: HttpResponseRedirect("/cafe")), # for now cafe is considered as main app
    (r'^general/', include("Lisculea.General.urls")),    
    (r'^grades/', include("Lisculea.Grades.urls")),   
    (r'^loadGK$', "Lisculea.loadGK.views.upload_files"),
    (r'^cafe/', include("Lisculea.Cafe.urls")),
    (r'^fileShare/', include("Lisculea.FileShare.urls")),
    (r'^luncher/', include("Lisculea.Luncher.urls")),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
