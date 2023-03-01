from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReviewForm
from .models import Review

# Create your views here
def thank_you(request):
    return render(request, 'my_app/thank_you.html')

def review_form(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('my_app:thank_you'))
    else:
        form = ReviewForm()
        return render(request, 'my_app/form.html', context={'form':form})    
    
def list(request):
    all_review = Review.objects.all()
    context = {'all_review':all_review}
    return render(request, 'my_app/list.html', context=context)

def delete(request):
    if request.POST:
        first_name = request.POST['first_name']
        try:
            Review.objects.get(first_name=str(first_name)).delete()
            return redirect(reverse('my_app:list'))
        except:
            print('Name is not Found')
            return redirect(reverse('my_app:list'))
    else:
        return render(request, 'my_app/delete.html')
    
def home(request):
    return render(request, 'my_app/home.html')

