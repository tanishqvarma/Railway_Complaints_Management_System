from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Complaint

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect('login')

    return render(request, 'register.html')



@login_required
def user_dashboard(request):
    if request.user.is_staff:
        return redirect('admin_dashboard')
    return render(request, 'user_dashboard.html')



@login_required
def add_complaint(request):
    if request.method == 'POST':
        Complaint.objects.create(
            user=request.user,
            pnr=request.POST.get('pnr'),
            complaint=request.POST.get('complaint'),
            urgency=request.POST.get('urgency'),
            cleanliness=request.POST.get('cleanliness'),
            working=request.POST.get('working'),
            status='Pending'
        )
        return redirect('my_complaints')

    return render(request, 'add_complaint.html')



@login_required
def my_complaints(request):
    data = Complaint.objects.filter(user=request.user)
    return render(request, 'my_complaints.html', {'data': data})


@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('login')

    if request.method == 'POST':
        cid = request.POST.get('id')
        status = request.POST.get('status')
        c = Complaint.objects.get(id=cid)
        c.status = status
        c.save()

    complaints = Complaint.objects.all()
    return render(request, 'admin_dashboard.html', {'complaints': complaints})



