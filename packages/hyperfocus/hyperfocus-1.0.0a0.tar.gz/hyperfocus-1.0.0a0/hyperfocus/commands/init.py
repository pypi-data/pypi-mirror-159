from hyperfocus.commands import HyperfocusCommand
from hyperfocus.config.config import Config
from hyperfocus.database import database
from hyperfocus.database.models import MODELS
from hyperfocus.locations import DEFAULT_DB_PATH
from hyperfocus.termui import printer


class InitCmd(HyperfocusCommand):
    def execute(self):
        db_path = printer.ask(
            "Database location", default=str(DEFAULT_DB_PATH), show_default=True
        )
        config = self._create_config(db_path=db_path)
        self._init_database(config=config)

    @staticmethod
    def _create_config(db_path: str) -> Config:
        config = Config()
        config.make_directory()
        config["core.database"] = db_path
        config.save()
        printer.info(
            text=f"Config file created successfully in {config.config_file.path}",
            event="init",
        )

        return config

    @staticmethod
    def _init_database(config: Config) -> None:
        database.connect(config["core.database"])
        database.init_models(MODELS)
        printer.info(
            text=f"Database initialized successfully in {config['core.database']}",
            event="init",
        )
