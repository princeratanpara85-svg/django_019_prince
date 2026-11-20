import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management_system.settings')
django.setup()

from main_app.models import CustomUser, Course, Session, Staff, Student, Subject

def seed():
    print("Seeding Student Management System demo accounts and records...")

    # 1. Create HOD / Administrator
    admin_email = "admin@admin.com"
    if not CustomUser.objects.filter(email=admin_email).exists():
        admin_user = CustomUser.objects.create_superuser(
            email=admin_email,
            password="admin",
            first_name="Dr. Vikram",
            last_name="Sharma",
            user_type='1',
            gender='M'
        )
        print(f"-> HOD / Admin created: {admin_email} / 'admin'")
    else:
        print(f"-> HOD / Admin already exists: {admin_email}")

    # 2. Create Sample Session
    session, _ = Session.objects.get_or_create(
        start_year=date(2026, 1, 1),
        end_year=date(2026, 12, 31)
    )
    print(f"-> Academic Session: {session}")

    # 3. Create Sample Course
    course, _ = Course.objects.get_or_create(name="B.Tech Computer Science & Engineering")
    print(f"-> Academic Course: {course.name}")

    # 4. Create Staff Account
    staff_email = "staff@staff.com"
    if not CustomUser.objects.filter(email=staff_email).exists():
        staff_user = CustomUser.objects.create_user(
            email=staff_email,
            password="staff",
            first_name="Prof. Ananya",
            last_name="Iyer",
            user_type='2',
            gender='F'
        )
        staff_profile = Staff.objects.get(admin=staff_user)
        staff_profile.course = course
        staff_profile.save()
        print(f"-> Faculty / Staff created: {staff_email} / 'staff'")
    else:
        print(f"-> Staff already exists: {staff_email}")

    # 5. Create Sample Subject
    staff_profile = Staff.objects.first()
    if staff_profile:
        subject, _ = Subject.objects.get_or_create(
            name="Database Management Systems (DBMS)",
            course=course,
            staff=staff_profile
        )
        print(f"-> Subject created: {subject.name}")

    # 6. Create Student Account
    student_email = "student@student.com"
    if not CustomUser.objects.filter(email=student_email).exists():
        student_user = CustomUser.objects.create_user(
            email=student_email,
            password="student",
            first_name="Rahul",
            last_name="Verma",
            user_type='3',
            gender='M'
        )
        student_profile = Student.objects.get(admin=student_user)
        student_profile.course = course
        student_profile.session = session
        student_profile.save()
        print(f"-> Student created: {student_email} / 'student'")
    else:
        print(f"-> Student already exists: {student_email}")

    print("\n--- DEMO LOGIN CREDENTIALS ---")
    print("1. HOD / Admin : admin@admin.com  |  password: admin")
    print("2. Staff / Faculty: staff@staff.com  |  password: staff")
    print("3. Student       : student@student.com  |  password: student")

if __name__ == '__main__':
    seed()
