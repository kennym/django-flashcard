"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.auth.models import User

from models import FlashCard
from views import (
    list_flashcards,
    create_flashcard,
    edit_flashcard,
    delete_flashcard
)

class FlashCardTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("test", "test@localhost",
                                                 "guessme")
    def test_create_flashcard_as_valid_user(self):
        """
        Create a flashcard with as a valid user in the db.
        """
        # Create the flashcard
        flashcard = FlashCard(
            front = "Test front",
            back = "Test Back",
            user = self.user)
        # Save it
        flashcard.save()

        self.assertEquals(FlashCard.objects.all()[0], flashcard)

    def test_edit_flashcard(self):
        pass

    def test_delete_flashcard(self):
        pass

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

