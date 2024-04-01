from django.shortcuts import render
from .forms import CalculatorForm
from .calculator_python import calculator

def calculator_view(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            consumo1 = form.cleaned_data['consumo1']
            consumo2 = form.cleaned_data['consumo2']
            consumo3 = form.cleaned_data['consumo3']
            tarifa = form.cleaned_data['tarifa']
            tipo_tarifa = form.cleaned_data['tipo_tarifa']
            
            economia_anual, economia_mensal, desconto, cobertura = calculator(consumo1, consumo2, consumo3, tarifa, tipo_tarifa)
            return render(request, 'calculator_result.html', {'economia_anual': economia_anual, 'economia_mensal': economia_mensal, 'desconto': desconto, 'cobertura': cobertura})
    else:
        form = CalculatorForm()
    return render(request, 'calculator_form.html', {'form': form})