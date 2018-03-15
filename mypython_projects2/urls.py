"""mypython_projects2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include ('apps.app1_landingpage.urls', namespace='app1')),
    url(r'^bright_ideas1/', include ('apps.bright_ideas1.urls', namespace='bright_ideas1')),
    url(r'^bright_ideas2/', include ('apps.bright_ideas2.urls', namespace='bright_ideas2')),
    url(r'^network1/', include ('apps.network1.urls', namespace='network1')),
    url(r'^network2/', include ('apps.network2.urls', namespace='network2')),
    url(r'^playlist1/', include ('apps.playlist1.urls', namespace='playlist1')),
    url(r'^playlist2/', include ('apps.playlist2.urls', namespace='playlist2')),
    url(r'^admin/', admin.site.urls),
]
