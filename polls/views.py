import random
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Questions


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		
		# Return the last five published questions (not including those set to be published in the future).

		# return Questions.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]
		rques=Questions.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:20]
		return random.sample(list(rques),10)


class QuestionDetailView(generic.DetailView):
	model = Questions
	template_name = 'polls/detail.html'
	def get_queryset(self):

        # Excludes any questions that aren't published yet.

		return Questions.objects.filter(pub_date__lte=timezone.now())

	


class ResultsView(generic.DetailView):
	model = Questions
	template_name = 'polls/results.html'

	def get_queryset(self):
		
		# Excludes any questions that aren't published yet.

		return Questions.objects.filter(pub_date__lte=timezone.now())
	


def vote(request,question_id):
	question=get_object_or_404(Questions,pk=question_id)
	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])
		# print(selected_choice)
		
	except(KeyError,Choice.DoesNotExist):
		return render(request,'polls/detail.html',{'question':question,'error_message':"You didn't select a choice.",})
	else:
		selected_choice.votes+=1
		selected_choice.save()
		# print(selected_choice)
		return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

