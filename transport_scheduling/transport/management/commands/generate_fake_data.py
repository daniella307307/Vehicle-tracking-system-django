import random
from django.core.management.base import BaseCommand
from faker import Faker
from transport.models import Location, Driver, Vehicle, Route, Schedule
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transport_scheduling.settings')
django.setup()

class Command(BaseCommand):
    help = 'Generate fake data for testing the model'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # List of some Rwandan cities or towns
        rwandan_cities = [
            'Kigali', 'Butare', 'Musanze', 'Gisenyi', 'Rubavu', 'Rwamagana',
            'Nyundo', 'Kibuye', 'Kamonyi', 'Nyanza', 'Musanze', 'Gicumbi', 'Huye'
        ]

        # Generate fake Locations based on Rwandan cities
        for _ in range(1000):
            city = random.choice(rwandan_cities)
            Location.objects.create(
                name=city,
                latitude=fake.latitude(),
                longitude=fake.longitude(),
                location_type=random.choice(['Urban', 'Rural', 'Suburban'])
            )

        # Generate fake Drivers with Rwandan-style names
        for _ in range(1000):
            contact_number = '250' + ''.join(random.choices('0123456789',k=9))
            Driver.objects.create(
                name=fake.first_name_male() + " " + fake.last_name(),
                license_number=fake.bothify(text='??####??'),
                contact_number=contact_number
            )

        # List of vehicle makes commonly found in Rwanda
        rwandan_vehicle_makes = ['Toyota', 'Nissan', 'Honda', 'Mitsubishi', 'Isuzu', 'Mazda']

        # Generate fake Vehicles
        for _ in range(1000):
            driver = random.choice(Driver.objects.all())  # Randomly assign a driver
            Vehicle.objects.create(
                VIN=fake.bothify(text='??????#####????'),
                make=random.choice(rwandan_vehicle_makes),
                model=fake.word(),
                year=random.randint(1990, 2025),
                color=fake.color_name(),
                capacity=random.randint(1, 15),
                driver=driver,
                status=random.choice(['Active', 'Inactive'])
            )

        # Generate fake Routes with Rwandan locations
        for _ in range(1000):
            start_location = random.choice(Location.objects.all())  # Random start location
            end_location = random.choice(Location.objects.all())    # Random end location
            Route.objects.create(
                start_location=start_location.name,
                end_location=end_location.name,
                distance=random.uniform(10.0, 500.0),  # Random distance in km
                duration=random.uniform(0.5, 10.0),    # Random duration in hours
                estimated_time=random.uniform(0.5, 10.0)
            )

        # Generate fake Schedules
        for _ in range(1000):
            vehicle = random.choice(Vehicle.objects.all())   # Random vehicle
            driver = random.choice(Driver.objects.all())     # Random driver
            route = random.choice(Route.objects.all())       # Random route
            Schedule.objects.create(
                vehicle=vehicle,
                driver=driver,
                route=route,
                departure_time=fake.date_time_this_year(),
                arrival_time=fake.date_time_this_year(),
                estimated_time=route.estimated_time
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated fake data for Rwanda'))
