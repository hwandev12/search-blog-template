from django.shortcuts import render
from .models import Candidate
from django.db.models import Q

def home(request):
    if 'q' in request.GET:
        search_key = request.GET['q']
        full_info = Q(Q(name__icontains=search_key) | Q(last_name__icontains=search_key) | Q(job__icontains=search_key))
        candidates = Candidate.objects.filter(full_info)
    else:
        candidates = Candidate.objects.all()
        
    context = {
        "candidates": candidates
    }
    
    return render(request, 'pages/index.html', context)
