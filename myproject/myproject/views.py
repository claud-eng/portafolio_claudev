from django.shortcuts import render

def portfolio_details(request):
    return render(request, 'portfolio_details.html')

def service_details(request):
    return render(request, 'service_details.html')

def starter_page(request):
    return render(request, 'starter_page.html')

