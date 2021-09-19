from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
# Create your views here.

def Index(request):
    return render(request, 'index.html')

def GetData(request):
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vS9hkCVqhrG2ihyl7FIC9RJj6B_0i9_ybM3wfCINiu8iZxyBhzPP_5zP0N6nJEPuVrZuN1nFWae7wRz/pub?output=csv'
    df = pd.read_csv(url)
    data = df.to_csv()
    return HttpResponse(data)
