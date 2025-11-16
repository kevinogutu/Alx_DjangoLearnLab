# bookshelf/management/commands/create_groups.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

class Command(BaseCommand):
    help = "Create default groups (Editors, Viewers, Admins) and assign permissions for Book."

    def handle(self, *args, **options):
        # Get content type for Book model
        ct = ContentType.objects.get_for_model(Book)

        # Permissions by codename (these should exist after migrations)
        p_view = Permission.objects.get(content_type=ct, codename='can_view')
        p_create = Permission.objects.get(content_type=ct, codename='can_create')
        p_edit = Permission.objects.get(content_type=ct, codename='can_edit')
        p_delete = Permission.objects.get(content_type=ct, codename='can_delete')

        # Create or get groups
        viewers, _ = Group.objects.get_or_create(name='Viewers')
        editors, _ = Group.objects.get_or_create(name='Editors')
        admins, _ = Group.objects.get_or_create(name='Admins')

        # Assign permissions
        viewers.permissions.set([p_view])
        editors.permissions.set([p_view, p_create, p_edit])
        admins.permissions.set([p_view, p_create, p_edit, p_delete])

        viewers.save()
        editors.save()
        admins.save()

        self.stdout.write(self.style.SUCCESS('Groups and permissions set up successfully.'))
