from django.contrib.auth.decorators import user_passes_test

def group_required(*group_names):
    def check_group(user):
        if user.is_superuser:
            return True
        for group in group_names:
            if user.group.filter(name = group).exists():
                return True
        return False
    return user_passes_test(check_group, login_url="accounts/login")

admin_required = group_required("admin")
editor_required = group_required("editor","admin")
author_required = group_required("auhor","editor","admin")