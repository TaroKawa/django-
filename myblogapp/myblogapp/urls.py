"""myblogapp URL Configuration

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
#from django.conf.urls import url

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from posts import views

urlpatterns = [
    url(r'^posts/',include('posts.urls')),
    #url(r'^',include('posts.urls')),
    url(r'^admin/', admin.site.urls),
    # 正規表現、表示するページ
    #url(r'^posts/(?P<post_id>[0-9]+)/$',views.post_detail),
    url(r'^posts/(?P<post_id>[0-9]+)/$',views.post_detail,name='post_detail'),
    # django特有の表現で、(?P<変数名>[変数の範囲]+(複数って意味）)/$
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
