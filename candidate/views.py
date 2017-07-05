from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewCandidateForm
from django.utils import timezone
from .models import Candidate
from django.contrib.auth.decorators import login_required



def applicant_tracker(request):
    candidateList = Candidate.objects.filter(deactivated_date=None)
    return render(request, 'applicanttracker.html', {'candidateList' : candidateList } )

def add_candidate(request):
    if request.method =='POST':
        form = NewCandidateForm(request.POST, request.FILES)
        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.manager = request.user
            candidate.interview_stage = 0
            candidate.save()
            return redirect(candidate_detail, candidate.pk)
    else:
        form = NewCandidateForm()
    return render(request, 'candidateform.html', {'form': form})

def candidate_detail(request, id):
    """
    Create a view that return a single
    Post object based on the post ID and
    and render it to the 'postdetail.html'
    template. Or return a 404 error if the
    post is not found
    """
    candidate = get_object_or_404(Candidate, pk=id)
    return render(request, "candidatedetail.html", {'candidate': candidate})

def deactivate_candidate(request, id):
    candidate = get_object_or_404(Candidate, pk=id)
    candidate.deactivated_date = timezone.now()
    candidate.save()
    return render(request, "candidatedetail.html", {'candidate': candidate})

def activate_candidate(request, id):
    candidate = get_object_or_404(Candidate, pk=id)
    candidate.deactivated_date = None
    candidate.save()
    return render(request, "candidatedetail.html", {'candidate': candidate})


def edit_candidate(request, id):
    candidate = get_object_or_404(Candidate, pk=id)
    if request.method =='POST':
        form = NewCandidateForm(request.POST, request.FILES, instance=candidate)
        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.manager = request.user
            candidate.save()
            return redirect(candidate_detail, candidate.pk)
    else:
       form = NewCandidateForm(instance=candidate)
    return render(request, 'candidateform.html', {'form': form, 'candidate': candidate})
