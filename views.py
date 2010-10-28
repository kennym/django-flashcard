from django.shortcuts import get_object_or_404, render_to_response
from django.forms.models import modelformset_factory
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

from dvoc.models import FlashCard


def list_flashcards(request, template_name='list_flashcards.html'):
    """
    Return a list with flash cards.
    """
    flashcard_list = FlashCard.objects.all()
    return_dict = {
        'flashcard_list': flashcard_list
    }

    return render_to_response(template_name, return_dict)

def show_details_about(request, response_id, template_name='show_details.html'):
    """
    """
    queryset = get_object_or_404(FlashCard.objects.filter(id=response_id))
    return_dict = {
        'object_detail': queryset
    }

    return render_to_response(template_name, return_dict)

@csrf_protect
def create_flashcard(request, template_name='create_flashcard.html'):
    """
    Return a form for creating a flashcard.
    """
    FlashCardFormSet = modelformset_factory(FlashCard)
    if request.method == "POST":
        formset = FlashCardFormSet(
            request.POST, request.FILES,
            queryset=FlashCard.objects.filter(front_view__startswith='0'))
        if formset.is_valid():
            formset.save()
    else:
        formset = FlashCardFormSet(
            queryset=FlashCard.objects.filter(front_view__startswith='0'))

    return_dict = {
        'formset': formset
    }

    return render_to_response(template_name,  return_dict,
                             context_instance=RequestContext(request))
