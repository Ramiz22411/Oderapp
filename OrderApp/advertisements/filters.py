import django_filters
from .models import Advertisement


class AdvertisementFilters(django_filters.FilterSet):
    condition = django_filters.BooleanFilter(field_name='condition', label="Новое")
    category = django_filters.ModelChoiceFilter(queryset=Advertisement.objects.none(), label='Категория')
    title = django_filters.CharFilter(lookup_expr='icontains', label='Поиск по названию')

    class Meta:
        model = Advertisement
        fields = ("category", "condition", "title")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Это что бы не было циклического импорта
        from .models import CategoryAds

        self.filters["category"].queryset = CategoryAds.objects.all()
