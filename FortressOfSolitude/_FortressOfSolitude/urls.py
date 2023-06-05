"""
DBA 1337_TECH, AUSTIN TEXAS © MAY 2021
Proof of Concept code, No liabilities or warranties expressed or implied.
"""
from django.contrib import admin
from django.urls import path

"""
_FortressOfSolitude URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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

# Uncomment next two lines to enable admin:
from django.conf.urls import include, url
from django.conf.urls.static import static
from _FortressOfSolitude.Blog import urls as blog_urls
from _FortressOfSolitude.Blog.views import PostList
from _FortressOfSolitude.organizer import urls as organizer_urls
from _FortressOfSolitude.superhero import urls as superhero_urls
from _FortressOfSolitude.superhero.views import my_403_forbidden_view, my_500_error_view
from . import settings

# from FortressOfSolitude._FortressOfSolitude.superhero.views import my_500_error_view

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    url(r'^', include(organizer_urls)),
    url(r'^$', PostList.as_view()),
    url(r'^superhero/', include((superhero_urls, 'superhero'), namespace='dj-auth')),
    url(r'^blog/', include(blog_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler500 = my_500_error_view
handler403 = my_403_forbidden_view
