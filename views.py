from django.shortcuts import get_object_or_404, render_to_response

from dvoc.models import FlashCard

def flashcard_list(request, template_name='dvoc/list_flashcards.html'):
    """
    Return a list with flash cards.
    """
    flashcard_list = FlashCard.objects.all()
    return render_to_response(template_name, {'flascard_list': flashcard_list})

def create_flashcard(request, template_name='dvoc/create_flashcard.html'):
    """
    Create a flashcard.
    """
    pass
