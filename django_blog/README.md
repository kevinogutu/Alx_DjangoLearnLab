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
# Comments feature — django_blog

## Overview
- Users can read comments on a post.
- Authenticated users may create, edit, and delete their own comments.

## Models
- Comment(post:FK, author:FK, content:Text, created_at, updated_at)

## URLs
- Create:   /posts/<post_id>/comments/new/       (comment-create)
- Edit:     /posts/<post_id>/comments/<comment_pk>/edit/   (comment-update)
- Delete:   /posts/<post_id>/comments/<comment_pk>/delete/ (comment-delete)

Forms use `CommentForm` (ModelForm) and validation is handled by the form/model.

## Permissions
- Create: logged-in users only
- Edit/Delete: comment author only

## How to use
1. Open post detail at /posts/<post_id>/
2. If logged in, enter a comment in the inline form and submit.
3. For editing/deleting, click the Edit/Delete links on your own comments.

## Admin
- Comments can also be viewed and moderated in the Django admin.
# Tagging & Search Features — django_blog

## Tagging
- Posts can have multiple tags.
- Tags are displayed on the post detail page.
- Clicking a tag shows all posts with that tag.

## Search
- Search bar available on the site.
- Search matches title, content, or tags.
- Results are displayed on a separate search results page.

## How to Use
1. Add tags when creating or updating a post.
2. Click tags to filter posts.
3. Enter keywords or tag names in the search bar to find posts.
