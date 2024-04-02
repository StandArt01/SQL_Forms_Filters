from django_filters import FilterSet, ModelMultipleChoiceFilter
from .models import Product, Material

class ProductFilter(FilterSet):
    material = ModelMultipleChoiceFilter(
        field_name='productmaterial_material',
        queryset=Material.objects.all(),
        label='Material',
        conjoined=False,
    )

   class Meta:
       model = Product
       fields = {
           'productmaterial_material': ['exact'],
           'name': ['icontains'],
           'quantity': ['gt'],
           'price': [
               'lt',
               'gt',
           ],
       }