from django_filters import rest_framework as filters

from .models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    # TODO: задайте требуемые фильтры
    created_at = filters.DateFromToRangeFilter()
    status = filters.ChoiceFilter(choices=AdvertisementStatusChoices.choices)

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status', 'creator', 'title']