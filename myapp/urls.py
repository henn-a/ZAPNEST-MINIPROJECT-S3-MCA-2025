"""EV_Charging URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [




        path('adminhome/',views.adminhome),
        path('login_get/',views.login_get),
        path('logout/',views.logout),


        path('c_registration/',views.c_registration),
        path('c_registration_post/',views.c_registration_post),


        path('add_category/',views.add_category),
        path('add_category_post/',views.add_category_post),
        path('deletecategory/<id>/',views.deletecategory),

        path('add_publicstation/',views.add_publicstation),
        path('add_publicstation_post/',views.add_publicstation_post),
        path('view_publicstation/',views.view_publicstation),
        path('edit_publicstation/<id>/',views.edit_publicstation),
        path('edit_publicsation_post/',views.edit_publicsation_post),
        path('delete_worker/<id>',views.delete_worker),
        path('delete_publication/<id>/',views.delete_publication),

        path('sendreply/<id>',views.sendreply),
        path('sendreply_post/',views.sendreply_post),

        path('verify_chargingstation/',views.verify_chargingstation),
        path('verify_workers/',views.verify_workers),

        path('accept_workers/<id>/',views.accept_workers),
        path('reject_worker/<id>/',views.reject_worker),

        path('accept_charging_station/<id>/',views.accept_charging_station),
        path('reject_charging_station/<id>/',views.reject_charging_station),
        path('view_category/',views.view_category),
        path('view_complaint/',views.view_complaint),
        path('view_feedback/',views.view_feedback),
        path('view_user/',views.view_user),




        ####################CHARGING_STATION###############




        path('charginstationhome/',views.charginstationhome),
        path('viewprofile/',views.viewprofile),
        path('edit_profile/',views.edit_profile),
        path('edit_profile_post/',views.edit_profile_post),

        path('addworkers/',views.addworkers),
        path('addworkers_post/',views.addworkers_post),
        path('editworker/<id>/',views.editworker),
        path('editworker_post/',views.editworker_post),
        path('viewworkers/',views.viewworkers),
        path('viewuser/',views.viewuser),
        path('addslot/',views.addslot),
        path('addslot_post/',views.addslot_post),
        path('view_slot/',views.view_slot),
        path('edit_slot/<id>',views.edit_slot),
        path('delete_slot/<id>',views.delete_slot),
        path('edit_slot_post/',views.edit_slot_post),

        path('chat_c/<id>',views.chat_c),
        path('chat_view_c/',views.chat_view_c),
        path('chat_send_c/<msg>',views.chat_send_c),
        path('EV_sendchat/',views.EV_sendchat),
        path('EV_viewchat/',views.EV_viewchat),
        path('view_evfeeback/',views.view_evfeeback),



        path('viewslotbookingandpayment/',views.viewslotbookingandpayment),





        path('addcatogery/',views.addcatogery),


        path('assign_requesttorwork/<id>',views.assign_requesttorwork),
        path('assign_requesttorwork_post/',views.assign_requesttorwork_post),
        path('editworker/',views.editworker),
        path('send_feedback/',views.send_feedback),
        path('viewfeedback/',views.viewfeedback),
        path('send_feedback_post/',views.send_feedback_post),
        path('viewservicerequest/',views.viewservicerequest),




        #################USER#################################

        path('userhome/',views.userhome),
        path('add_servicerequest/<id>',views.add_servicerequest),
        path('add_servicerequest_post/',views.add_servicerequest_post),
        path('view_chargingslot/<id>',views.view_chargingslot),
        path('sendfeedback/',views.sendfeedback),
        path('sendfeedbackpost/',views.sendfeedbackpost),
        path('send_complaint/',views.send_complaint),
        path('send_complaint_post/',views.send_complaint_post),
        path('viewcomplaint/',views.viewcomplaint),
        path('view_chargingstation/',views.view_chargingstation),
        path('user_registration/',views.user_registration),
        path('user_registration_post/',views.user_registration_post),
        path('view_servicerequest/',views.view_servicerequest),
        path('book_slot/<id>/',views.book_slot),
        path('send_evfeedback/<id>',views.send_evfeedback),
        path('send_evfeedback_post/',views.send_evfeedback_post),
        path('editprofile/',views.editprofile),
        path('editprofile_post/',views.editprofile_post),


        path('chat/<id>',views.chat),
        path('chat_view/',views.chat_view),
        path('chat_send/<msg>',views.chat_send),
        path('User_sendchat/',views.User_sendchat),
        path('User_viewchat/',views.User_viewchat),


        path('view_profile/',views.view_profile),
        path('raz_pay/<id>',views.raz_pay),








        # path('sendreply/',views.sendreply),
        # path('sendreply_post/',views.sendreply_post),

]
