from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306213836',
        'name': 'Dionysius Davis',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)