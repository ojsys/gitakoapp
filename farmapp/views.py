from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import FarmBudget, FarmBlock
from .forms import FarmBlockForm, FarmBudgetForm, CropCalendarForm


# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def farmbudget(request):
    form = FarmBudgetForm
    budgets = FarmBudget.objects.all()

    return render(request, 'farmapp/farm_budget.html', {'form': form,'budgets': budgets})


def addbudget(request):
    form = FarmBudgetForm()
    if request.method == 'POST':
        form = FarmBudgetForm(request.POST)
        if form.is_valid():
            farmname = form.cleaned_data['farmname']
            blocks = form.cleaned_data['blocks']
            crop = form.cleaned_data['crop']
            location = form.cleaned_data['location']
            hectares = form.cleaned_data['hectares']
            cropseason = form.cleaned_data['cropseason']
            particulars = form.cleaned_data['particulars']
            productbrand = form.cleaned_data['productbrand']
            quantity = form.cleaned_data['quantity']
            description = form.cleaned_data['description']
            units = form.cleaned_data['units']
            rates = form.cleaned_data['rates']
            totalcost = form.cleaned_data['totalcost']

            new_budget = FarmBudget(
                farmname = farmname,
                blocks = blocks,
                crop = crop,
                location = location,
                hectares = hectares,
                cropseason = cropseason,
                particulars = particulars,
                productbrand = productbrand,
                quantity = quantity,
                description = description,
                units = units,
                rates = rates,
                totalcost = totalcost

            )
            new_budget.save()
            return render(request, 'add_budget.html', {'form': FarmBudgetForm(), 'success': True})
    else:
        form = FarmBudgetForm()

    return render(request, 'add_budget.html', {'form': form})