import django_filters
from django import forms
from costs.spending.models import Spending

class LeadEntriesFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='timestamp',
                                           widget= forms.DateInput(attrs={'class': 'form-control form-control-lg', 'type': 'date'}),
                                           lookup_expr='gte', label='Начальная дата')
    end_date = django_filters.DateFilter(field_name='timestamp',
                                         widget= forms.DateInput(attrs={'class': 'form-control form-control-lg', 'type': 'date'}),
                                         lookup_expr='lte', label='Конечная дата')
    
    
    class Meta:
        model = Spending
        fields = ['start_date', 'end_date']
        
    @property
    def qs(self):
        parent = super().qs

        return parent.order_by('-timestamp')