from django.test import TestCase
from django.utils import timezone

from models import Poll


class PollModelTest(TestCase):
    def test_creating_a_new_poll_and_sawing_it_to_the_database(self):
        poll = Poll()
        poll.question = "What's up?"
        poll.pub_date = timezone.now()

        poll.save()

        all_polls_from_db = Poll.objects.all()
        self.assertEquals(len(all_polls_from_db), 1)
        first_poll_from_db = all_polls_from_db[0]
        self.assertEquals(first_poll_from_db, poll)

        self.assertEquals(first_poll_from_db.question, "What's up?")
        self.assertEquals(first_poll_from_db.pub_date, poll.pub_date)

