from django.urls import path
from .views import (
	FileUploadView,Sample01,  # 追加
)
app_name = 'app_urls'
urlpatterns = [
	path('', FileUploadView.as_view(), name='index'),
	path('sample01',Sample01.as_view(),name='Sample01'),
]