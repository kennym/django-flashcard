"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.test import TestCase, Client
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
        self.password = "password"
        self.user = User.objects.create_user("test", "test@localhost",
                                             self.password)
        self.client = Client()

    def create_flashcard(self, front="", back=""):
        """
        A DRY method for creating a flashcard and returning the instance.
        """
        # Create the flashcard
        flashcard = FlashCard(
            front = front,
            back = back,
            user = self.user)
        # Save it
        flashcard.save()
        return flashcard # Return the FlashCard instance

    def login(self, username=None, password=None):
        user = username or self.user.username
        pw   = password or self.password
        # Login as the owner of the flashcard
        login = self.client.login(username=user,
                                  password=pw)
        return login

    def test_create_flashcard_as_valid_user(self):
        """
        Create a flashcard with as a valid user in the db.
        """
        # Create the flashcard
        flashcard = self.create_flashcard("Test", "Test")

        filter = FlashCard.objects.filter
        # Check that the the front is the same
        self.assertEquals(filter(id=flashcard.id).get().front, 
                          flashcard.front)
        # Check that the back is the same
        self.assertEquals(filter(id=flashcard.id).get().back, 
                          flashcard.back)
        # Check the ID is the same
        self.assertEquals(filter(id=flashcard.id).get().id,
                          flashcard.id)

    def test_login_as_valid_user(self):
        """
        Log-in as a valid user.
        """
        login = self.login()
        self.failUnless(login, "Could not login")

    def test_login_as_invalid_user(self):
        """
        Log-in as an invalid user.
        """
        login = self.login("Invalid_user", "Invalid_password")
        self.assertEquals(login, False)

    def test_edit_flashcard_with_valid_form_data(self):
        """
        Assert that editing an existing flashcard gets actually updated.
        """
        # Create the flashcard
        flashcard = self.create_flashcard("Test", "Testback")
        # Login as the owner of the flashcard
        self.login()

        # The data to fill in the form
        post_data = {
            'front' : 'POST',
            'back' : 'POST',
            'user' : self.user
        }

        response = self.client.post(reverse('edit_flashcard',
                                            args=[flashcard.id]),
                                    post_data)
        # Should redirect to the detail view page or the flashcard index.
        self.assertEquals(response.status_code, 302)
        # Check if the values have really changed of the card
        self.assertEquals(FlashCard.objects.filter(
            id=flashcard.id).values()[0]['front'], post_data['front'])
        self.assertEquals(FlashCard.objects.filter(
            id=flashcard.id).values()[0]['back'], post_data['back'])

    def test_delete_flashcard_view(self):
        """
        Delete a flashcard.
        """
        # Create a flashcard
        flashcard = self.create_flashcard("TestFront", "Testback")
        # Login as the owner of the flashcard
        self.login()
        # Make the request
        response = self.client.get(reverse('delete_flashcard',
                                           args=[flashcard.id]))
        # Now, it should not exist anymore
        self.assertEquals(FlashCard.objects.filter(id=flashcard.id).exists(),
                          False)

    def test_set_next_practice_item(self):
        # Create the flashcard
        flashcard = self.create_flashcard()

        # Shouldn't raise any errors
        flashcard.set_next_practice(1) 
        flashcard.set_next_practice(2)
        flashcard.set_next_practice(3)
        flashcard.set_next_practice(4)
        flashcard.set_next_practice(5)

        # SCREAM! and mute.
        self.assertRaises(ValidationError, flashcard.set_next_practice, 0)
        self.assertRaises(ValidationError, flashcard.set_next_practice, 6)


    def test_practice_flashcard(self):
        """
        Practice the flashcard with the given ID.
        """
        # Create the flashcard
        flashcard = self.create_flashcard("PracticeFront", "PracticeBack")
        # Log-in as the owner of the flashcard
        self.login()
        # Make the request
        response = self.client.get(reverse('practice_flashcards'))

        # TODO: Post the rating.
        self.fail()
