# SKULLUSERBOT
THIS IS ULTRA BEST USERBOT FOR TELEGRAM.

# SKULL USERBOT

### The Easy Way to deploy the bot
Get APP ID and API HASH from [HERE](https://my.telegram.org) and BOT TOKEN from [Bot Father](https://t.me/botfather) and then Generate stringsession by clicking on run.on.repl.it button below and then click on deploy to heroku . Before clicking on deploy to heroku just click on fork and star just below

[![Get string session](https://repl.it/@hackelite01/SKULLUSERBOT)

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fhackelite01%2FSKULLUSERBOT%2Ftree%2Fbugs&template=https%3A%2F%2Fgithub.com%2Fhackelite01%2FSKULLUSERBOT)
<p align="center">
  <a href="https://github.com/hackelite01/SKULLUSERBOT/fork">
    <img src="https://img.shields.io/github/forks/hackelite01/SKULLUSERBOT?label=Fork&style=social">
    
  </a>
  <a href="https://github.com/hackelite01/SKULLUSERBOT">
    <img src="https://img.shields.io/github/stars/hackelite01/SKULLUSERBOT?style=social">
  </a>
</p>


[![SKULLUSERBOT logo](https://telegra.ph/file/0e2141584fb187583002b.jpg)](https://heroku.com/deploy?template=https://github.com/hackelite01/SKULLUSERBOT)


### Join [here](https://t.me/skulluserbot) for updates and tuts and [here](https://t.me/skulluserbot_support) for discussion and bugs

### The Normal Way

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```

### UniBorg Configuration

The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**

Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`

    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.
