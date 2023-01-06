from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.urls import reverse

from places.models import Place


def index(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.longitude, place.latitude]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse(place_detail_view, args=[place.id])
                }
            }
        )
    geo = {
        "type": "FeatureCollection",
        "features": features,
    }
    context = {"places": geo}
    return TemplateResponse(request, "index.html", context)


def place_detail_view(_, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_details = {
        "title": place.title,
        "imgs": [img.image.url for img in place.images.order_by('index')],
        "description_short": place.summary,
        "description_long": place.description,
        "coordinates": {
            "lat": place.latitude,
            "lng": place.longitude,
        },
    }

    return JsonResponse(
        place_details, 
        json_dumps_params={
            'indent': 2,
            'ensure_ascii': False,
        }
    )
