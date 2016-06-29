# coding=utf-8
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.admin import widgets
from django.utils.translation import ugettext_lazy as _
from django import forms
import models as models


class CustomUserCreationForm(UserCreationForm):
    stations = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=widgets.FilteredSelectMultiple(_('stations'), False)
    )

    def __init__(self, *args, **kw):
        super(CustomUserCreationForm, self).__init__(*args, **kw)
        self.fields['stations'].queryset = models.Station.objects.all()
        self.m2mrel_fields = ['stations']

    def _save_m2m_rel(self):
        for field in self.m2mrel_fields:
            data = self.cleaned_data[field]
            setattr(self.instance, field, data)

    def _save_m2m(self):
        super(CustomUserCreationForm, self)._save_m2m()
        self._save_m2m_rel()


class CustomUserChangeForm(UserChangeForm):
    stations = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=widgets.FilteredSelectMultiple(_('stations'), False),
    )

    def __init__(self, *args, **kw):
        instance = kw.get('instance')
        kw['initial'] = kw.pop('initial', {})
        kw['initial'].update({'stations': instance.stations.all()})
        super(CustomUserChangeForm, self).__init__(*args, **kw)
        self.fields['stations'].queryset = models.Station.objects.all()
        self.m2mrel_fields = ['stations']

    def _save_m2m_rel(self):
        for field in self.m2mrel_fields:
            data = self.cleaned_data[field]
            setattr(self.instance, field, data)

    def _save_m2m(self):
        super(CustomUserChangeForm, self)._save_m2m()
        self._save_m2m_rel()


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'stations')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'stations'),
        }),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm


@admin.register(models.Station)
class StationAdmin(admin.ModelAdmin):
    filter_horizontal = ['managers']

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
