# Twitter Filmobot

## Description
A twitter bot posting nice curated movie screenshots.
This project is using Python and Tweepy to handle the communication with the twitter API.
Hosted on Heroku and running with the Heroku Scheduler addon.

Two scripts have been made to capture screenshots, first I made [screenshot-contraption](https://github.com/monsieurr/screenshot_contraption) to capture screenshots directly from any window but this wasn't very efficient and meant you had to wait for the entire duration of the video for the script to end. It's still useful if you want to capture using the OS print screen feature.
I made another one ([screenshot-contraption2](https://github.com/monsieurr/screenshot_contraption2)) that works in the background using ffmpeg, very efficient to treat multiple local files.

## Other twitter bots I made
- [twitter-arti-bot](https://github.com/monsieurr/twitter-arti-bot) : posts photos each day, curated from my collection.
- [motbot](https://github.com/monsieurr/motbot) : posts a different quote in french with a random coloured background each day.
- [color-bot](https://github.com/monsieurr/color-bot) : posts a set of 4 random colors each day, very simple but probably my favourite.
