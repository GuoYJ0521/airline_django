from django.test import Client, TestCase
from .models import Airport, Flight, Passenger

# Create your tests here.
class FlightTestCase(TestCase):
    
    def setUp(self):

        a1 = Airport.objects.create(code="AAA", city="City A")
        a2 = Airport.objects.create(code="BBB", city="City B")

        Flight.objects.create(orgin=a1, destination=a2, duration=100)
        Flight.objects.create(orgin=a1, destination=a1, duration=200)
        Flight.objects.create(orgin=a1, destination=a2, duration=-100)

    def test_departures_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.departures.count(), 3)

    def test_arrivals_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.arrivals.count(), 1)