import io
from django.contrib import admin
from .models import Client, Worker
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
import pandas as pd
admin.site.unregister(User)
admin.site.unregister(Group)
import logging
from django.core.management.base import BaseCommand
logger = logging.getLogger(__name__)


class ContactForm(forms.ModelForm):
    class Meta:
        widgets = {
            'telefon_raqam': PhoneNumberPrefixWidget(),
        }

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    form = ContactForm
    list_display_links = ('f_i_o','telefon_raqam')
    list_display = ('id', 'ishchi', 'f_i_o', 'telefon_raqam', 'zayafka_vaqti',
                     'tekshirilgan_vaqti','status')
    actions = ['export_to_excel']
    def export_to_excel(self, request, queryset):
        clients_data = []
        for client in queryset:
            clients_data.append({
                'Ishchi': client.ishchi,
                'F.I.O': client.f_i_o,
                'Telefon Raqam': client.telefon_raqam,
                'Status': client.status,
                'Kamentariya': client.comment,
                'Zayafka Vaqti': client.zayafka_vaqti.strftime('%Y-%m-%d %H:%M:%S'),
                'Tekshirilgan Vaqti': client.tekshirilgan_vaqti.strftime('%Y-%m-%d %H:%M:%S'),
            })
        df = pd.DataFrame(clients_data)
        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=False)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="clients.xlsx"'
        excel_buffer.seek(0)
        response.write(excel_buffer.read())

        return response
    export_to_excel.short_description = "EXCEL FORMAT"

    





