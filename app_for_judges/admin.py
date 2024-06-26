from django.contrib import admin
from django.contrib.auth.models import User

from .models import Judge, Participant, ParticipantsTeam, TableTask, CompetitionResult


@admin.action(description='Сбросить статус до наблюдателя')
def reset_status(modeladmin, request, queryset):
    queryset.update(status='O')


# Register your models here.
# class JudgeAdmin(admin.ModelAdmin):
#
#     list_display = ['patronymic', 'status', 'organization']
#     # list_display = ['last_name', 'name', 'patronymic', 'status', 'is_active']
#     # ordering = ['last_name', 'name']
#     # list_filter = ['last_name', 'status', 'organization']
#     # search_fields = ['last_name']
#     # search_help_text = "Поиск по полю Фамилия пользователя"
#     # actions = [reset_status]
#     # # readonly_fields = ['organization']
#     #
#     # fieldsets = [
#     #     (
#     #         None,
#     #         {
#     #             'classes': ['wide'],
#     #             'fields' : ['status', 'last_name', 'name', 'patronymic', 'is_active']
#     #
#     #         },
#     #     ),
#     #     (
#     #         'Подробности',
#     #         {
#     #             'classes'    : ['collapse'],
#     #             'description': 'Место работы, должность и регалии',
#     #             'fields'     : ['organization', 'post', 'regalia']
#     #         }
#     #     ),
#     #     ('Конкурсы и этапы',
#     #      {
#     #          'fields': ['competitions']
#     #      }
#     #      )
#     # ]


class JudgeInline(admin.ModelAdmin):
    model = User
    display_list = ['last_name', 'first_name', 'patronymic', 'status', 'is_active']
    actions = [reset_status]


class ParticipantsAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'name', 'organization', 'birthday', 'team', 'competition']
    ordering = ['last_name', 'name']
    list_filter = ['organization', 'competition']
    search_fields = ['last_name']
    search_help_text = "Поиск по полю Фамилия пользователя"


class ParticipantTeamsAdmin(admin.ModelAdmin):
    list_display = ['name', 'organization', 'competition']
    ordering = ['organization', 'name']
    list_filter = ['organization', 'competition']
    search_fields = ['name']
    search_help_text = "Поиск по полю Название команды "


class TableTaskAdmine(admin.ModelAdmin):
    model = TableTask
    list_display = ['competition_task', 'participant', 'time', 'result_place']
    ordering = ['competition_task', 'participant']
    list_filter = ['competition_task', 'participant']


class CompetitionResultAdmin(admin.ModelAdmin):
    model = CompetitionResult
    list_display = ['participant', 'final_place']


# admin.site.register(Judge, JudgeAdmin)
admin.site.register(Judge, JudgeInline)
admin.site.register(Participant, ParticipantsAdmin)
admin.site.register(ParticipantsTeam, ParticipantTeamsAdmin)
admin.site.register(TableTask, TableTaskAdmine)
admin.site.register(CompetitionResult, CompetitionResultAdmin)
