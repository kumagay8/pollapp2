from django import forms
from .models import Guest
from django.core.exceptions import ValidationError

class GuestsForm(forms.ModelForm):
	class Meta:
		model = Guest
		fields = ('name','furi','email','memo')
		widgets ={
			'name':forms.TextInput(attrs={'size':30}),
			'furi':forms.TextInput(attrs={'size':30}),
			'email':forms.EmailInput(attrs={'size':40}),
			'memo':forms.Textarea(attrs={'cols':40, 'rows':2}),
		}
		requireds = {
			'name': True ,
			'furi': True ,
			'email': True ,
			'memo': None,
					}
		# requiredsはTrueかNone/’’を必ず入れる

#	guest =forms.EmailField(
#		label = 'email',
#		widget = forms.EmailInput(attrs={'size':50}),	#EmailInput:EmailFieldのデフォルトのウィジェット
#		required =  True,
#		)

#	class Meta:
#		model = Guest
#		fields = ("name","furi","email","memo")
#		widgets = {
#					'name':forms.TextInput(attrs={'size':30}),
#					'furi':forms.TextInput(attrs={'size':30}),
#					'email':forms.EmailInput(attrs={'size':50}),	#EmailInput:EmailFieldのデフォルトのウィジェット
#					'memo':forms.Textarea(attrs={'rows':4, 'cols':50}),
#					}
					





