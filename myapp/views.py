from django.shortcuts import render

# Create your views here.
def task(regform):
    task = task.myapp()
    if request.method == 'POST':
        task = task.myapp(request.POST)
        html = 'we have receive this task again'

    else:
        html = 'welcomefor the first time'

def myapp(regapp)
    return render(request, 'bus.html',{'html': html, 'task': task})