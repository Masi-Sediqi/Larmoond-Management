from django.db import models

class AttendanceSetting(models.Model):
    work_start_time = models.TimeField(default='08:00')
    work_end_time = models.TimeField(default='16:00')
    work_hours_per_day = models.DecimalField(max_digits=4, decimal_places=2, default=8)
    allowed_paid_leave_days_per_month = models.DecimalField(max_digits=4, decimal_places=2, default=2)
    weekly_off_day = models.CharField(max_length=20, default='friday')

    def __str__(self):
        return "Attendance Setting"