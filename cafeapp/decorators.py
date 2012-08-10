from django.contrib.auth.decorators import user_passes_test, login_required

@login_required
def group_required(group):
    "Decorator that checks whether user is in given group"
    return user_passes_test(lambda u: bool(u.groups.filter(name = (group))))

