import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandParser
from pathlib import Path
from typing import Any, Optional
from urllib.parse import unquote, urlparse

from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = 'Get location with images'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('json_url', type=str)

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        try:
            response = requests.get(options['json_url'])
            response.raise_for_status()
            location = response.json()
            image_urls = location['imgs']

            place, is_created = Place.objects.get_or_create(
                title=location['title'],
                summary=location['description_short'],
                description=location['description_long'],
                longitude=location['coordinates']['lng'],
                latitude=location['coordinates']['lat'],
            )
        except requests.exceptions.HTTPError:
            self.stderr.write(self.style.ERROR(
                f'Location {options["json_url"]} is not available'))
            return
        except KeyError as e:
            self.stderr.write(self.style.ERROR(
                f'Field "{e.args[0]}" is missing in location'))
            return
            
        if not is_created:
            place.images.all().delete()

        for index, img_link in enumerate(image_urls):
            try:
                filename = unquote(Path(urlparse(img_link).path).name)
                image_response = requests.get(img_link)
                image_response.raise_for_status()
                image_content = ContentFile(image_response.content)

                place_image = PlaceImage(index=index, place=place)
                place_image.image.save(filename, content=image_content)
            except requests.exceptions.HTTPError:
                self.stderr.write(self.style.ERROR(
                    f'Image {img_link} is missing'))
            self.stdout.write(self.style.SUCCESS('Image for location is loaded'))
