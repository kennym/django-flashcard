from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

from dvoc.models import FlashCard, FlashCardForm


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
        'object_detail': queryset,
        'object_id': request_id
    }

    return render_to_response(template_name, return_dict)

@csrf_protect
def create_flashcard(request, template_name='create_flashcard.html'):
    """
    Return a form for creating a flashcard.
    """
    if request.method == "POST":
        formset = FlashCardForm(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect(to='list_flashcards')
    else:
        formset = FlashCardForm()

    return_dict = {
        'formset': formset
    }

    return render_to_response(template_name, return_dict,
                             context_instance=RequestContext(request))

@csrf_protect
def edit_flashcard(request, flashcard_id, template_name='edit_flashcard.html'):
    """
    Edit a flashcard.
    """
    flashcard = get_object_or_404(FlashCard, pk=flashcard_id)
    if request.method == "POST":
        form = FlashCardForm(instance=flashcard, data=request.POST)
        if form.is_valid():
            flashcard = form.save()
            return HttpResponseRedirect(flashcard.get_absolute_url())
    else:
        form = FlashCardForm(instance=flashcard)

    return_dict = {
        'form': form
    }
    return render_to_response(template_name, return_dict,
                             context_instance=RequestContext(request))

def delete_flashcard(request, flashcard_id):
    """
    Delete a flashcard given the `ID`.
    """
    FlashCard.objects.filter(id = flashcard_id).delete()
    return redirect('list_flashcards') # Redirect to the flashcard list
