from django.conf.urls.defaults import *

from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^dj/', include('dj.foo.urls')),
    (r'^flashcards/', include('flashcard.urls')),
    (r'^practice/', include('flashcard.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': 'media'}),
    )
