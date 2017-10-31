from django.shortcuts import render
from django.forms import formset_factory
from plots.forms import AddFileForm, ValueForm

def index(request):
	ValueFormSet = formset_factory(ValueForm, extra=1)
	if request.method == 'POST':
		value_formset = ValueFormSet(request.POST, request.FILES, prefix='values')
	else:
		value_formset = ValueFormSet(prefix='values')
	context={'value_forms':value_formset}
	return render(request, 'plots/index.html', context)