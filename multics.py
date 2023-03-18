"""The Multics Discord bot class."""

from discord.ext.commands import Bot
from discord.utils import utcnow


class MulticsBot(Bot):
    """The Multics Discord bot."""

    def __init__(self, cmd_prefix: String, **kwargs):
        """Initialize the bot."""
        super().__init__(cmd_prefix, **kwargs)
        self.cogs = []
        self.start_time = utcnow()

    def add_cog(self, cog):
        """Add a cog to the bot."""
        self.cogs.append(cog)

    def uptime(self):
        """Return the uptime of the bot."""
        return utcnow() - self.start_time

    async def load_cogs(self):
        """Load all cogs."""
        for cog in self.cogs:
            self.load_extension(cog)

    async def on_ready(self):
        """Run when the bot is ready."""
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        """Run when a message is sent."""
        if message.author.bot:
            return
        await self.process_commands(message)