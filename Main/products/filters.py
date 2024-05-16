import django_filters
from django import forms
class ProductFilter(django_filters.FilterSet):
    sort = (
        ('گران ترین', 'گران ترین'),
        ('ارزان ترین', 'ارزان ترین'),
        ('محصولات پرتخفیف', 'محصولات پرتخفیف'),
    )
    less = django_filters.NumberFilter(field_name='unit_price', lookup_expr='gte', label='حداقل قیمت',
                                       widget=forms.TextInput(attrs={'class': 'form-control'}))
    more = django_filters.NumberFilter(field_name='unit_price', lookup_expr='lte', label='حداکثر قیمت',
                                       widget=forms.TextInput(attrs={'class': 'form-control'}))
    sort_product = django_filters.ChoiceFilter(choices=sort, label='مرتب سازی', method='get_sort',
                                               widget=forms.Select(attrs={'class': 'form-control'}))
    def get_sort(self, queryset, name, value):
        if value == 'گران ترین':
            order = '-unit_price'
            return queryset.order_by(order)
        if value == 'ارزان ترین':
            order = 'unit_price'
            return queryset.order_by(order)
        if value == 'محصولات پرتخفیف':
            order = 'discount'
            return queryset.order_by(order)
