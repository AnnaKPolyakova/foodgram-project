from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

from recipes.views import page_not_found, server_error

handler404 = "recipes.views.page_not_found"
handler500 = "recipes.views.server_error"

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),
    path(
        'about-author/',
        views.flatpage,
        {'url': '/about-author/'},
        name='about-author'
    ),
    path(
        'about-spec/',
        views.flatpage,
        {'url': '/about-spec/'},
        name='about-spec'
    ),
    path('', include('api.urls')),
    path('', include('recipes.urls')),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('404/', page_not_found, name='Error_404'),
    path('500/', server_error, name='Error_500'),

]

urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
    path(
        'api/schema/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
