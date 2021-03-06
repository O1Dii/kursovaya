from django.contrib import admin

from .models import *


class SolutionInline(admin.TabularInline):
    model = Solution
    extra = 1


class TopicAdmin(admin.ModelAdmin):
    list_display = [i.name for i in Topic._meta.fields]
    inlines = [SolutionInline]

    class Meta:
        model = Topic


admin.site.register(Topic, TopicAdmin)


class SolutionAdmin(admin.ModelAdmin):
    list_display = [i.name for i in Solution._meta.fields]

    class Meta:
        model = Solution


admin.site.register(Solution, SolutionAdmin)


class RatingsAdmin(admin.ModelAdmin):
    list_display = [i.name for i in SolutionRating._meta.fields]

    class Meta:
        model = SolutionRating


admin.site.register(ExpertsToTopics)
admin.site.register(SolutionRating, RatingsAdmin)
