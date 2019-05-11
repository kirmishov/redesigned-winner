from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "my_cookiecutter_django_project.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import my_cookiecutter_django_project.users.signals  # noqa F401
        except ImportError:
            pass
