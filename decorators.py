from django.contrib.auth.decorators import user_passes_test

def groupRequired(group):
    "Decorator that checks whether user is in given group"
    return user_passes_test(lambda u: bool(u.groups.filter(name = (group))))

