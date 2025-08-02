from django.apps import AppConfig

class RelationshipAppConfig(AppConfig):
    name = 'relationship_app'

    def ready(self):
        # The signal was likely imported here. Let's ensure it's commented out or removed.
        # from . import signals 
        pass # We don't want any signals running from this app