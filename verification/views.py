from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def verify_nin(request):
    return render(request, "verification/verify_nin.html")