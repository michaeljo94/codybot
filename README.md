# CoDyBot

<p align="Left">
    <img src="https://i.imgur.com/9i0V0hq.png" alt="CoDy at its finest">
</p>


# Description

This repository is where i (@michaeljo94) develop CoDy a bot for Discord. The code is provided with absolutely no
warranty and is published under the
[MIT license](https://github.com/michaeljo94/codybot/blob/master/LICENSE.md).

CoDy is supposed to be a simple more or less lightweight bot framework based on
[discord.py](https://github.com/Rapptz/discord.py) by [Rapptz](https://github.com/Rapptz). The bot will be developed out
of the simple need for an information center on Mitsus Trash-Server.

## Table of Contents

- [Notabel Features](#notable-features)
- [Installation](#installation)
    - [No Docker](#no-docker)
    - [Docker](#docker)
- [Usage](#usage)
- [License](#license)

## Notable Features

- Easy to extend commands
- Optimized to follow modern design concepts

## Installation

__Python 3.9 or higher is required__

__A virtual environment will be strongly recommended if docker is not in use!!!__

First you need to clone the Bot.

``` bash
git clone https://github.com/michaeljo94/codybot.git
```

Now this you need to change directory to `codybot`

```bash
cd codybot
```

### No Docker

Create a virtual environment and activate it

```bash
python -m vemv venv
source venv/bin/activate
```

Install the required packages by running

```bash
python -m pip install -r requirements.txt
```

Configure your environment

```bash
echo DISCORD_TOKEN=<YOUR_TOKEN> >> .env
echo DISCORD_GUIRLD=<YOUR_GUILD_NAME> >> .env
echo CONFIG_MODULE="config" >> .env
```

Finally, run CoDy

```bash
python codybot.py
```

### Docker

Build docker container

```bash
docker build . -t <your_username>/codybot:latest
```

Run docker container

```bash
docker run <your_username>/codybot:latest --restart=until-stoped -v .env:/code/.env
```

## Usage
### Getting Help
Send `!help` in any non-nsfw discord chat the bot is connected too, to see all possible commands
```text
!help
```
### Action Example
Write you action code kinda like this.
```python
# /actions/demo_actions.py
from core.actions.generic import SimpleResponseAction


class MyAction(SimpleResponseAction):
    command_name = "MyAction"
    command_desc = "Quick demo command to demonstrate actions"
    command_trigger = "!demo"

    async def get_response(self, client, *args, **kwargs):
        return "it works! - A once well known webserver called Apache"
```

Register the action

```python
# /config.py
...
INSTALLED_ACTIONS = [..., "actions.demo_actions.MyAction", ...]
...
```

## License
This project is published with absolutely no warranty and no liability under the
 [MIT license](https://github.com/michaeljo94/codybot/blob/master/LICENSE.md).
