# django-extuser

Custom user model for Django Framework.

# Using

1. Clone this repository into your project folder
2. Add application `extuser` into Django settings variable `INSTALLED_APPS`
3. Add at end of `settings.py` line

```python
AUTH_USER_MODEL = 'extuser.ExtUser'
```

4. Add more fields to `ExtUser` model
4.1. Override methods, if required.
5. Call two commands from console

```bash
django-admin.py makemigrations
django-admin.py migrate
```
