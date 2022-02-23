from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Info, Booking, Notify
# Create your views here.

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='Customer')
            user.groups.add(group)
            messages.success(request,'Account was created for ' + username )
            return redirect('loginPage')
    context ={'form' : form}
    return render(request,'admin_login.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request,user)
            # return render(request,'student/home.html')
            return redirect('/dashboard')
        else:
            messages.info(request,'username OR password is incorrect')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('loginPage')

# Create your views here.
def bookPage(request):
    return render(request,'book1.html')

def home(request):
    return  render(request, 'index.html')

def index(request):
    datas = Booking.objects.all()
    context={'datas':datas}
    return  render(request, 'dashboard.html',context)

def book(request,pk):
    data = Info.objects.get(id=pk)
    return render(request,'book1.html',{'data':data})


def about(request):
    return  render(request, 'aboutus.html')

def forrent(request):
    datas = Info.objects.all()
    context = {'datas':datas}
    return  render(request, 'forrent.html',context)

def submit(request,pk):
    data = Info.objects.get(id=pk)
    name = request.POST['name']
    email = request.POST["email"]
    contact = request.POST["contact"]
    location = request.POST["location"]
    book_date= request.POST["book_date"]
    addbooking = Booking(name=name,email=email,contact=contact,book_date=book_date,location=location,book_location=data.book_location,price=data.price,rent_no=data.rent_no)
    addbooking.save()
    messages.success(request, "sucessfully booked!!!")
    return render(request,'book1.html')


def select(request,pk):
    Booking.objects.filter(pk=pk).update(status="Booked")
    return  redirect('/dashboard')

def not_select(request,pk):
    Booking.objects.filter(pk=pk).update(status="Not_Booked")
    return  redirect('/dashboard')

def notify(request):
    return  render(request, 'notify.html')


def notify_submit(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST["email"]
    contact = request.POST["contact"]
    message = request.POST["message"]
    addbooking = Notify(f_name=fname,l_name=lname,email=email,contact=contact,message=message)
    addbooking.save()
    return  render(request, 'notify.html')

def notifyadmin(request):
    datas = Notify.objects.all()
    context = {'datas':datas}
    return  render(request, 'notifyadmin.html',context)
   
def search(request):
    query = request.GET['query']
    data = Info.objects.get(book_location=query)
    context = {
            'data':data
            }
    return render(request,"search.html", context)

def contact(request):
    return render(request,'contact.html')


def detail(request,pk):
    data = Info.objects.get(id=pk)
    return render(request,'detail.html',{'data':data})

def read1(request):
    return render(request,'read1.html')

def read2(request):
    return render(request,'read2.html')

def read3(request):
    return render(request,'read3.html')

def read4(request):
    return render(request,'read4.html')

def read5(request):
    return render(request,'read5.html')

def read6(request):
    return render(request,'read6.html')

def read7(request):
    return render(request,'read7.html')

def read8(request):
    return render(request,'read8.html')

def room1(request):
    return render(request,'room1.html')

def room2(request):
    return render(request,'room2.html')

def room3(request):
    return render(request,'room3.html')

def room4(request):
    return render(request,'room4.html')

def room5(request):
    return render(request,'room5.html')

def room6(request):
    return render(request,'room6.html')

def room7(request):
    return render(request,'room7.html')

def room8(request):
    return render(request,'room8.html')