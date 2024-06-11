from django.shortcuts import render
from .forms import DateForm
from datetime import date
from dateutil.relativedelta import relativedelta

def calculate_age(request):
    age_details = None
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            dob = form.cleaned_data['date_of_birth']
            today = date.today()
            delta = relativedelta(today, dob)
            age_details = {
                'years': delta.years,
                'months': delta.months,
                'days': delta.days
            }
    else:
        form = DateForm()
    return render(request, 'calculator/age_calculator.html', {'form': form, 'age_details': age_details})
