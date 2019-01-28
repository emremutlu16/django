from django.core.management.base import BaseCommand, CommandError
from api.models import Student


class Command(BaseCommand):
    help = 'Delete student'

    def add_arguments(self, parser):
        parser.add_argument('student_id',  type=int, help='id of student')

    def handle(self, *args, **options):
        import ipdb; ipdb.set_trace()
        student_id = options.get('student_id')
        if Student.objects.filter(id=student_id).exists():
            Student.objects.filter(id=student_id).delete()
        else:
            raise CommandError("Student does not exist")

    # def handle(self, *args, **options):
    #     student_id = options.get('student_id')
    #     print(type(student_id))
    #     print(student_id)
    #     a = student_id[0]
    #     print(a)
    #     print(Student.objects.filter(id=a).exists())
    #     if Student.objects.filter(id=a).exists():
    #         s = Student.objects.get(id=a)
    #         s.delete()
    #     else:
    #         raise CommandError("hopplara")
    #     print("çak abim")
