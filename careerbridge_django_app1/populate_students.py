# IMPORT STATEMENTS
import os
import sys
import django
from faker import Faker

# Add the project directory to sys.path
sys.path.append(r'D:\CareerBridge\Django\DjangoProjectDir\careerbridge_django_project1')

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'careerbridge_django_project1.settings')
django.setup()


# Import the model
from careerbridge_django_app1.models import Student

# Populate script
fake = Faker()

def create_students(n=50):
    for _ in range(n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.unique.email()
        course_name = "Django Training"
        enrollment_date = fake.date_between(start_date='-30d', end_date='today')

        print(f"Creating student: {first_name} {last_name}, {email}, {course_name}, {enrollment_date}")

        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            course_name=course_name,
            enrollment_date=enrollment_date
        )

        print(f"Student {first_name} {last_name} created successfully.")

if __name__ == '__main__':
    print("Populating the database with students data...")
    create_students(50)
    print("Database populated successfully...")
