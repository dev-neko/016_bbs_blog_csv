from django.urls import include,path
from django.contrib import admin
from django.conf.urls.static import static  # mediaを使うために追加
from . import settings  # mediaを使うために追加

urlpatterns = [
	# トップページへのURLルーティングをapplicationsフォルダ内のurls.pyへ回す
	path('',include('applications.urls')),
	# adminページ
	path('admin/', admin.site.urls,name='admin'),
	# ログイン関連ページ
	path('accounts/',include('django.contrib.auth.urls')),
]

# mediaを使うために追加
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)