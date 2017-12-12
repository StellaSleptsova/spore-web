from django.shortcuts import render, render_to_response
from django.forms import formset_factory
from plots.forms import AddFileForm, VariableValueForm
from django.contrib import messages
import random
import datetime
import time
from logs.parser import parse
from django.http import HttpResponseRedirect

def getData(strYorX, containerValue, strX1, strX2):
	if strYorX == 'spec' and con:
		return containerValue.spec
	elif strYorX == 'snr':
		return containerValue.snr 
	elif strYorX == 'schedule':
		return containerValue.schedule
	elif strYorX == 'n':
		return containerValue.n
	elif strYorX == 'k':
		return containerValue.k
	elif strYorX == 'r':
		return containerValue.r
	elif strYorX == 'stddev':
		return containerValue.stddev
	elif strYorX == 'fer':
		return containerValue.fer
	return "null"

def index(request):	
	context = {}
	formset = formset_factory(VariableValueForm, extra=1)
	#formset = formset_factory(VariableValueForm, extra=1)
	'''data = {
		'form-TOTAL_FORMS': u'1',
		'form-INITIAL_FORMS': u'0',
		'form-MAX_NUM_FORMS': u'',
	}
	formset = formset(data)'''
	if request.method=='POST':
		myform=formset(request.POST,prefix='values')
	#	form=VariableValueForm(request.POST)

		print(myform.is_valid())
		if not myform.is_valid():
		#save_it= form.save(commit=False)
		#save_it.save()
			messages.success(request,'Y, X2, X3, X4 not must be equal')
		else:
			'''
			strY = form.getY()
			strX1 = form.getX1()
			strX2 = int(form.getX1())
			strX3 = form.getX1()'''
			form = myform
			for oneform in myform:
				form = oneform
			strX2 = int(form.getX2()) #int(form.Cleaned_data['X2'])
			strX3 = form.getX3() #str(form.Cleaned_data['X3'])
			print("AAAAAAAAAAAAAAAAAAAAa")
			print(strX2)
			print(strX3)

			storage = messages.get_messages(request)	
			storage.used = True

			points = {}
			points.update(parse("results.txt"))
			xdata = [value.snr for key, value in points.items() if value.n == strX2 if value.spec == strX3]
			ydata = [value.fer for key, value in points.items() if value.n == strX2 if value.spec == strX3 ]
			print(xdata)
			print(ydata)
			kwargs1 = {'shape': 'circle'}
			extra_serie1 = {"tooltip": {"y_start": "", "y_end": " balls"}}
			chartdata = {
				'x': xdata,
				'name1': 'series 1', 'y1': ydata, 'kwargs1': kwargs1, 'extra1': extra_serie1,
			}
			charttype = "scatterChart"
			context.update({
				'charttype': charttype,
				'chartdata': chartdata,
				'extra': {
            		'x_is_date': True,
            		'x_axis_format': '%d-%b',
            		'tag_script_js': True,
            		'jquery_on_ready': True,
        		},
			})
			'''
			nb_element = 50
			xdata = [i + random.randint(1, 10) for i in range(nb_element)]
			ydata1 = [i * random.randint(1, 10) for i in range(nb_element)]
			ydata2 = map(lambda x: x * 2, ydata1)
			ydata3 = map(lambda x: x * 5, ydata1)

			kwargs1 = {'shape': 'circle'}
			kwargs2 = {'shape': 'cross'}
			kwargs3 = {'shape': 'triangle-up'}

			extra_serie1 = {"tooltip": {"y_start": "", "y_end": " balls"}}

			chartdata = {
				'x': xdata,
				'name1': 'series 1', 'y1': ydata1, 'kwargs1': kwargs1, 'extra1': extra_serie1,
				'name2': 'series 2', 'y2': ydata2, 'kwargs2': kwargs2, 'extra2': extra_serie1,
				'name3': 'series 3', 'y3': ydata3, 'kwargs3': kwargs3, 'extra3': extra_serie1
			}
			charttype = "scatterChart"
			context.update({
				'charttype': charttype,
				'chartdata': chartdata,
				'extra': {
            		'x_is_date': True,
            		'x_axis_format': '%d-%b',
            		'tag_script_js': True,
            		'jquery_on_ready': True,
        		},
			})
			'''
	else:
		'''
		data = {
			'form-TOTAL_FORMS': u'3',
			'form-INITIAL_FORMS': u'0',
			'form-MAX_NUM_FORMS': u'',
		}'''	
		form = formset(prefix='values')
	context.update({'variableValue_forms':form})
	return render(request, 'plots/index.html', context)
	#return HttpResponseRedirect('/plots')
	'''
	VariableValueFormSet = formset_factory(VariableValueForm, extra=1)
	if request.method == 'POST':
		#if request.POST.get('plot'):
		variableValue_form= VariableValueForm(request.POST)
		save_it = variableValue_form(commit=False)
		save_it.save()
		#if not variableValue_form.is_valid():
		messages.success(request,"Error")
		return render_to_response('plots/index.html', locals(), context_instance=Request.Context(request))
	else:
		variableValue_formset = VariableValueFormSet(prefix='values')
		context={'variableValue_forms':variableValue_formset}
		return render(request, 'plots/index.html', context)
	'''