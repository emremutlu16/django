from django.core.management.base import BaseCommand, CommandError
from api.models import Student


class Command(BaseCommand):
    help = 'Stands for updating student information'

    def add_arguments(self, parser):
        parser.add_argument('field', type=str)

        parser.add_argument('-u', '--update', nargs='+', help="Update", )

    def handle(self, *args, **options):
        student_field = options.get('field')
        old_data = options.get('update')[0]
        new_data = options.get('update')[1]
        filter_data = {student_field: old_data}
        update_data = {student_field: new_data}
        student = Student.objects.filter(**filter_data).update(**update_data)
        if not student:
            raise CommandError('{} not found'.format(student_field))
