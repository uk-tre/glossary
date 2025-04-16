from mkdocs.config import config_options
from mkdocs.plugins import get_plugin_logger
from mkdocs_table_reader_plugin.plugin import TableReaderPlugin

from .readers import READERS

logger = get_plugin_logger("uktre-glossary")


class GlossaryPlugin(TableReaderPlugin):
    config_scheme = (
        ("data_path", config_options.Type(str, default=".")),
        ("allow_missing_files", config_options.Type(bool, default=False)),
        (
            "select_readers",
            config_options.ListOfItems(
                config_options.Choice(list(READERS.keys())),
                default=list(READERS.keys()),
            ),
        ),
    )

    def on_config(self, config, **kwargs):
        """
        See https://www.mkdocs.org/user-guide/plugins/#on_config.

        Args:
            config

        Returns:
            Config
        """

        self.readers = {
            reader: READERS[reader].set_config_context(
                mkdocs_config=config, plugin_config=self.config
            )
            for reader in self.config.get("select_readers")
            if reader in self.config.get("select_readers", [])
        }
        self.external_jinja_engine = False
