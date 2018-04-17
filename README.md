# Portfolio Tracker
Portfolio tracker is a plugin for BitBar that lets you easily see your gains or losses for the day in your menu bar. Clicking on the menu bar item will also give you a breakdown of how each of your stocks is performing, as seen here: [portfolio tracker screenshot](https://imgur.com/a/WV50W)

# Installation

In order to use this plugin, you must download and install [BitBar](https://getbitbar.com/), which lets you put the output from any program in your MacOS menu bar. BitBar will ask you to set up a plugins folder. After doing so, simply drag the .py file into the proper directory. If you are having issues with it running, try running `chmod +x portfolio-tracker.py` in the directory it's located in, and refreshing BitBar. 

# Usage

Using Portfolio Tracker is easy! Simply edit line 18 of the python file with your favorite text editor to include the stocks (in symbol format) that you own, as well as the amount owned. An example is included in the file: `portfolio = {'APPL': 10, 'NFLX': 3, 'AMZN': 1}`.
