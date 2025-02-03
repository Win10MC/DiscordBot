# Multipurpose Discord Bot

A discord bot with many features to enhance your server
## Features

- Moderation Commands
    - /kick {user}
    - /ban {user}
    - /unban {user}
    - /purge {message count}
- Welcome Images
- Leveling System
    - Gain exp by sending messages
    - Exponential curve for required exp
    - Stored in an SQL database
    - Commands
        - /setlevel {user} {level}
        - /level {user}
- Other Commands
    - /help
    - /ping
## Requirements

- Must have [git](https://git-scm.com/downloads) installed
- Must have a recent version of [python](https://www.python.org/downloads/) installed
## Installation

```bash
  git install https://github.com/Win10MC/DiscordBot.git
  cd DiscordBot
```
    
## Environment Variables

To run this project, you will need to add the following environment variable to your .env file

`BOT_TOKEN`
## Deployment

To deploy this project run

```python
  pip install -r requirements.txt
  py main.py
```
