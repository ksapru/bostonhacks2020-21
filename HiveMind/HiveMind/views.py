from django.http import render
from django.views.generic.base import TemplateView 


def index(request):
    print(request.user)
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


class ProfileView(TemplateView):
    template_name = 'accounts.profile.html'
    
def vote(request, question_id):
    question = get_object_or_404(page, pk = page_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:

        selected_choice.save()
        
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
