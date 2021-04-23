from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from apps.job.models import Application,Job
from .models import ConversationMessage
from apps.notification.utilities import create_notification
# Create your views here.

#usamos un decorador para checkear si esta logueado o no
@login_required
def dashboard(request):
    return render(request,'userprofile/dashboard.html',{'userprofile':request.user.userprofile})

@login_required
def view_application(request,application_id):
    if request.user.userprofile.is_employer:
        application=get_object_or_404(Application,pk=application_id, job__created_by=request.user)
        to_user=application.created_by
    else:
        application=get_object_or_404(Application,pk=application_id, created_by=request.user)
        to_user=application.job.created_by

    if request.method=="POST":
        content=request.POST.get('content')
        if content:
            conversationmessage=ConversationMessage.objects.create(application=application,content=content,created_by=request.user)
            create_notification(request, to_user,'message',extra_id=application.id)

            return redirect('view_application',application_id=application_id)

    return render(request,'userprofile/view_application.html',{'application':application})

@login_required
def view_dashboard_job(request,job_id):
    job=get_object_or_404(Job,pk=job_id,created_by=request.user)

    return render(request, 'userprofile/view_dashboard_job.html',{'job':job})

