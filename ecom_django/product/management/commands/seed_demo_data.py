from decimal import Decimal

from django.core.management.base import BaseCommand

from product.models import Category, Product


class Command(BaseCommand):
    help = "Seed starter categories and products for local development."

    def handle(self, *args, **options):
        categories = [
            ("Summer", "cat1"),
            ("Winter", "cat2"),
        ]

        for name, slug in categories:
            Category.objects.get_or_create(slug=slug, defaults={"name": name})

        summer = Category.objects.get(slug="cat1")
        winter = Category.objects.get(slug="cat2")

        products = [
            {
                "category": summer,
                "name": "Light Denim Jacket",
                "slug": "light-denim-jacket",
                "description": "A lightweight denim jacket for warm days.",
                "price": Decimal("49.99"),
                "image": "uploads/summer1.jpg",
            },
            {
                "category": summer,
                "name": "Linen Overshirt",
                "slug": "linen-overshirt",
                "description": "A breathable overshirt for summer layering.",
                "price": Decimal("39.99"),
                "image": "uploads/summer1.jpg",
            },
            {
                "category": winter,
                "name": "Puffer Jacket",
                "slug": "puffer-jacket",
                "description": "A warm insulated jacket for cold weather.",
                "price": Decimal("89.99"),
                "image": "uploads/winter3.jpg",
            },
            {
                "category": winter,
                "name": "Wool Coat",
                "slug": "wool-coat",
                "description": "A clean wool coat for winter outfits.",
                "price": Decimal("119.99"),
                "image": "uploads/winter3.jpg",
            },
        ]

        for product in products:
            Product.objects.update_or_create(
                category=product["category"],
                slug=product["slug"],
                defaults={
                    "name": product["name"],
                    "description": product["description"],
                    "price": product["price"],
                    "image": product["image"],
                    "thumbnail": product["image"],
                },
            )

        self.stdout.write(self.style.SUCCESS("Seeded demo categories and products."))
