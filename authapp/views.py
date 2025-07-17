from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from authapp.models import Contact,Trainer,MembershipPlan,Enrollment,Gallery,Attendance

# Create your views here.
def Home(request):
    return render(request,"index.html")

def signup(request):
    if request.method=="POST":
        email=request.POST.get('email')
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        if len(username)!=10:
            messages.info(request,"Incorrect Phone Number")
            return redirect('/signup')
        
        if pass1!=pass2:
            messages.info(request,"Password does not match")
            return redirect('/signup')
        
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email Address already registered")
                return redirect('/signup')
        except Exception as identifier:
            pass

        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone Number already registered")
                return redirect('/signup')
        except Exception as identifier:
            pass

        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"User Created Successfully. PLease Login.")
        return redirect('/login')

    return render(request,"signup.html")

def handlelogin(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')
    
    return render(request,"handlelogin.html")

def handlelogout(request):
    logout(request)
    messages.success(request,"Logout Successful")
    return redirect('/login')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('num')
        desc=request.POST.get('desc')
        myquery=Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()
        messages.info(request,"Thanks for contacting us. We will get back to you soon.")
        return redirect('/contact')
    
    return render(request,"contact.html")

def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and try again.")
        return redirect('/login')
    Membership=MembershipPlan.objects.all()
    Trainers=Trainer.objects.all()
    context={"Membership":Membership, "Trainers":Trainers}
    if request.method=="POST":
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        gender=request.POST.get('gender') 
        phonenumber=request.POST.get('phonenumber')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        membershipplan=request.POST.get('membershipplan')
        trainer=request.POST.get('trainer')
        reference=request.POST.get('reference')
        query=Enrollment(FullName=fullname,Email=email,Gender=gender,PhoneNumber=phonenumber,DOB=dob,Address=address,SelectMembershipPlan=membershipplan,SelectTrainer=trainer,Reference=reference)
        query.save()
        messages.success(request,"Thanks for enrolling into our gym.")
        return redirect('/payment')
    return render(request,"enroll.html",context)

def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and try again.")
        return redirect('/login')
    user_phone=request.user
    #print(user_phone)
    posts=Enrollment.objects.filter(PhoneNumber=user_phone)
    #print(posts)
    attendance=Attendance.objects.filter(PhoneNumber=user_phone)
    context={"posts":posts, "attendance":attendance}
    return render(request,"profile.html",context)

def gallery(request):
    posts=Gallery.objects.all()
    context={"posts":posts}
    return render(request,"gallery.html",context)

def attendance(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and try again.")
        return redirect('/login')
    if request.method=="POST":
        name=request.POST.get('fullname')
        number=request.POST.get('phonenumber')
        workout=request.POST.get('workout')
        login=request.POST.get('logintime')
        logout=request.POST.get('logouttime')
        trainedby=request.POST.get('trainer')
        query=Attendance(Name=name,PhoneNumber=number,Login=login,Logout=logout,SelectWorkout=workout,TrainedBy=trainedby)
        query.save()
        messages.success(request,"Attendance applied successfully.")
        return redirect('/attendance')
    user_phone=request.user
    SelectTrainer=Trainer.objects.all()
    Enroll=Enrollment.objects.filter(PhoneNumber=user_phone)
    context={"SelectTrainer":SelectTrainer,"Enroll":Enroll}
    return render(request,"attendance.html",context)

def payment(request):
    user_phone=request.user
    Enroll=Enrollment.objects.filter(PhoneNumber=user_phone)
    #print(Enroll[1].SelectMembershipPlan)
    Membership=MembershipPlan.objects.filter(Plan=Enroll[0].SelectMembershipPlan)
    #print(Membership)
    plan=Membership[0].Plan
    price=Membership[0].Price
    context={"plan":plan,"price":price}
    return render(request,"payment.html",context)
