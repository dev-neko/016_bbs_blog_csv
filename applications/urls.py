from django.urls import path
from .views import (
	FileUploadView,# 追加
)
app_name = 'app_urls'
urlpatterns = [
	path('', FileUploadView.as_view(), name='index'),
]