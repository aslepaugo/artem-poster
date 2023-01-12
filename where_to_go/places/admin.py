from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, PlaceImage


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    readonly_fields = (
        'img_preview',
    )
    extra = 0
    fields = ('image', 'img_preview')

    def img_preview(self, instance):
        return format_html('<img src="{url}" height="{height}" style="max-width:300px; max-height:200px"/>',
            url = instance.image.url,
            height="200px",
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        PlaceImageInline,
    ]
