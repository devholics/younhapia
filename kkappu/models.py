from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.documents.models import AbstractDocument
from wagtail.images.models import AbstractImage, AbstractRendition


class KkappuImage(AbstractImage):
    admin_form_fields = (
        "title",
        "file",
        "collection",
        "tags",
        "focal_point_x",
        "focal_point_y",
        "focal_point_width",
        "focal_point_height",
    )

    class Meta(AbstractImage.Meta):
        verbose_name = _("image")
        verbose_name_plural = _("images")
        permissions = [
            ("choose_image", "Can choose image"),
        ]


class KkappuRendition(AbstractRendition):
    image = models.ForeignKey(
        KkappuImage, on_delete=models.CASCADE, related_name="renditions"
    )

    class Meta:
        unique_together = (("image", "filter_spec", "focal_point_key"),)


class KkappuDocument(AbstractDocument):
    admin_form_fields = ("title", "file", "collection", "tags")

    class Meta(AbstractDocument.Meta):
        permissions = [
            ("choose_document", "Can choose document"),
        ]
