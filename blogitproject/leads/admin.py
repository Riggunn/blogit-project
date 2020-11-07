from django.contrib import admin
from leads.models import Lead
from  django.db import models
from django.http import HttpResponse
import csv
# Register your models here.
# class Lead(models.Model):
#     name = models.CharField(max_length=60, blank=True, default='')
#     subject = models.CharField(max_length=60, blank=True, default='')
#     email = models.EmailField(max_length=250, blank=False, default='')
#     message = models.TextField(blank=True, default='')
#     created_at = models.DateTimeField(auto_now=True, blank=True)
#     is_answered = models.BooleanField(default=False)
class ExpotrCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type = 'text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response, delimiter=';')

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

class LeadFormAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = False
    list_display = ('id', 'name', 'subject', 'email', 'message', 'created_at_format', 'is_answered')
    list_display_links = ('subject',)
    list_editable = ('is_answered',)
    list_filter = ('is_answered',)
    ordering = ('is_answered', 'id')
    readonly_fields = ('name', 'subject', 'email', 'message', 'created_at',)
    search_fields = ('email', 'name',)
    actions = ('export_as_csv',)

    def created_at_format(self, obj):
        beauty_data = obj.created_at.strftime('%d.%m.%y %H:%M:%S')
        return beauty_data


admin.site.register(Lead, LeadFormAdmin)
