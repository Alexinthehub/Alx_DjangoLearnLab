from django.apps import AppConfig
def ready(self):
    import bookshelf.signals

class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'