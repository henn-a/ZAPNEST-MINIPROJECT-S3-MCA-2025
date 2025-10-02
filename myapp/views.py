import datetime
import email

from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group

# Create your views here.
from myapp.models import *

################LOGIN###################

#
# def login_get(request):
#     if request.method=="POST":
#         username=request.POST['username']
#         password=request.POST['password']
#         user=authenticate(request,username=username,password=password)
#         if user is not None:
#             if user.groups.filter(name="admin").exists():
#                 login(request,user)
#                 return redirect('/myapp/adminhome/')
#             elif user.groups.filter(name="Station").exists():
#                 login(request,user)
#                 # k=Charging_Station_table.objects.get(LOGIN__id=user.id)
#                 # request.session['chid']=k.id
#                 return redirect('/myapp/charginstationhome/')
#             elif user.groups.filter(name="user").exists():
#                 login(request,user)
#                 return redirect('/myapp/userhome/')
#             else:
#                 return redirect('/myapp/login_get')
#     # messages.error(request, 'Invalid username or password')
#     return render(request,'loginpage.html')




from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_get(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.groups.filter(name="admin").exists():
                return redirect('/myapp/adminhome/')
            elif user.groups.filter(name="Station").exists():
                # Example: Store station ID in session if needed
                # station = Charging_Station_table.objects.get(LOGIN__id=user.id)
                # request.session['chid'] = station.id
                return redirect('/myapp/charginstationhome/')
            elif user.groups.filter(name="user").exists():
                return redirect('/myapp/userhome/')
            else:
                messages.error(request, "Unauthorized access: No valid group assigned.")
                return redirect('/myapp/login_get/')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('/myapp/login_get/')

    return render(request,'login_page.html')




####################LOGOUT##########################

def logout(request):
    auth.logout(request)
    return render(request,'login_page.html')

####################REGISTRATION#########################



################ADMINHOME######################

def adminhome(request):
    return render(request,'admin/adminhome.html')

@login_required(login_url='/myapp/login_get/')

def add_category(request):
    return render(request,'admin/add_category.html')

@login_required(login_url='/myapp/login_get/')

def add_category_post(request):
    category=request.POST['category']
    # date=request.POST['date']

    obj=Category_table()
    obj.category_type=category
    obj.date=datetime.datetime.today()
    obj.save()
    return redirect('/myapp/view_category')
@login_required(login_url='/myapp/login_get/')
def view_category(request):
    a=Category_table.objects.all()
    return render(request,'admin/view_category.html',{'data':a})

@login_required(login_url='/myapp/login_get/')
def deletecategory(request,id):
    a=Category_table.objects.get(id=id)
    a.delete()
    return redirect('/myapp/view_category')

@login_required(login_url='/myapp/login_get/')
def add_publicstation(request):
    return render(request,'admin/add_public_station.html')


# def add_publicstation_post(request):
#     name=request.POST['name']
#     contact=request.POST['phone']
#     type=request.POST['type']
#     latitude=request.POST['latitude']
#     longitude=request.POST['longitude']
#
#     ob=public_station_table()
#     ob.name=name
#     ob.phone=contact
#     ob.type=type
#     ob.latitude=latitude
#     ob.longitude=longitude
#     ob.save()
#
#     return redirect('/myapp/view_publicstation')


@login_required(login_url='/myapp/login_get/')
def add_publicstation_post(request):
    name = request.POST['name']
    contact = request.POST['phone']
    type = request.POST['type']
    latitude = float(request.POST['latitude'])  # Convert to float
    longitude = float(request.POST['longitude'])  # Convert to float

    ob = public_station_table()
    ob.name = name
    ob.phone = contact
    ob.type = type
    ob.latitude = latitude
    ob.longitude = longitude
    ob.save()

    return redirect('/myapp/view_publicstation')

@login_required(login_url='/myapp/login_get/')
def view_publicstation(request):
    ab=public_station_table.objects.filter()

    return render(request,'admin/view_public_station.html',{'data':ab})

@login_required(login_url='/')
def edit_publicstation(request,id):
    ab=public_station_table.objects.get(id=id)
    request.session['id']=id
    return render(request,'admin/edit_publicstation.html',{'data':ab})

@login_required(login_url='/myapp/login_get/')
def edit_publicsation_post(request):
    name = request.POST['name']
    contact = request.POST['phone']
    type = request.POST['type']
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']

    ob = public_station_table.objects.get(id=request.session['id'])
    ob.name = name
    ob.phone = contact
    ob.type = type
    ob.latitude = latitude
    ob.longitude = longitude
    ob.save()
    return redirect('/myapp/view_publicstation/')

@login_required(login_url='/myapp/login_get/')
def delete_publication(request,id):
    a = public_station_table.objects.get(id=id)
    a.delete()
    return redirect('/myapp/view_publicstation')
#
#
# def send_reply(request,id):
#     return render(request,'admin/send_reply.html')
#
# def send_reply_post(request):
#     reply=request.POST['reply']
#     ob=Complaint_table()
#     ob.Reply=reply
#     return render(request,'admin/send_reply.html',{'data':ob})

@login_required(login_url='/myapp/login_get/')
def verify_chargingstation(request):
    ab=Charging_Station_table.objects.all()
    return render(request,'admin/verify_charging_station.html',{'data':ab})

@login_required(login_url='/myapp/login_get/')
def accept_charging_station(request,id):
    ob=Charging_Station_table.objects.get(id=id)
    ob.status="accepted"
    ob.save()
    return redirect('/myapp/verify_chargingstation/')


@login_required(login_url='/myapp/login_get/')
def reject_charging_station(request,id):
    ob=Charging_Station_table.objects.get(id=id)
    ob.status="rejected"
    ob.save()
    return redirect('/myapp/verify_chargingstation')

@login_required(login_url='/myapp/login_get/')
def verify_workers(request):
    ab=Worker_table.objects.all()
    return render(request,'admin/verify_workers.html',{'data':ab})

@login_required(login_url='/myapp/login_get/')
def accept_workers(request,id):
    ob=Worker_table.objects.get(id=id)
    ob.status="accepted"
    ob.save()
    return redirect('/myapp/verify_workers')


@login_required(login_url='/myapp/login_get/')
def reject_worker(request,id):
    ob=Worker_table.objects.get(id=id)
    ob.status="rejected"
    ob.save()
    return redirect('/myapp/verify_workers')

@login_required(login_url='/myapp/login_get/')
def view_complaint(request):
    ab=Complaint_table.objects.all()
    return render(request,'admin/view_complaint.html',{'data':ab})

@login_required(login_url='/myapp/login_get/')
def sendreply(request,id):
    request.session['rid']=id
    return render(request,'admin/send_reply.html')


@login_required(login_url='/myapp/login_get/')
def sendreply_post(request):
    reply=request.POST['reply']
    Complaint_table.objects.filter(id=request.session['rid']).update(Reply=reply)
    return redirect('/myapp/view_complaint/')


# def view_feedback(request):
#     a=Feedback_table.objects.all()
#     l=[]
#     for i in a:
#         u=User_table.objects.get(LOGIN=i.LOGIN.id)
#         l.append({'feedback':i.feedback,'date':i.date,'name':u.name})
#         u=Charging_Station_table.objects.get(LOGIN=i.LOGIN.id)
#         l.append({'feedback':i.feedback,'date':i.date,'name':u.name})
#
#     return render(request,'admin/view_feeeback.html',{'data':a})
@login_required(login_url='/myapp/login_get/')
def view_feedback(request):
    feedback_entries = Feedback_table.objects.all()
    feedback_list = []

    for entry in feedback_entries:
        login_id = entry.LOGIN.id
        name = "Unknown"

        if User_table.objects.filter(LOGIN=login_id).exists():
            name = User_table.objects.get(LOGIN=login_id).name
        elif Charging_Station_table.objects.filter(LOGIN=login_id).exists():
            name = Charging_Station_table.objects.get(LOGIN=login_id).name

        feedback_list.append({
            'feedback': entry.feedback,
            'date': entry.date,
            'name': name,
        })

    return render(request, 'admin/view_feeeback.html', {'data': feedback_list})

@login_required(login_url='/myapp/login_get/')
def view_user(request):
    ab=User_table.objects.all()
    return render(request,'admin/view_user.html',{'data':ab})



##################CHARGINGSTATION######################

def c_registration(request):
    return render(request,'registration.html')

def c_registration_post(request):
    name=request.POST['name']
    place=request.POST['place']
    contact=request.POST['contact']
    latitude=request.POST['latitude']
    longitude=request.POST['longitude']
    username=request.POST['username']
    password=request.POST['password']

    user = User.objects.create(username=username, password=make_password(password), first_name=name, email=email)
    user.save()
    user.groups.add(Group.objects.get(name='Station'))

    ob=Charging_Station_table()
    ob.name=name
    ob.place=place
    ob.contact=contact
    ob.latitude=latitude
    ob.longitude=longitude
    ob.LOGIN = user
    ob.status='pending'
    ob.save()
    return redirect('/myapp/login_get/')

@login_required(login_url='/myapp/login_get/')
def viewprofile(request):
    a = Charging_Station_table.objects.get(LOGIN=request.user.id)
    return render(request,'charging_station/view_profile.html', {'data': a})

@login_required(login_url='/')
def edit_profile(request):
    ab = Charging_Station_table.objects.get(LOGIN=request.user.id)
    return render(request, 'charging_station/edit_profile.html', {'data': ab})

@login_required(login_url='/myapp/login_get/')
def edit_profile_post(request):
    name = request.POST['name']
    place = request.POST['place']
    contact = request.POST['contact']
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']

    ob = Charging_Station_table.objects.get(LOGIN=request.user.id)

    ob.name = name
    ob.place = place
    ob.contact = contact
    ob.latitude = latitude
    ob.longitude = longitude

    ob.save()

    return redirect('/myapp/viewprofile/')

@login_required(login_url='/myapp/login_get/')
def charginstationhome(request):
    return render(request,'charging_station/chargingstationhome.html')

@login_required(login_url='/myapp/login_get/')

def addworkers(request):
    return render(request,'charging_station/add_workers.html')

@login_required(login_url='/myapp/login_get/')
def addworkers_post(request):
    # CHARGE_STATION=request.POST['charging_station']
    name=request.POST['name']
    phone=request.POST['phone']
    email=request.POST['email']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']

    obj=Worker_table()

    obj.CHARGE_STATION=Charging_Station_table.objects.get(LOGIN=request.user.id)
    obj.name=name
    obj.phone=phone
    obj.email=email
    obj.place=place
    obj.post=post
    obj.pin=pin
    obj.status='pending'

    obj.save()

    return redirect('/myapp/viewworkers/')


@login_required(login_url='/myapp/login_get/')
def editworker(request,id):
    ab=Worker_table.objects.get(id=id)
    request.session['id']=id
    return render(request,'charging_station/edit_workers.html',{'data':ab})


@login_required(login_url='/myapp/login_get/')
def editworker_post(request):
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']

    obj = Worker_table.objects.get(id=request.session['id'])

    obj.CHARGE_STATION = Charging_Station_table.objects.get(LOGIN=request.user.id)

    obj.name = name
    obj.phone = phone
    obj.email = email
    obj.place = place
    obj.post = post
    obj.pin = pin

    obj.save()

    return redirect('/myapp/viewworkers/')


@login_required(login_url='/myapp/login_get/')
def delete_worker(request,id):
    a = Worker_table.objects.get(id=id)
    a.delete()
    return redirect('/myapp/viewworkers')

@login_required(login_url='/myapp/login_get/')
def viewworkers(request):
    b=Worker_table.objects.filter(CHARGE_STATION__LOGIN__id=request.user.id)
    return render(request,'charging_station/view_workers.html',{'data':b})

@login_required(login_url='/myapp/login_get/')
def assign_requesttorwork(request,id):
    ob=Worker_table.objects.all()
    request.session['rid']=id
    return render(request, 'charging_station/assign_request_to_worker.html',{'id':id,'data':ob})

@login_required(login_url='/myapp/login_get/')
def assign_requesttorwork_post(request):
    work=request.POST['work']
    ob=Assign_service_table.objects.all()
    ob.WORKER=work
    ob.REQUEST_id=request.session['rid']
    ob.date=datetime.datetime.now()

    a=Service_request.objects.filter(id=request.session['rid']).update(status='assigned')
    return redirect('/myapp/viewservicerequest/')


@login_required(login_url='/myapp/login_get/')
def send_feedback(request):
    return render(request,'charging_station/send_feedback.html')

@login_required(login_url='/')
def send_feedback_post(request):
    feedback=request.POST['feedback']
    # date=request.POST['date']
    obj=Feedback_table()
    obj.LOGIN=User.objects.get(id=request.user.id)
    obj.feedback=feedback
    obj.date=datetime.datetime.now()
    obj.save()
    return redirect('/myapp/viewfeedback/#about')

@login_required(login_url='/myapp/login_get/')
def viewfeedback(request):
    ab=Feedback_table.objects.filter(CHARGE_STATION__LOGIN__id=request.user.id)
    return render(request,'charging_station/view_feedback.html',{'data':ab})

@login_required(login_url='/myapp/login_get/')
def viewservicerequest(request):
    ab=Service_request.objects.filter(CHARGING_STATION__LOGIN__id=request.user.id)
    return render(request,'charging_station/view_servicerequest.html',{'data':ab})

@login_required(login_url='/myapp/login_get/')
def viewuser(request):
    ab=User_table.objects.filter(LOGIN_id=request.user.id)
    return render(request,'charging_station/view_user.html',{'data':ab})

@login_required(login_url='/myapp/login_get/')
def addslot(request):
    return render(request,'charging_station/addchargingslot.html')

@login_required(login_url='/myapp/login_get/')
def view_slot(request):
    ab=Charging_slot_table.objects.filter(CHARGING_STATION__LOGIN_id=request.user.id)
    return render(request,'charging_station/view_charging_slot.html',{'data':ab})


@login_required(login_url='/myapp/login_get/')
def addslot_post(request):
    slot=request.POST['slot']
    status='pending'
    start_time=request.POST['start']
    endtime=request.POST['endtime']
    ob=Charging_slot_table()
    ob.CHARGING_STATION = Charging_Station_table.objects.get(LOGIN=request.user.id)
    ob.slot_number=slot
    ob.status=status
    ob.start_time=start_time
    ob.end_time=endtime
    ob.save()
    return redirect('/myapp/view_slot/')




@login_required(login_url='/myapp/login_get/')
def edit_slot(request,id):
    ab=Charging_slot_table.objects.get(id=id)
    request.session['id']=id
    return render(request,'charging_station/edit_slot.html',{'data':ab})


@login_required(login_url='/myapp/login_get/')
def edit_slot_post(request):
    slot_number = request.POST['slot']
    start_time = request.POST['start']
    end_time = request.POST['endtime']


    obj = Charging_slot_table.objects.get(id=request.session['id'])

    obj.slot_number=slot_number
    obj.start_time=start_time
    obj.end_time=end_time
    obj.save()

    return redirect('/myapp/view_slot/')



@login_required(login_url='/myapp/login_get/')
def delete_slot(request,id):
    a = Charging_slot_table.objects.get(id=id)
    a.delete()
    return redirect('/myapp/view_slot/')


@login_required(login_url='/myapp/login_get/')
def addcatogery(request):
    return render(request,'charging_station/add_cateogry.html')

@login_required(login_url='/myapp/login_get/')
def viewslotbookingandpayment(request):
    ob=Charging_slot_booking_table.objects.filter(SLOT__CHARGING_STATION__LOGIN_id=request.user.id)
    l=[]
    for i in ob:
        res=Charging_slot_booking_table.objects.get(SLOT_id=i.SLOT.id)
        l.append({
            'booking_date':i.booking_date,
            'status':i.status,
                  'name':i.USER.name,
                  'LOGIN':i.USER.LOGIN.id,
                  'phone':i.USER.phone,
                  'slot_number':i.SLOT.slot_number,

            'payment': res.status,
            'amount': '200'


                  })
    return render(request,'charging_station/viewslot_booking_and_paymentstatus.html',{'data':l})


@login_required(login_url='/myapp/login_get/')
def view_evfeeback(request):
    ob=Charging_station_feedback_table.objects.filter(CHARGING_STATION__LOGIN__id=request.user.id)
    return render(request,'charging_station/view_evfeedback.html',{'data':ob})


##############user############################


def userhome(request):
    return render(request,'user/user_home.html')


def user_registration(request):
    return render(request,'user/user_registration.html')


def user_registration_post(request):
    name=request.POST['name']
    email=request.POST['email']
    phone=request.POST['contact']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    username=request.POST['username']
    password=request.POST['password']


    user = User.objects.create(username=username, password=make_password(password), first_name=name, email=email)
    user.save()
    user.groups.add(Group.objects.get(name='user'))


    ob=User_table()
    ob.name=name
    ob.email=email
    ob.phone=phone
    ob.place=place
    ob.post=post
    ob.pin=pin
    ob.LOGIN = user
    ob.status='pending'
    ob.save()
    return redirect('/myapp/login_get')

@login_required(login_url='/myapp/login_get/')
def add_servicerequest(request,id):
    request.session['sid']=id
    return render(request,'user/send_servicerequest.html',{'id':id})

@login_required(login_url='/myapp/login_get/')
def add_servicerequest_post(request):
    service=request.POST['service']
    # date=request.POST['date']
    ob=Service_request()
    ob.service=service
    ob.CHARGING_STATION_id=request.session['sid']
    ob.date=datetime.datetime.now()
    ob.status='pending'
    ob.USER=User_table.objects.get(LOGIN=request.user.id)
    ob.save()
    return redirect('/myapp/view_chargingstation/')
#
# @login_required(login_url='/myapp/login_get/')
# def view_chargingslot(request,id):
#     b=Charging_slot_table.objects.filter(CHARGING_STATION_id=id)
#     print(b,"kkkkkkkkkkkkkkkk")
#     l=[]
#     for i in b:
#         res = Charging_slot_booking_table.objects.filter(SLOT_id=i.id)
#         print(res,""""""""""""""""''""""")
#         l.append({
#             'name': i.CHARGING_STATION.name,
#             # 'status': i.status,
#             'slot_number': i.slot_number,
#             'LOGIN': i.CHARGING_STATION.LOGIN.id,
#             'end_time': i.end_time,
#             'start_time': i.start_time,
#             'payment': res.status,
#             # 'amount': '200'
#
#         })
#
#     return render(request,'user/view_charging_slot.html',{'data':l})
#

def view_chargingslot(request,id):
    request.session['cid']=id
    b = Charging_slot_table.objects.filter(CHARGING_STATION__id=id)
    print(b,"jjjjjj")
    l = []

    for i in b:
        # Get the first booking for this slot (or None if not found)
        res = Charging_slot_booking_table.objects.filter(SLOT_id=i.id).first()
        # Safely handle cases where there's no booking
        payment_status = res.status if res else "Not Booked"

        l.append({
            'name': i.CHARGING_STATION.name,
            'slot_number': i.slot_number,
            'LOGIN': i.CHARGING_STATION.LOGIN.id,
            'end_time': i.end_time,
            'start_time': i.start_time,
            'status': i.status,
            'payment': payment_status,
            'amount': '200',
            'sid': i.id
        })

    return render(request, 'user/view_charging_slot.html', {'data': l})


@login_required(login_url='/myapp/login_get/')
def book_slot(request,id):
    print("hhhhhhhhhhhhhhhhh")
    ob=Charging_slot_booking_table()
    ob.status='Booked'
    ob.SLOT=Charging_slot_table.objects.get(id=id)
    ob.USER=User_table.objects.get(LOGIN=request.user.id)
    ob.booking_date=datetime.datetime.now()
    ob.save()
    k=Charging_slot_table.objects.get(id=id)
    k.status='Booked'
    k.save()
    b= request.session['cid']
    # a = Charging_slot_table.objects.filter(id=id).update(status='Booked')
    # b=request.session['cid']
    return redirect(f'/myapp/view_chargingslot/{b}')

@login_required(login_url='/myapp/login_get/')
def send_complaint(request):
    return render(request, 'user/sendcomplaint.html')


@login_required(login_url='/myapp/login_get/')
def send_complaint_post(request):
    complaint=request.POST['complaint']
    ob=Complaint_table()
    ob.USER = User_table.objects.get(LOGIN=request.user.id)
    ob.complaint=complaint
    ob.reply='pending'
    ob.date=datetime.datetime.now()
    ob.save()
    return redirect('/myapp/viewcomplaint/')


@login_required(login_url='/myapp/login_get/')
def viewcomplaint(request):
    ab=Complaint_table.objects.all()
    return render(request,'user/view_complaint.html',{'data':ab})

# def sendreply(request):
#     return render(request,'user/send_reply.html')
#
# def sendreply_post(request):
#     Reply=request.POST['Reply']
#     date=request.POST['date']
#     ob=Complaint_table()
#     ob.Reply=Reply
#     ob.date=date
#     ob.save()
#     return redirect('/myapp/viewcomplaint/')

@login_required(login_url='/myapp/login_get/')
def sendfeedback(request):
    return render(request,'user/sendfeedback.html')


@login_required(login_url='/myapp/login_get/')
def sendfeedbackpost(request):
    feedback=request.POST['feedbackk']
    # date=request.POST['date']
    obj=Feedback_table()
    obj.LOGIN=User.objects.get(id=request.user.id)
    obj.feedback=feedback
    obj.date=datetime.datetime.now()
    obj.save()
    return redirect('/myapp/sendfeedback/')

@login_required(login_url='/myapp/login_get/')
def view_chargingstation(request):
    ab=Charging_Station_table.objects.all()
    print(ab,'============')
    return render(request, 'user/viewcharging_station.html', {'data':ab})

@login_required(login_url='/myapp/login_get/')
def view_servicerequest(request):
    ab=Service_request.objects.filter(USER__LOGIN__id=request.user.id)
    return render(request,'user/view_servicerequest.html',{'data':ab})

@login_required(login_url='/myapp/login_get/')
def send_evfeedback(request,id):
    request.session['id'] = id
    return render(request,'user/send_ev_feedback.html',{'id':id})



#
# def send_evfeedback_post(request):
#     feedback=request.POST['feedback']
#     # date=request.POST['date']
#     rating=request.POST['rating']
#
#     ob=Charging_station_feedback_table()
#     ob.USER = User_table.objects.get(LOGIN=request.user.id)
#     ob.CHARGING_STATION_id = request.session['id']
#
#     ob.feedback=feedback
#     ob.date=datetime.datetime.now()
#     ob.rating=rating
#     ob.save()
#     return HttpResponse("ok")

@login_required(login_url='/myapp/login_get/')
def send_evfeedback_post(request):
    if request.method == "POST":
        feedback = request.POST['feedback']
        ob = Charging_station_feedback_table()
        ob.USER = User_table.objects.get(LOGIN=request.user.id)
        ob.CHARGING_STATION_id = request.session['id']
        ob.feedback = feedback
        ob.date = datetime.datetime.now()
        ob.save()

        b = request.session['id']
        return redirect(f'/myapp/send_evfeedback/{b}')

@login_required(login_url='/myapp/login_get/')
def view_profile(request):
    a=User_table.objects.get(LOGIN=request.user.id)
    return render(request,'user/view_profile.html',{'data':a})

@login_required(login_url='/myapp/login_get/')
def editprofile(request):
    ab = User_table.objects.get(LOGIN=request.user.id)
    return render(request, 'user/edit_profile.html', {'data': ab})
@login_required(login_url='/myapp/login_get/')
def editprofile_post(request):
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    place = request.POST['address']
    post = request.POST['address']
    pin = request.POST['address']

    obj = User_table.objects.get(LOGIN=request.user.id)

    obj.name = name
    obj.phone = phone
    obj.email = email
    obj.place = place
    obj.post = post
    obj.pin = pin

    obj.save()

    return redirect('/myapp/view_profile/')


@login_required(login_url='/myapp/login_get/')
def chat(request,id):
    request.session["userid"] = id
    cid = str(request.session["userid"])
    request.session["new"] = cid
    qry = User_table.objects.get(LOGIN=cid)

    return render(request, "charging_station/Chat.html", {'photo': '/static/pic.png', 'name': qry.name, 'toid': cid})

@login_required(login_url='/myapp/login_get/')
def chat_view(request):
    fromid = request.user.id
    toid = request.session["userid"]
    qry = User_table.objects.get(LOGIN=request.session["userid"])
    from django.db.models import Q

    res = Chat_table.objects.filter(Q(from_id_id=fromid, To_id_id=toid) | Q(from_id_id=toid, To_id_id=fromid)).order_by('id')
    l = []

    for i in res:
        l.append({"id": i.id, "message": i.message, "to": i.To_id_id, "date": i.date, "from": i.from_id_id})

    return JsonResponse({'photo': '/static/pic.png', "data": l, 'name': qry.name, 'toid': request.session["userid"]})

@login_required(login_url='/myapp/login_get/')
def chat_send(request, msg):
    lid = request.user.id
    toid = request.session["userid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat_table()
    chatobt.message = message
    chatobt.To_id_id = toid
    chatobt.from_id_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})

