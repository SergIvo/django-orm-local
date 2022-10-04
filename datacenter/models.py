from django.db import models
from django.utils.timezone import localtime

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
    
    def get_duration(self):
        if self.leaved_at:
    	    delta = self.leaved_at - self.entered_at
        else:
            delta = localtime() - self.entered_at
        return round(delta.total_seconds())
        
    def is_long(self, minutes):
        duration = self.get_duration()
        max_time = minutes * 60
        return bool(duration // max_time)
        
def format_duration(duration):
    hours = duration // 3600
    minutes = (duration - hours * 3600) // 60
    seconds = duration - hours * 3600 - minutes * 60
    return f'{hours}ч {minutes}мин {seconds}сек'
