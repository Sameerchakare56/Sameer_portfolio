from django.shortcuts import render
from .portfolio_data import PORTFOLIO_DATA

def index(request):
    """
    Renders Sameer Chakravedi's portfolio homepage.
    All data is stored in portfolio_data.py for quick and easy modifications.
    """
    return render(request, 'index.html', PORTFOLIO_DATA)