@login_required(login_url='/myapp/login_get/')
def User_sendchat(request):
    FROM_id=request.POST['from_id']
    TOID_id=request.POST['to_id']
    msg=request.POST['message']

    from  datetime import datetime
    c=Chat_table()
    c.from_id_id=FROM_id
    c.To_id_id=TOID_id
    c.message=msg
    c.date=datetime.now()
    c.save()
    return JsonResponse({'status':"ok"})

@login_required(login_url='/myapp/login_get/')
def User_viewchat(request):
    fromid = request.POST["from_id"]
    toid = request.POST["to_id"]
    # lmid = request.POST["lastmsgid"]
    from django.db.models import Q

    res = Chat_table.objects.filter(Q(from_id_id=fromid, To_id_id=toid) | Q(from_id_id=toid, To_id_id=fromid)).order_by('id')
    l = []

    for i in res:
        l.append({"id": i.id, "msg": i.message, "from": i.from_id_id, "date": i.date, "to": i.To_id_id})

    return JsonResponse({"status":"ok",'data':l})






@login_required(login_url='/myapp/login_get/')
def chat_c(request,id):
    request.session["seid"] = id
    cid = str(request.session["seid"])
    # request.session["new"] = cid
    qry = Charging_Station_table.objects.get(LOGIN=cid)

    return render(request, "user/Chat.html", {'photo': '/static/pic.png', 'name': qry.name, 'toid': cid})

