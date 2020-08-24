from django.shortcuts import render, get_object_or_404

from .forms import FormOfMeasurement
from .models import Measurement


# Create your views here.

def index(request):
    obj = get_object_or_404(Measurement)
    form = FormOfMeasurement(request.POST or None)
    context = {"obj": obj, "form": form}
    return render(request, "main.html", context)
