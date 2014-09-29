from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from quiz.api import PersonAPI

router = routers.DefaultRouter(trailing_slash=False)
router.register('persons', PersonAPI)

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
)
