# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import discord
from sql import create_table, retrieve_data

client = discord.Client()

trigger = '!'
database_name = 'Test.db'


async def run_commands(message):
    """Checks if message is a command and calls command method if it is

    :param message:
    :return:
    """
    commands = {'info': send_data}
    for key in commands:
        if message.content.startswith(trigger + key):
            await commands[key](message)


async def send_data(message):
    """Retrieves data from a database and sends it as a reply

    :param message:
    :return:
    """
    command = message.content.split()
    if len(command) == 4:
        data = retrieve_data(database_name, command[1], command[2], command[3])
        await message.channel.send(data)
    else:
        await message.channel.send('!info [Table Name] [Search Col] [Search Parameter]')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await run_commands(message)


client.run('your token here')
