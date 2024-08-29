from django.test import TestCase,Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Exercise, Comment, ContactMessage, CommentReport
from .forms import CommentForm, ContactMessageForm, ReportCommentForm

class ExerciseModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.exercise = Exercise.objects.create(
            title="Test Exercise",
            description="This is a test exercise.",
            author=self.user,
            status=1
        )

    def test_exercise_creation(self):
        self.assertEqual(self.exercise.title, "Test Exercise")
        self.assertEqual(str(self.exercise), "Test Exercise")

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.exercise = Exercise.objects.create(
            title="Test Exercise",
            description="This is a test exercise.",
            author=self.user,
            status=1
        )
        self.comment = Comment.objects.create(
            exercise=self.exercise,
            user=self.user,
            body="This is a test comment."
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.body, "This is a test comment.")
        self.assertEqual(str(self.comment), f"Comment This is a test comment. by {self.user.username}")

class ExerciseViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.exercise = Exercise.objects.create(
            title="Test Exercise",
            description="This is a test exercise.",
            author=self.user,
            status=1
        )
    
    def test_exercise_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Exercise")
    
    def test_exercise_detail_view(self):
        response = self.client.get(reverse('exercise_detail', args=[self.exercise.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Exercise")
    
    def test_add_comment_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('add_comment', args=[self.exercise.pk]), {
            'body': 'This is a new comment.',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Comment.objects.filter(body='This is a new comment.').exists())

class CommentReportTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.exercise = Exercise.objects.create(
            title="Test Exercise",
            description="This is a test exercise.",
            author=self.user,
            status=1
        )
        self.comment = Comment.objects.create(
            exercise=self.exercise,
            user=self.user,
            body="This is a test comment."
        )

class CommentReportTest(TestCase):
    def setUp(self):
        # Creating my test user
        self.user = User.objects.create_user(username='testuser', password='12345')
        
        # Logggin in
        self.client.login(username='testuser', password='12345')
        
        # Create a test exercise and comment
        self.exercise = Exercise.objects.create(title='Test Exercise', description='Test Description')
        self.comment = Comment.objects.create(exercise=self.exercise, body='Test comment', user=self.user)
        
        # URL for reporting a comment
        self.report_url = reverse('report_comment', args=[self.comment.id])
    
    def test_report_comment(self):
        # Post valid data to the report comment view
        response = self.client.post(self.report_url, {
            'reason': 'Spam',  
        })
        
        # Response redirect
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        
        # Checking if comment was created
        self.assertTrue(CommentReport.objects.filter(comment=self.comment, user=self.user).exists())

class ContactMessageFormTest(TestCase):
    def test_contact_message_form(self):
        form_data = {
            'name': 'Test Name',
            'email': 'test@example.com',
            'message': 'This is a test message.',
        }
        form = ContactMessageForm(data=form_data)
        self.assertTrue(form.is_valid())


