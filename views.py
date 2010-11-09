from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

from dvoc.forms import RatingForm
from dvoc.models import FlashCard, FlashCardForm

@login_required
def list_flashcards(request, template_name='list_flashcards.html'):
    """
    Return a list with flash cards.
    """
    flashcard_list = FlashCard.objects.filter(user=request.user)
    return_dict = {
        'flashcard_list': flashcard_list
    }

    return render_to_response(template_name, return_dict)

@login_required
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

@login_required
@csrf_protect
def create_flashcard(request, template_name='create_flashcard.html'):
    """
    Return a form for creating a flashcard.
    """
    if request.method == "POST":
        formset = FlashCardForm(data=request.POST)
        if formset.is_valid():
            formset.instance.user = request.user
            formset.save()
            # Redirect to the flashcard list index.
            return redirect(to='list_flashcards')
    else:
        formset = FlashCardForm()

    return_dict = {
        'formset': formset
    }

    return render_to_response(template_name, return_dict,
                             context_instance=RequestContext(request))

@login_required
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

@login_required
def delete_flashcard(request, flashcard_id):
    """
    Delete a flashcard given the `ID`.
    """
    FlashCard.objects.filter(id = flashcard_id).delete()

    return redirect('list_flashcards') # Redirect to the flashcard list

@login_required
def practice_flashcards(request, template_name='practice_flashcards.html'):
    """
    Practice a flashcard.
    """
    # Get the latest element you should practice
    practices = FlashCard.by_practice.filter(user=request.user)
    if len(practices) == 0:
        return render_to_response(template_name, {
            'errors': ['No items to practice']})

    practice = practices[0]
    form = RatingForm(initial={'id': practice.id})

    return_dict = {
        'practice': practice,
        'form': form
    }

    return render_to_response(template_name, return_dict,
                              context_instance=RequestContext(request))

@csrf_protect
@login_required
def process_rating(request):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            practice_item = get_object_or_404(FlashCard,
                                              pk=int(form.cleaned_data['id']))
            practice_item.set_next_practice(int(form.cleaned_data['rating']))
            practice_item.save()

            return redirect(to='list_flashcards')
    else:
        return HttpResponseBadRequest("There's nothing here. Haha.")
