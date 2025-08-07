from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


@receiver(post_migrate)
def setup_groups(sender, **kwargs):
    groups = ['Candidates', 'HR Managers', 'Admins']
    for group_name in groups:
        Group.objects.get_or_create(name=group_name)

    try:
        content_type = ContentType.objects.get_for_model(sender.get_model('Resume'))

        hr_group = Group.objects.get(name='HR Managers')
        view_perm = Permission.objects.get(
            content_type=content_type,
            codename='view_resume'
        )
        hr_group.permissions.add(view_perm)

        admin_group = Group.objects.get(name='Admins')
        all_perms = Permission.objects.filter(content_type=content_type)
        admin_group.permissions.set(all_perms)
    except:
        pass