@login_required(login_url='/myapp/login_get/')
def chat_view_c(request):
    fromid = request.user.id
    toid = request.session["seid"]
    print(fromid,toid,"nnnnnnnnnn")
    qry = Charging_Station_table.objects.get(LOGIN__id=request.session["seid"])
    from django.db.models import Q

    res = Chat_table.objects.filter(Q(from_id_id=fromid, To_id_id=toid) | Q(from_id_id=toid, To_id_id=fromid)).order_by('id')
    l = []

    for i in res:
        l.append({"id": i.id, "message": i.message, "to": i.To_id.id, "date": i.date, "from": i.from_id.id})

    return JsonResponse({'photo': '/static/pic.png', "data": l, 'name': qry.name, 'toid': request.session["seid"]})


@login_required(login_url='/myapp/login_get/')
def chat_send_c(request,msg):
    lid = request.user.id
    toid = request.session["seid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat_table()
    chatobt.message = message
    chatobt.To_id_id = toid
    chatobt.from_id_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})

@login_required(login_url='/myapp/login_get/')
def EV_sendchat(request):
    FROM_id=request.POST['from_id']
    TOID_id=request.POST['to_id']
    msg=request.POST['message']

    from  datetime import datetime
    c=Chat_table()
    c.from_id_id=FROM_id
    c.To_id_id=TOID_id
    c.message=msg
    c.date=datetime.now()
    c.save()
    return JsonResponse({'status':"ok"})

