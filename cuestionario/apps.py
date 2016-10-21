from django.apps import AppConfig


class CuestionarioConfig(AppConfig):
    name = 'cuestionario'
    def ready(self):
        print('evento autoTriggered')
        import cuestionario.cuestionario.signals.handlers #noqa
