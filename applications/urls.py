from django.urls import path
from .views import (
	FileUploadView,
	Sample01,
	v1,
	SearchFormView,
	axios_form,
)
from . import views
from .views import *

app_name = 'app_urls'

urlpatterns = [
	path('', FileUploadView.as_view(), name='index'),
	path('sample01/',Sample01.as_view(),name='Sample01'),
	# path('v1/',v1.as_view(),name='v1'),
	path('v1/',SearchFormView.as_view(),name='v1'),
	# axios
	path('axios_form/',views.axios_form,name='axios_form'),
]