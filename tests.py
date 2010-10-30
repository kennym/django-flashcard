"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase

from models import FlashCard
from views import (
    list_flashcards,
    create_flashcard,
    edit_flashcard,
    delete_flashcard
)

class FlashCardTestCase(TestCase):
    def test_create_flashcard(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

    def test_list_flashcards(self):
        pass
    
    def test_edit_flashcard(self):
        pass

    def test_delete_flashcard(self):
        pass

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

