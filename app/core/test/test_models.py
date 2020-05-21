from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@londonappdev.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTest(TestCase):
    # Create User
    def test_create_user__with_correct_email_and_password__should_create_user(self):
        email = 'test@abv.bg'
        password = 'test_pass'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    # def test_new_user_email_normalized(self):
    def test_create_user__with_uppercase_domain_name__should_normalize_to_lovercase(self):
        """Test the email for a new user is normalized"""
        email = 'test@ABV.BG'
        user = get_user_model().objects.create_user(email=email,password='asd')

        self.assertEqual(user.email, email.lower())

    def test_create_user__with_invalid_email__should_raise_error(self):
        with self.assertRaises(ValueError) as context_manager:
            get_user_model().objects.create_user(email='', password='asdpassss')
        # self.assertIsNotNone(context_manager.exception)

    # Create Superuser
    def test_create_superuser__should_created_it(self):
        user = get_user_model().objects.create_superuser('test@abv.bg', 'passss123123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    # Tag
    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)


