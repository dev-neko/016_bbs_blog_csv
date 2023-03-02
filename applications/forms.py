# from bootstrap4.widgets import RadioSelectButtonGroup
from django import forms

class FileUploadForm(forms.Form):
	file = forms.FileField(label='ファイル')
	# FileType = forms.ChoiceField(
	# 	help_text="Select file type.",
	# 	choices=(('csv', 'csv'), ('xlsx', 'xlsx')),
	# 	initial='csv',
	# 	required=True,
	# 	widget=RadioSelectButtonGroup,
	# )