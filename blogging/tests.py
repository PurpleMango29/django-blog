from django.test import TestCase
from django.contrib.auth.models import User
from blogging.models import Post

class PostTestCase(TestCase):
    fixtures = ['blogging_test_fixture.json', ]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)

# Run the test: `python manage.py test blogging`

# Or run the tests (if multiple files): `python manage.py test`