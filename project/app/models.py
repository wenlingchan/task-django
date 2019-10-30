from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    expiry_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    def expiry_alarm(self):
        if self.expiry_date:
            EXPIRY_ALARM_ZONE = 15 * 60  # seconds
            now = timezone.now()
            if now < self.expiry_date:
                remaining_timedelta = self.expiry_date - now
                seconds_to_alarm = max(remaining_timedelta.seconds - EXPIRY_ALARM_ZONE, 0)
                html_str = 'To be expired<script>setTimeout("alert(\'Task [%s] is going to expire!\')", %s);</script>' % (self.title, seconds_to_alarm * 1000)
                return mark_safe(html_str)
            else:
                return 'Expired'
        else:
            return 'N/A'
