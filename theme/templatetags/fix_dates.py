from django import template
from django.utils import timezone
from datetime import datetime
register = template.Library()

@register.filter()
def fix_date(value):
        current_date = timezone.now()
        value = datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f%z')
        if current_date.month == value.month and current_date.day == value.day and current_date.hour == value.hour and current_date.minute == value.minute:
            return f"{current_date.second - value.second} second(s) ago"
        elif current_date.month == value.month and current_date.day == value.day and current_date.hour == value.hour:
            return f"{current_date.minute - value.minute} minute(s) ago"
        elif current_date.day == value.day and current_date.month == value.month:
            return f"{current_date.hour - value.hour} hour(s) ago"
        else:
            return f"{(value.day - current_date.day)} day(s) ago"


@register.filter()
def update(value, arg):
    value = arg
    return value