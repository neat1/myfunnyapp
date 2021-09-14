from django.shortcuts import render
from .models import *
    

def home(request):
    # Take randomly a word or sentence from the sqlite database
	context = {'target':Target.objects.order_by('?').first(),
                'issue': Issue.objects.order_by('?').first(),
                'start':Start.objects.order_by('?').first(),
                # I remove the articles before the targets to use it in different sentence
                'issue_without_article':str(Issue.objects.order_by('?').first()).replace("a ", "",).replace("an ", "",)}

	return render(request, 'sentence_generator/index.html', context)