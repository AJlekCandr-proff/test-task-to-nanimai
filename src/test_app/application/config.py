from dynaconf import Dynaconf


settings: Dynaconf = Dynaconf(
    envvar_prefix=False,
    environments=True,
    load_dotenv=True,
    settings_files=["config/settings.yaml"],
)
