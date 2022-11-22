from django.shortcuts import render

# Create your views here.


def predict(request):
    return render(request, 'predict.html')

def predict_chances(request):
    pass