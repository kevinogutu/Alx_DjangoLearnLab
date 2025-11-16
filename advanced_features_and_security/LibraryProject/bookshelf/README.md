Bookshelf Permissions & Groups
------------------------------

1. Custom permissions added to Book model:
   - can_view
   - can_create
   - can_edit
   - can_delete

2. Groups (created via management command):
   - Viewers  => can_view
   - Editors  => can_view, can_create, can_edit
   - Admins   => can_view, can_create, can_edit, can_delete

3. Setup steps:
   - python manage.py makemigrations
   - python manage.py migrate
   - python manage.py create_groups
   - Create users and add them to groups via admin or shell.

4. Views:
   - add_book: requires bookshelf.can_create
   - edit_book: requires bookshelf.can_edit
   - delete_book: requires bookshelf.can_delete
   - (optional) book_list: can be left open or protected by bookshelf.can_view

5. Notes:
   - Use Django admin to tune group membership and to adjust permissions.
   - The management command expects the Book model permissions already exist (so run migrations first).
