from django import forms

class ValueForm(forms.Form):
	SPECNAME_TYPE_CHOICE_TEST = (
		('1', 'Specification 1'),
		('2', 'Specification 2'),
		('3', 'Specification 3'),
		('4', 'Specification 4'),	
	)
	name = forms.ChoiceField(label="Name of experiment (specification)", choices=SPECNAME_TYPE_CHOICE_TEST)
	X = forms.CharField(label="X", max_length=10)
	Y = forms.CharField(label='Y', max_length=10)
	L = forms.CharField(label="L(curve)", max_length=10)

class CurvesForm(forms.Form):
	AAAAAAAAA=()

class AddFileForm(forms.Form):
	file = forms.FileField(label="Upload file")
	name = forms.CharField(label="UInlude in the args as", max_length=50, required=False)

