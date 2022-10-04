from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import format_duration
from django.shortcuts import render, get_object_or_404, get_list_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits_by_passcard = get_list_or_404(Visit, passcard=passcard)

    this_passcard_visits = [
        {
            'entered_at': visit.entered_at,
            'duration': format_duration(visit.get_duration()),
            'is_strange': visit.is_long(60)
        } for visit in visits_by_passcard
    ]
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
