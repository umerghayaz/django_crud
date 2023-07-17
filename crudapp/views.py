from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm,CreateUserForm
from django.contrib import messages #import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
# Create your views here.
@login_required(login_url='login')
def emp(request):
    # if request.method=='POST':
    form=EmployeeForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "user added.")
        return redirect('/show')
    return render(request,'index.html',{'form':form})
@login_required(login_url='login')
def show(request):
    employees =Employee.objects.all()
    return render(request, 'show.html', {'employees': employees })
@login_required(login_url='login')
def boot(request):
    return render(request, 'home.html')
@login_required(login_url='login')
def destroy(request,id):
    employees =Employee.objects.get(id=id)
    employees.delete()
    messages.warning(request, "user deleted.")
    return redirect('/show')
@login_required(login_url='login')
def edit(request,id):
    employee=Employee.objects.get(id=id)
    messages.warning(request, "user edited.")
    return render(request,'edit.html',{'employee':employee})
@login_required(login_url='login')
def update(request,id):
    employee=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'edit.html',{'employee':employee})

def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'{username}, You are logged in.')
            return redirect("/")
        else:
            messages.info(request, 'Wrong passwrod or username')
            return redirect('login')
    return render(request, 'login.html')

def register_user(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account is created.')
            return redirect('login/')
        else:
            context = {'form': form}
            messages.info(request, 'Invalid credentials')
            return render(request, 'signup.html', context)

    context = {'form': form}
    return render(request, 'signup.html', context)

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.info(request, 'You logged out successfully')
    return redirect('login')
# def emp(request):
#     if request.method == "POST":
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('/show')
#             except:
#                 pass
#     else:
#         form = EmployeeForm()
#     return render(request,'index.html',{'form':form})