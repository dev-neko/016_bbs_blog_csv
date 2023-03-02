import io
from pprint import pprint

import openpyxl as openpyxl
import xlrd
import xlwings as xlwings
from django.shortcuts import redirect
from django.views.generic import FormView,ListView,UpdateView
from .forms import FileUploadForm
import pandas as pd
from django.urls import reverse_lazy
from django.http import HttpResponse
from io import BytesIO

from .models import CompanyModel



class FileUploadView(FormView):
	template_name='applications/index.html'
	form_class=FileUploadForm
	success_url=reverse_lazy('index')
	# context_object_name='ctx'
	# model=CompanyModel

	def form_valid(self,form):
		# フォームから受け取ったデータをデータフレームへ変換
		# ファイル形式に応じた読み込み
		# file=io.TextIOWrapper(form.cleaned_data['file'],encoding='cp932')
		# print(file.encoding)

		# def get_context_data(self,**kwargs):
		# 	ctx=super().get_context_data(**kwargs)
		# 	# excel=self.request.FILES['file']
		# 	return ctx,self.header_cells

		# df=pd.read_excel(file,dtype=str,index_col=0)
		# print(df)

		# with open(file,encoding='cp932') as file:
		# 	data = file.read()

		# wb = xlrd.open_workbook(file, encoding_override='cp932')
		# df = pd.read_excel(wb)
		# print(df)

		# wb=xlwings.Book(df)
		# data_sheet=wb.sheets['Sheet1']
		# test_data=data_sheet.range(1,11).expand('down').value
		# print(test_data)

		# if filetype == 'csv':
		# 	df = pd.read_csv(file, dtype=str)
		# elif filetype == 'xlsx':
		# 	df = pd.read_excel(file, dtype=str, index_col=0)

		excel=self.request.FILES['file']
		# print(excel.read())

		wb=openpyxl.load_workbook(excel)
		ws=wb['Sheet1']
		# print(ws.cell(4,11).value)

		# １行目（列名のセル）
		header_cells = ws[3]
		# print(header_cells[10].value)

		# ２行目以降（データ）
		company_list = []
		for row in ws.iter_rows(min_row=4):
			row_dic = {}
			# セルの値を「key-value」で登録
			for k, v in zip(header_cells, row):
				if k.value!=None:
					row_dic[k.value] = v.value
			company_list.append(row_dic)

		# pprint(student_list)

		# DBに保存
		CompanyModel.objects.update_or_create(defaults={'information':company_list})

		return redirect('app_urls:index')


	# def get_object(self,queryset=None):
	# 	ctx['company_list']=CompanyModel.objects.all()
	# 	print(ctx)
	# 	return ctx

	def get_context_data(self,**kwargs):
		ctx=super().get_context_data(**kwargs)
		company_model_obj=CompanyModel.objects.all()
		ctx['company_list']=eval(company_model_obj[0].information)
		ctx['title_list']=['企業名', 'HP', '業界', '住所', '従業員数', '設立年月', '上場区分', '総合評価', 'A.事業戦略', 'B.経営手腕', 'C.職場環境', 'D.仕事の意義', 'E.教育・成長', 'F.給与・処遇', 'G.生活しやすさ']
		return ctx


