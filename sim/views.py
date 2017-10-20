from django.shortcuts import render, redirect
from django.forms import formset_factory
from sim.forms import ValueForm, AddFileForm, ExecutableFileForm, ArgTemplateForm


def index(request):
    ValueFormSet = formset_factory(ValueForm, extra=1)
    FileFormSet = formset_factory(AddFileForm, extra=1)
    if request.method == 'POST':
        value_formset = ValueFormSet(request.POST, request.FILES, prefix='values')
        file_formset = FileFormSet(request.POST, request.FILES, prefix='files')
        exec_form = ExecutableFileForm(request.POST, request.FILES)
        argtemp_form = ArgTemplateForm(request.POST)
        # TODO Submit data and launch HTCondor
    else:
        value_formset = ValueFormSet(prefix='values')
        file_formset = FileFormSet(prefix='files')
        exec_form = ExecutableFileForm()
        argtemp_form = ArgTemplateForm()
    context = {'arg_forms': value_formset, 'file_forms': file_formset, 'exec_form' : exec_form, 'argtemp_form' : argtemp_form}
    return render(request, 'sim/index.html', context)
