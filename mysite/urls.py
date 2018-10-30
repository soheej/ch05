"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import HomeView

# from bookmark.views import BookmarkLV, BookmarkDV # 이 부분은 bookmark.urls 부분으로 옮겼음

urlpatterns = [
    # ch02 완성본의 모습인데, bookmark.urls로 옮겼으므로 주석 처리함
    # url(r'^admin/', admin.site.urls),
    # # url(regex, view, kwargs=None, name=None, prefix='')
    # # 여기서 regex와 view는 필수 인자)
    # url(r'', include('bookmark.urls')),
    # # 아래 내용을 모두 bookmark/urls.py 파일로 옮기자.
    # # # 북마크 앱을 위한 클래스 기반 뷰
    # # # /bookmark/ 요청을 처리할 뷰 클래스를 BookmarkLV로 지정하고, URL 패턴 이름 지정
    # # url(r'^bookmark/$', BookmarkLV.as_view(), name='index'),
    # # # /bookmark/숫자/ 요청을 처리할 뷰 클래스를 BookmarkDV로 지정하고, URL 패턴 이름 지정
    # # url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
    # # # tabular list
    # # url(r'^bookmark_t/$', bookmark.views.tabularBookmark, name='index_t'),

    url(r'^admin/', include(admin.site.urls)),
    # admin.site.urls를 include(admin.site.urls)로 변경했으나 사실 동일한 효과를 발휘
    # 다른 앱에서 정의된 url 설정을 재활용할 때 include() 함수를 써야 하지만,
    # 예외적으로 admin.site.urls에 대해서는 include() 함수를 생략해도 무방함

    # 아래 두 url 패턴에서 뒷 부분에 패턴의 끝을 표시하는 '$' 문자가 없음!!!
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    # bookmark.urls를 적용하고, 이름공간을 'bookmark'로 지정
    url(r'^blog/', include('blog.urls', namespace='blog')),
    # blog.urls를 적용하고, 이름공간을 'blog'로 지정
]