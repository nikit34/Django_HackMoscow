from django.contrib import admin

# Register your models here.

from .models import Task, Child, TaskInstance, Teacher#, Subject


# admin.site.register(Task)
# admin.site.register(TaskInstance)
# admin.site.register(Subject)
admin.site.register(Teacher)
# admin.site.register(Child)


class CompanysInline(admin.TabularInline):
    model = Task


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'group')
    fields = ['first_name', 'last_name', ('date_of_birth', 'group')]


@admin.register(Child)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'group')
    fields = ['first_name', 'last_name', ('date_of_birth', 'group')]
    inlines = [CompanysInline]


class CompanysInstanceInline(admin.TabularInline):
    model = TaskInstance


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'child', 'display_genre')
    inlines = [CompanysInstanceInline]


admin.site.register(Task, CompanyAdmin)


@admin.register(TaskInstance)
class CompanyInstanceAdmin(admin.ModelAdmin):
    list_display = ('task', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('task', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
