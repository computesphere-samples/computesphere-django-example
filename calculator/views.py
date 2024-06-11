from django.shortcuts import render
from .forms import DateForm
from datetime import date

def calculate_age(request):
    age = None
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            dob = form.cleaned_data['date_of_birth']
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    else:
        form = DateForm()

    return render(request, 'calculator/age_calculator.html', {'form': form, 'age': age})
