from django.apps import AppConfig

class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'  # ✅ use actual app name

    def ready(self):
        import relationship_app.signals  # ✅ use actual app name
