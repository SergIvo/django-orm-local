from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import format_duration
from django.utils.timezone import localtime
from django.shortcuts import render


def storage_information_view(request):
    not_leaved = Visit.objects.filter(leaved_at=None)
    non_closed_visits = [
        {
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(visit.get_duration()),
        } for visit in not_leaved
    ]
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
