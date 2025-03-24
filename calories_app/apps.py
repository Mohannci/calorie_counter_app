from django.apps import AppConfig


class CaloriesConfig(AppConfig):
    name = 'calories_app'

    def ready(self):
    	import calories_app.signals
