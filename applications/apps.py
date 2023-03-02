from django.apps import AppConfig


class ApplicationsConfig(AppConfig):
    name = 'applications'

    # 追加
    def ready(self):
        # 同じ階層にあるap_scheduler.pyのstart()をimportする
        from .ap_scheduler import start
        start()