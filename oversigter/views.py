from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


@login_required(login_url='login')
def oversigt(request):
  if request.user.is_staff:
    
    return render(request, 'oversigter/admin_oversigt.html')
  else:
    context = {'user': request.user}
    return render(request, 'oversigter/user_oversigt.html', context)