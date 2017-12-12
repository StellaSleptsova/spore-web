from django import forms
from logs.parser import parse

class VariableValueForm(forms.Form):
	VARIABLE_TYPE_CHOICE_TEST = (
		('1', 'N'),
		('2', 'K'),
		('3', 'Spec'),
		('4', 'L'),	
		('5', 'FER'),
		('6','BER'),
		('7', 'NEMP'),
	)
	EXPERIMENT_TYPE_CHOICE_TEST = (
		('1', 'Experiment 1'),
		('2', 'Experiment 2'),
		('3', 'Experiment 3'),
	)
	VARIABLE_TYPE_CHOICE_N = [
		(1, 1024), 
		(2, 1056), 
		(3, 1088),
	]
	VARIABLE_TYPE_CHOICE_SPEC = [
		(1, 'R_0.17_N_1024_K_171.xpec'), 
		(2, 'R_0.17_N_1056_K_176.xpec'), 
		(3, 'R_0.17_N_1088_K_182.xpec'),
	]
	experiment = forms.ChoiceField(label="Name of experiment", choices=EXPERIMENT_TYPE_CHOICE_TEST)
	Y = forms.ChoiceField(label="Y", choices= VARIABLE_TYPE_CHOICE_TEST)
	X1 = forms.ChoiceField(label='X1', choices=VARIABLE_TYPE_CHOICE_TEST)
	X2 = forms.ChoiceField(label="X2", choices=VARIABLE_TYPE_CHOICE_N)
	X3 = forms.ChoiceField(label="X3", choices=VARIABLE_TYPE_CHOICE_SPEC)
	isUpdated = False
	
	def __init__(self, *args,**kwargs):
		super(VariableValueForm, self).__init__(*args, **kwargs)
		#self.updateVariableData()
		for key in self.fields:
			self.fields[key].required = False 

	def is_valid(self):
		valid = super(VariableValueForm, self).is_valid()

		print(str(self.cleaned_data['X1']))
		if not valid:
			return valid
		return True

		if (self.cleaned_data['Y'] == self.cleaned_data['X1'] or
				self.cleaned_data['Y'] == self.cleaned_data['X2'] or
				self.cleaned_data['Y'] == self.cleaned_data['X3']):
				return False
		elif (self.cleaned_data['X1'] == self.cleaned_data['X2'] or
				self.cleaned_data['X1'] == self.cleaned_data['X3']):
				return False
		elif self.cleaned_data['X2'] == self.cleaned_data['X3']:
			return False
		return True

	def getY(self):
		self.is_valid()
		print(self.cleaned_data['Y'])
		return str(self.cleaned_data['Y'])

	def getX1(self):
		self.is_valid()
		return str(self.cleaned_data['X1'])

	def getX2(self):
		print("LOG: getX2")
		dic = dict(self.fields['X2'].choices)
		print(dic)
		for key, value in dic.items():
			print(value)
		datax2 = int(self.cleaned_data['X2'])
		print(dic[datax2])
		return int(dic[datax2])

	def getX3(self):
		self.is_valid()
		dicr = dict(self.fields['X3'].choices)
		for key, value in dicr.items():
			print(value)
		datax3 = int(self.cleaned_data['X3'])
		print(str(dicr[datax3]))
		return str(dicr[datax3])

	def updateVariableData(self):
		if not self.isUpdated:		
			points = {}
			points.update(parse("results.txt"))

			variableFER = list(set([value.fer for key, value in points.items()]))
			variableFERnum = [i for i in range(1,len(variableFER))]

			variableK = list(set([value.k for key, value in points.items()]))
			variableKnum = [i for i in range(1,len(variableK))]

			variableN = list(set([value.n for key, value in points.items()]))
			variableNnum =  [i for i in range(1,len(variableN))]

			variableSPEC = list(set([value.spec for key, value in points.items()]))
			variableSPECnum = [i for i in range(1,len(variableSPEC))]

			tupleY = tuple(zip(variableFERnum,variableFER))
			tupleX1 = tuple(zip(variableKnum,variableK))
			tupleX2 = tuple(zip(variableNnum, variableN))
			tupleX3 = tuple(zip(variableSPECnum,variableSPEC))

			#self.Y = forms.ChoiceField(label="Y ", choices=tupleY)
			#self.X1 = forms.ChoiceField(label='X1', choices=tupleX1)
			self.X2 = forms.ChoiceField(label="X2", choices=tupleX2)
			self.X3 = forms.ChoiceField(label="X3", choices=tupleX3)
			#print(tupleX2)
			#print(tupleX3)
			self.isUpdated = True


class AddFileForm(forms.Form):
	file = forms.FileField(label="Upload file")
	name = forms.CharField(label="UInlude in the args as", max_length=50, required=False)