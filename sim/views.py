from django.shortcuts import render, redirect
from django.forms import formset_factory
from sim.forms import ValueForm, AddFileForm

def index(request):
    ValueFormSet = formset_factory(ValueForm)
    FileFormSet = formset_factory(AddFileForm)
    if request.method == 'POST':
        value_formset = ValueFormSet(request.POST, request.FILES, prefix='values')
        file_formset = FileFormSet(request.POST, request.FILES, prefix='files')
        # TODO Submit data and launch HTCondor
    else:
        value_formset = ValueFormSet(prefix='values')
        file_formset = FileFormSet(prefix='files')
    context = {'arg_forms': value_formset, 'file_forms': file_formset}
    return render(request, 'sim/index.html', context)
