from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'post/index.html')

def contact(request):
	return render(request, 'post/contact.html')

def about(request):
	return render(request, 'post/about.html')

def blog(request):
	return render(request, 'post/blog.html')

def work(request):
	return render(request, 'post/work.html')