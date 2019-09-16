from django.shortcuts import render,redirect,reverse
from apps.xfzauth.models import User
from django.views.generic import View
from django.contrib.auth.models import Group
from apps.xfzauth.decorators import xfz_superuser_required
from django.utils.decorators import method_decorator
from django.contrib import messages

@xfz_superuser_required
def staffs_view(request):
    staffs=User.objects.filter(is_staff=True)
    context={
        'staffs':staffs
    }
    return render(request,'cms/staffs.html',context=context)


@method_decorator(xfz_superuser_required,name='dispatch')
class AddStaffView(View):
    def get(self,request):
        groups=Group.objects.all()
        context={
            'groups':groups
        }
        return render(request,'cms/add_staff.html',context=context)

    def post(self,request):
        telephone=request.POST.get('telephone')
        user=User.objects.filter(telephone=telephone).first()
        if user:
            user.is_staff=True
            group_ids=request.POST.getlist('groups')
            groups=Group.objects.filter(pk__in=group_ids)
            user.groups.set(groups)
            user.save()
            return redirect(reverse('cms:staffs'))
        else:
            messages.info(request,'手机号码不存在')
            return redirect(reverse('cms:add_staff'))