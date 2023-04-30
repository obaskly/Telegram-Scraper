
<h1 align="center">
  <br>
  <img src="https://w7.pngwing.com/pngs/431/275/png-transparent-discord-emoji-emote-twitch-internet-bot-emoji-purple-face-head.png" width="300">
  <br>
  AH-Scraper
  <br>
</h1>

<h4 align="center">:) </h4>

<p align="center">
  <a href="">
    <img src="https://img.shields.io/badge/os-windows-blue.svg?maxAge=2592000&amp;style=flat"
         >
  </a>
  <a href=""><img src="https://img.shields.io/badge/version-1.0-red.svg?maxAge=2592000&amp;style=flat"></a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#Requirements">Requirements</a> •
  <a href="#Copyright">Copyright</a>
</p>


## Key Features

* Get messages of a specific user
* No need for bots

## How To Use

1. Log in to your Telegram core: https://my.telegram.org.

2. Go to "API development tools" and fill out the form.

3. You will get basic addresses as well as the api_id and api_hash parameters required for user authorization.

4. Put your api_id and api_hash in the script

5. Put your number in international format

6. Run script using the following command

  `python main.py -u USER_ID -o OUTPUT_FILENAME.txt`

  It will ask you for a code, you will receive that code in your telegram, copy paste the code, enter your telegram password, and you are ready to use the script.

  Go to a group and send the command `/scrape`, the script will get all the messages of that user and store them to a text file.

## Requirements

`pip install telethon colorama`

> **Note**
> Don't delete the `anon.session` file so that you don't have to enter the verification code every time you run the script

> Don't use your main account (If you don't have an extra account, don't use your main account a lot because there is a risk of getting a ban)

## Copyright

All rights reserved to Bropocalypse Team.
