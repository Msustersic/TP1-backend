from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Asigna permisos de staff a un usuario específico'

    def handle(self, *args, **options):
        username = input("Ingrese el nombre de usuario del usuario al que desea asignar permisos de staff: ")

        try:
            usuario = User.objects.get(username=username)
            usuario.is_staff = True
            usuario.save()
            self.stdout.write(self.style.SUCCESS(f"Se han asignado permisos de staff a {username}"))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"No se encontró el usuario con nombre de usuario {username}"))
