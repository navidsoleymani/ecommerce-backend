from django.contrib import admin
from django import forms
from django.contrib.auth.hashers import make_password

from users.models import UserModel as Model

INITIAL_PASSWORD = '********'


class UserModelForm(forms.ModelForm):
    new_password = forms.CharField(
        required=False, initial=INITIAL_PASSWORD, label=' Password')

    class Meta:
        model = Model
        fields = [
            'new_password',
        ]


@admin.register(Model)
class UserModelAdmin(admin.ModelAdmin):
    filter_horizontal = [
        'groups',
        'user_permissions',
    ]

    list_display = [
        'is_active',
        'available',
        'id',

        'username',
        'first_name',
        'last_name',
        'email',

        'is_staff',
        'is_superuser',

        'last_login',
        'date_joined',

        'created_dt',
        'updated_dt',
    ]
    list_display_links = [
        'is_active',
        'available',
        'id',

        'username',
        'first_name',
        'last_name',
        'email',

        'is_staff',
        'is_superuser',

        'last_login',
        'date_joined',

        'created_dt',
        'updated_dt',
    ]
    list_filter = [

        'is_active',
        'available',

        'is_staff',
        'is_superuser',

        'date_joined',

        'groups',
    ]
    search_fields = [
        'id',

        'username',
        'first_name',
        'last_name',
        'email',
    ]
    readonly_fields = [
        'id',
        'created_dt',
        'updated_dt',
        'password',
    ]
    fieldsets = [
        ('Info', {'fields': [
            ('available', 'id'),
            ('username', 'new_password',),
            ('first_name', 'last_name',),
            'email',
        ]}),
        ('Auth', {'fields': [
            ('is_staff', 'is_superuser',),
            'groups',
            'user_permissions',
        ]}),
        ('Extra', {'fields': [
            'is_active',
            ('last_login', 'date_joined',),
            ('created_dt', 'updated_dt',),
        ]}),
    ]
    form = UserModelForm

    def save_model(self, request, obj, form, change):
        new_password = request.POST.get('new_password')

        if new_password and new_password != INITIAL_PASSWORD:
            obj.password = make_password(new_password)

        super().save_model(request, obj, form, change)
