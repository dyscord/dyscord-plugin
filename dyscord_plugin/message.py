from discord.ext.commands import Context
from .storage import StorageManager


class DyscordContext(Context):
    def __init__(self, storagem: StorageManager, **attrs):
        super().__init__(**attrs)
        self.storage = storagem
