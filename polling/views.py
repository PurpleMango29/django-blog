from django.shortcuts import render
from polling.models import Poll

def list_view(request):
    context = {'polls': Poll.objects.all()}  # 'polls' matches the 'polls' in the list.html
    return render(request, 'polling/list.html', context)

def detail_view(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404

    if request.method == "POST":
        if request.POST.get("vote") == "Yes":
            poll.score += 1  # score ties back to the models.py
        else:
            poll.score -= 1
        poll.save()

    context = {'poll': poll}
    return render(request, 'polling/detail.html', context)



