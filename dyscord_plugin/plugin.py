import discord
import discord.ext.commands as commands
from discord.ext.commands import view, context, bot

from .storage import StorageManager
from .message import DyscordContext


class DyscordPlugin:
    def __init__(self, b: bot.Bot):
        self.bot = b

    async def process_msg(self, msg: discord.Message, storagem: StorageManager):
        sview = view.StringView(msg.content)

        prefix = await self.bot.get_prefix(msg)
        invoked_prefix = prefix

        if not isinstance(prefix, (tuple, list)):
            if not sview.skip_string(prefix):
                return
        else:
            invoked_prefix = discord.utils.find(sview.skip_string, prefix)
            if invoked_prefix is None:
                return

        invoker = sview.get_word()
        tmp = {
            'bot': self.bot,
            'invoked_with': invoker,
            'message': msg,
            'view': sview,
            'prefix': invoked_prefix
        }
        ctx = DyscordContext(storagem, **tmp)
        del tmp

        try:
            command = getattr(self, invoker)
            if not isinstance(command, commands.Command):
                raise AttributeError
        except AttributeError:  # Command not found
            return
        else:
            try:
                await command.invoke(ctx)
            except commands.CommandError as e:
                await ctx.command.dispatch_error(ctx, e)
