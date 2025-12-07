# django_blog — Post CRUD Features

## Overview
This addition implements full Create / Read / Update / Delete operations for the Post model using Django class-based views.

## URLs
- List all posts:        /posts/            (PostListView)
- Create a post:         /posts/new/        (PostCreateView) — login required
- View post detail:      /posts/<pk>/       (PostDetailView)
- Edit a post:           /posts/<pk>/edit/  (PostUpdateView) — author only
- Delete a post:         /posts/<pk>/delete/ (PostDeleteView) — author only

## Permissions
- Anyone can view lists and details.
- Only authenticated users can create posts.
- Only the original author can edit or delete their posts (enforced with `UserPassesTestMixin`).

## Templates
Templates are under `blog/templates/blog/`:
- `post_list.html`
- `post_detail.html`
- `post_form.html`
- `post_confirm_delete.html`

All templates extend `blog/base.html`.

## Forms
A `PostForm` (`blog/forms.py`) is used for create & update. The `author` is automatically set in the CreateView `form_valid()` method. The UpdateView does not allow changing the author.

## Admin
Register the `Post` model in `blog/admin.py` to manage posts via the Django admin.

## Testing
Follow the "Testing guidelines" in the project documentation or above.

## Notes
- Ensure `LOGIN_URL`, `LOGIN_REDIRECT_URL`, and `LOGOUT_REDIRECT_URL` are set in settings.py.
- Use `makemigrations` and `migrate` after changing models.
