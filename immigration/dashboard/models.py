from django.db import models
from django.urls import reverse
from PIL import Image
from django.utils import timezone
from django.utils.timezone import now
from datetime import datetime


class Branch(models.Model):
    brach_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.brach_name)


class Lead(models.Model):
    STATUSES = (
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected')
    )
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    case_type = models.CharField(max_length=255)
    countery_for_apply = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    mobile_number = models.IntegerField()
    email = models.EmailField()
    description = models.TextField(null=True, blank=True)
    lead_date = models.DateTimeField(auto_now_add=True)
    succeed = models.CharField(max_length=255, choices=STATUSES, default='pending')

    def __str__(self):
        return str(self.full_name)

    def get_absolute_url(self):
        return reverse('lead-details', kwargs={'pk': self.id})


class Application(models.Model):
    STATUSES = (
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected')
    )
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='media/application-images', blank=True, null=True)
    file_number = models.CharField(max_length=255, unique=True)
    uic_number = models.IntegerField(null=True, blank=True)
    full_name = models.CharField(max_length=255)
    case_type = models.CharField(max_length=255)
    countery_for_apply = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    mobile_number = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    total_fees = models.IntegerField(null=True, blank=True)
    estimate_compleation_date = models.DateField()
    application_date = models.DateField()
    succeed = models.CharField(max_length=255, choices=STATUSES, default='pending')

    def save(self):
        super().save()
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 50 or img.width > 50:
                new_img = (256, 256)
                img.thumbnail(new_img)
                img.save(self.image.path, format="JPEG", quality=100)

    def time_progress(self):
        total_time = (int((self.estimate_compleation_date).strftime('%s')) - int((self.application_date).strftime('%s')))/86400
        completed_time = (int(now().strftime('%s'))-int((self.application_date).strftime('%s')))/86400
        progress = (completed_time*100)/total_time
        return int(progress)
    
    def estimated_time(self):
        seconds = int((self.estimate_compleation_date).strftime('%s')) - int(now().strftime('%s'))
        days_s = seconds/86400
        days = int(days_s)
        weeks = int(seconds*0.0000016534391534392)
        months = int(days_s*0.0329)
        if seconds <= 0:
            remaining_time = f'Completed'
        elif seconds > 0 and seconds < 86400:
            remaining_time = f'1 Day'
        elif seconds >= 86400 and seconds <= 172800:
            remaining_time = f'2 Days'
        elif seconds > 172800 and days <= 30:
            remaining_time = f'{days} Day(s)'
        elif days > 30 and days <= 120:
            remaining_time = f'{weeks} Week(s)'
        elif days == 121:
            remaining_time = f'{weeks} Week(s)'
        elif days > 120:
            remaining_time = f'{months} Month(s)'
        return remaining_time

    def __str__(self):
        return f'{self.full_name} ({self.file_number})'

    def get_absolute_url(self):
        return reverse('application-details', kwargs={'pk': self.id})


class Payment(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField()
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.application)
    
    def get_absolute_url(self):
        return reverse('applications')
