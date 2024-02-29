from django.shortcuts import render, redirect
from .models import registering, posting
from .forms import newregister, newpost, Editpost, Editregister

# Create your views here.


def home(request):
    return render(request, 'index.html')

# register updeat

def registerup(request, id):
    news = registering.objects.get(id = id)
    if request.method == 'POST':
        form = Editregister(request.POST, instance=news)

        if form.is_valid():
            reg = form.save()
            return redirect('viewre')
    else:
        form = Editregister(instance=news)

    return render(request, 'sign_up.html', {'id': id, 'form':form})

# register create

def registercreate(request):

    if request.method == 'POST':
        form = newregister(request.POST)

        if form.is_valid():
            reg = form.save()
            reg.save()
            return redirect('viewre')

    fo = newregister()

    return render(request, 'creatre.html', {'fo': fo})

# view register

def viewre(request):
    

    viewr = registering.objects.all()
    data = {'viewr': viewr}
    return render(request, 'viewsign.html', data)




# Delete register


def deleteregister(request, id):
    dele = registering.objects.get(id = id)
    dele.delete()
    return redirect('viewre')

# post created

def post(request):

    if request.method == 'POST':
        form = newpost(request.POST, request.FILES)

        if form.is_valid():
            reg = form.save()
            reg.save()
            return redirect('viewpost')

    fo = newpost() 
    return render(request, 'post.html', {'fo': fo})

# post delete

def delete(request, id):
    dele = posting.objects.get(id = id)
    dele.delete()
    return redirect('viewpost')



# view post

def viewpost(request):


    viewp= posting.objects.all()

    data = {'viewp': viewp}
    return render(request, 'vewpost.html', data)




# edit poset form
def editpost(request, id):
    news = posting.objects.get(id = id)
    if request.method == 'POST':
        form = Editpost(request.POST, request.FILES, instance=news)

        if form.is_valid():
            reg = form.save()
            return redirect('viewpost')
    else:
        form = Editpost(instance=news)

    return render(request, 'update_post.html', {'id': id, 'form':form})