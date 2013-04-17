from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

from models import Poll


class PollModelTest(TestCase):
    def test_creating_a_new_poll_and_saving_it_to_the_database(self):
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


class PollsPageViewTest(TestCase):
    def test_polls_page_shows_links_to_all_polls(self):
        #setup polls
        poll1 = Poll(question='6 times 7', pub_date=timezone.now())
        poll1.save()
        poll2 = Poll(question='How is your day', pub_date=timezone.now())
        poll2.save()

        #access polls view
        response = self.client.get(reverse('polls.views.show_all_pools'))
        #check if right template used
        self.assertTemplateUsed(response, 'all_polls.html')

        #check if polls transferred to template
        polls_in_context = response.context['polls']
        self.assertEquals(list(polls_in_context), [poll1, poll2])

        #check if polls displayed on the page
        self.assertIn(poll1.question, response.content)
        self.assertIn(poll2.question, response.content)

        #check if polls has links to individual poll
        self.assertIn(reverse('polls.views.poll', args=[poll1.id]),
                      response.content)
        self.assertIn(reverse('polls.views.poll', args=[poll2.id]),
                      response.content)
