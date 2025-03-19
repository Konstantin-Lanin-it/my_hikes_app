from django.test import TestCase
from .models import Hike, Application

class HikeModelTest(TestCase):

    def setUp(self):
        # Метод setUp выполняется перед каждым тестом
        Hike.objects.create(title="Test Hike", description="A test hike description", image_url="http://example.com/image.jpg")

    def test_hike_creation(self):
        """Проверка создания похода."""
        hike = Hike.objects.get(title="Test Hike")
        self.assertEqual(hike.description, "A test hike description")
        self.assertEqual(hike.image_url, "http://example.com/image.jpg")
        self.assertTrue(isinstance(hike, Hike))
        self.assertEqual(str(hike), "Test Hike")  # Тестирование метода __str__

class ApplicationModelTest(TestCase):

    def setUp(self):
        hike = Hike.objects.create(title="Test Hike", description="A test hike description", image_url="http://example.com/image.jpg")
        Application.objects.create(name="John Doe", email="john@example.com", phone="1234567890", hike=hike)

    def test_application_creation(self):
        """Проверка создания заявки."""
        application = Application.objects.get(name="John Doe")
        self.assertEqual(application.email, "john@example.com")
        self.assertEqual(application.phone, "1234567890")
        self.assertTrue(isinstance(application, Application))
        self.assertEqual(str(application), "John Doe - Test Hike")  # Тестирование метода __str__