from django.core.management.base import BaseCommand
from inventario.models import Categoria
from datetime import date


class Command(BaseCommand):
    help = 'Carga categorías iniciales en la base de datos'

    def handle(self, *args, **kwargs):
        categorias = [
            ("Abarrotes", "Productos básicos de consumo diario"),
            ("Lácteos", "Leche, queso, yogurt y derivados"),
            ("Bebidas", "Refrescos, jugos y bebidas en general"),
            ("Botanas", "Papas, frituras y snacks"),
            ("Limpieza", "Productos de higiene y limpieza"),
            ("Higiene personal", "Cuidado personal"),
            ("Panadería", "Pan y productos horneados"),
            ("Enlatados", "Alimentos en conserva"),
            ("Dulces", "Golosinas y chocolates"),
            ("Mascotas", "Alimentos y accesorios para mascotas"),
        ]

        for nombre, descripcion in categorias:
            obj, created = Categoria.objects.get_or_create(
                nombre=nombre,
                defaults={
                    "descripcion": descripcion,
                    "fecha_creacion": date.today()
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"✔ Categoría creada: {nombre}"))
            else:
                self.stdout.write(self.style.WARNING(f"• Ya existe: {nombre}"))

        self.stdout.write(self.style.SUCCESS("Proceso terminado."))