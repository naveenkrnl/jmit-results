from django.shortcuts import render
from .forms import EntryForm
from .models import ResultData

# Create your views here.
def home(request):
    context={}
    form = EntryForm(request.POST or None)
    if form.is_valid():
        userdata=form.cleaned_data['user']
        user=ResultData.objects.get(rollno=userdata)      
        context['user']=user
        return render(request,'result.html',context)
        # print(request.POST.get('user'))
        # print(request.POST.get('dob'))

        # obj = form.save(commit=False)
        # print(obj.title)
        # obj.title = "Some random title"
        # obj.publish = timezone.now()
        # obj.save()

    context['form']=form    
    return render(request, 'home.html', context)