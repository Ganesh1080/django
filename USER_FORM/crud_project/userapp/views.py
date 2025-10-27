from django.shortcuts import render
from django.http import JsonResponse
from .models import UserForm
from .serializer import UserFormSerializer
from django.views.decorators.csrf import csrf_exempt
from .forms import UserFormModel
from django.shortcuts import render,redirect,get_object_or_404
# Create your views here.


@csrf_exempt
def user_register(request):
    if request.method=="POST":
        form=UserFormModel(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form=UserFormModel()
    return render(request,'userapp/register.html',{'form':form})

def user_details(request):
    users=UserForm.objects.all()
    return render(request,'userapp/list.html',{'users':users})

@csrf_exempt
def user_update(request,id):
    user=get_object_or_404(UserForm,id=id)
    if request.method == "POST":
        form=UserFormModel(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form=UserFormModel(instance=user)
    return render(request,'userapp/update.html',{"form":form})

def user_delete(request, id):
    user = get_object_or_404(UserForm, id=id)
    if request.method == "POST":
        user.delete()
        return redirect('list')
    return render(request, 'userapp/delete.html', {'user': user})