import csv
import datetime

from django.contrib import admin

# Register your models here.
from django.http import HttpResponse

from .models import Todos


class TodoAdmin(admin.ModelAdmin):
    """
    Modify the features for the admin interface
    """
    fields = ['title', 'todo_date_time', 'status', 'is_deleted', 'description']

    search_fields = ['title', 'status']

    list_filter = ['title', 'todo_date_time', 'created_at', 'modified_at']

    list_display = ['title', 'status', 'todo_date_time', 'created_at', 'modified_at', 'description', 'is_deleted']

    # list_editable = ['status', 'todo_date_time', 'description']

    list_editable = ['status']

    list_per_page = 10

    actions = ['export_to_csv']

    def export_to_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])
        return response

    export_to_csv.short_description = "Export Selected to CSV"


admin.site.register(Todos, TodoAdmin)
