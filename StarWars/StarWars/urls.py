from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

import mainapp.urls as mainapp
from mainapp.endpoints.api_recruit import RecruitViewSet, PlanetViewSet, SithViewSet

schema_view = get_schema_view(title='Pastebin API')

router = DefaultRouter()
router.register('recruits', RecruitViewSet)
router.register('planets', PlanetViewSet)
router.register('siths', SithViewSet)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include(mainapp)),
                  path('api/', include(router.urls)),
                  path('schema/', schema_view),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
