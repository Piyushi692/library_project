from .models import Author
from django.db import IntegrityError


def generate_author_id(city):
    prefix = 'AR'
    city_code = city[:3].upper()

    # Use a loop to handle potential race conditions
    while True:
        try:
            # Find the last author ID for the given city
            last_author = Author.objects.filter(author_id__startswith=f'{prefix}{city_code}').order_by('author_id').last()

            if last_author:
                last_id = int(last_author.author_id[5:])
                new_id = f"{prefix}{city_code}{str(last_id + 1).zfill(4)}"
            else:
                new_id = f"{prefix}{city_code}0001"

            return new_id

        except IntegrityError:
            # Handle the situation where the generated ID already exists due to a race condition
            continue