@login_required(login_url='/myapp/login_get/')
def EV_viewchat(request):
    fromid = request.POST["from_id"]
    toid = request.POST["to_id"]
    # lmid = request.POST["lastmsgid"]
    from django.db.models import Q

    res = Chat_table.objects.filter(Q(from_id_id=fromid, To_id_id=toid) | Q(from_id_id=toid, To_id_id=fromid)).order_by('id')
    l = []

    for i in res:
        l.append({"id": i.id, "msg": i.message, "from": i.from_id_id, "date": i.date, "to": i.To_id_id})

    return JsonResponse({"status":"ok",'data':l})



#####################payment#######################################
@login_required(login_url='/myapp/login_get/')
def raz_pay(request,id):
    import razorpay
    razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
    razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

    razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

    amount = 200
    amount= float(amount)*100

    # Create a Razorpay order (you need to implement this based on your logic)
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1',  # Auto-capture payment
    }
    k=Charging_slot_booking_table.objects.get(id=id)
    k.status='paid'
    k.save()
    l=Charging_slot_table.objects.get(id=k.SLOT.id)
    l.status='paid'
    l.save()
    # Create an order
    order = razorpay_client.order.create(data=order_data)

    context = {
        'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],
    }

    obj = Payment()
    obj.BOOKING_id = id
    obj.date = datetime.datetime.now().today()
    obj.amount = float(amount)
    obj.status = 'paid'
    obj.save()

    Charging_slot_booking_table.objects.filter(id=id).update(status='paid')

    return render(request, 'user/payment.html',{ 'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],"id":id})






