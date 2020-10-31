from django.shortcuts import render


def main(request):
    return render(request, 'main/main.html')

def main_detail(request):
    return render(request, 'main/main_detail.html')
