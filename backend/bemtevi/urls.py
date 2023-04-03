from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from posts.views import ArtView, HighlightsView

import django_js_reverse.views
from rest_framework.routers import DefaultRouter

from common.routes import routes as common_routes
from posts.views import *
from rest_framework import routers
from users.views import Profileview

router = routers.DefaultRouter()
print(dir(router))
router.register(r'comment', Commentspageapi,  basename ='comment')

# routes = common_routes
# for route in routes:
#     router.register(route['regex'], route['viewset'], basename=route['basename'])
#     print(route)



print(router.urls)



urlpatterns = [
    path("", include("common.urls"), name="common"),
    path("admin/", admin.site.urls, name="admin"),
    path("jsreverse/", django_js_reverse.views.urls_js, name="js_reverse"),

    path("api/", include((router.urls, 'posts'), namespace="api")),

    path("accounts/", include("allauth.urls")),
    path("accounts/", include("users.urls")),
    path("home/", ArtView.as_view(), name='artview'),
    # path('search/<str:term>/', search_view, name='search')
    path("api/highlights/", HighlightsView.as_view(), name='hgs' ),
    path("api/post/", Api_post.as_view(), name='posts'),
    path("api/post/<int:pk>/likes/", API_likes, name='likes'),
    path("api/post/<int:pk>/like/", like_api.as_view(), name='like'),
    path('teste/', Profileview.as_view())
]

