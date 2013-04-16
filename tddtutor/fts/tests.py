from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PollsTest(LiveServerTestCase):
    fixtures = ['admin_user.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_create_new_poll_via_admin_site(self):
        # Kate opens her web browser, and goes to the admin page
        self.browser.get(self.live_server_url + '/admin/')

        # She sees the familiar 'Django administration' heading
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Django administration', body.text)

        # She types in her username and password and hits return
        username_field =  self.browser.find_element(By.NAME, 'username')
        username_field.send_keys('admin')

        password_field = self.browser.find_element(By.NAME, 'password')
        password_field.send_keys('pass')
        password_field.send_keys(Keys.RETURN)

        # her username and password are accepted, and she is taken to
        # the Site Administration page
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Site administration', body.text)

        # She now sees a couple of hyperlink that says "Pools"
        polls_links = self.browser.find_elements(By.LINK_TEXT, 'Polls')
        self.assertEquals(len(polls_links), 2)

        # todo: use the admin site to create a Poll
        self.fail('finish this test')
