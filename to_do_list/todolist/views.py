from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.
# a_row=Todo(thing='逛街',done=True)
# a_row.save() #保存
def home(request):  
    if request.method=="POST":
        if request.POST['back']=='':
            content={'list': Todo.objects.all(),'warning':'请输入内容' }
            return render(request, "home.html",content)
        else:
            a_row=Todo(thing=request.POST['back'],done=False)
            a_row.save()
            content={'list':Todo.objects.all()}
            return render(request, "home.html",content)
    else:
        content={'list':Todo.objects.all() }
        return render(request, "home.html",content)



def about(request):
    return render(request, "about.html")



def comp(request,ls_id): 
    if request.method=="POST":
        if request.POST['xiuwan']=='':
            content={'list': Todo.objects.all(),'warning':'请输入内容' }
            return render(request, "compile.html",content)
        else:
            a=Todo.objects.get(id=ls_id)
            a.thing=request.POST['xiuwan']
            a.save()
            return redirect("home")
    else:
        content ={'xiu':Todo.objects.get(id=ls_id).thing}
        return render(request, "compile.html",content)




def delet(request,ls_id):
    a=Todo.objects.get(id=ls_id)
    a.delete()
    return redirect("home")




def cross(request,ls_id):
    
    if request.POST['inp']=='a':
        c=Todo.objects.get(id=ls_id)
        c.done=False
        c.save()
      
    else:
        c=Todo.objects.get(id=ls_id)
        c.done=True
        c.save()
    return redirect("home")