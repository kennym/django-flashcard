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

def show_details_about(request, request_id, template_name='show_details.html'):
    """
    Show the details about a flashcard, given the ID.
    """
    queryset = get_object_or_404(FlashCard.objects.filter(id=request_id))
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
            queryset=FlashCard.objects.filter(front__startswith='0'))
        if formset.is_valid():
            formset.save()
    else:
        formset = FlashCardFormSet(
            queryset=FlashCard.objects.filter(front__startswith='0'))

    return_dict = {
        'formset': formset
    }

    return render_to_response(template_name, return_dict,
                             context_instance=RequestContext(request))

def edit_flashcard(request, flashcard_id, template_name='edit_flashcard.html'):
    """
    Edit a flashcard.
    """
    if request.method == "POST":
        # Save the changes
        pass
    else:
        pass

def delete_flashcard(request, flashcard_id,
                     template_name='delete_flashcard.html'):
    """
    Delete a flashcard given the `ID`.
    """
    FlashCard.objects.filter(id = flashcard_id).delete()
    return render_to_response(template_name)
