#!/usr/bin/env python
#

# <bitbar.title>Portfolio Tracker</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Sawyer Blatz</bitbar.author>
# <bitbar.author.github>sblatz</bitbar.author.github>
# <bitbar.desc>Displays gains and losses on a portfolio for the day.</bitbar.desc>
# <bitbar.image>https://imgur.com/a/WV50W</bitbar.image>
# <bitbar.dependencies>python</bitbar.dependencies>

import json, urllib2, re

portfolioValue = 0.0
amountGained = 0.0
portfolio = {'SPY': 37, 'ZNGA': 1}

def get_stock_price(stock):
	response = urllib2.urlopen('https://api.iextrading.com/1.0/stock/' + stock + '/quote')
	return json.loads(response.read())

def create_output_string(stock, amount):
	global amountGained
	global portfolioValue

	output = stock
	output += " - $"
	output += "{:0.2f}".format(response["latestPrice"])
	totalCost = (response["latestPrice"] * amount)
	amountGained += totalCost * response["changePercent"]
	portfolioValue += round(portfolioValue + totalCost, 2)

	output += " (" + "{:0.2f}".format(response["changePercent"] * 100.00) + "%)"
	color = "red" if response["changePercent"] < 0 else "green"
	output += " | color=" + color
	return output

for key, value in portfolio.iteritems():
	response = get_stock_price(key)
	out = create_output_string(key, value)

portfolioPercentGained = (round((amountGained / portfolioValue) * 100, 2))
finalColor = "red" if amountGained < 0 else "green"
symbol = "-$" if amountGained < 0 else "+$"

#ensure negative sign isn't shown twice
amountGained = abs(amountGained)
#bitbar output
print symbol + str(format(round(amountGained,2), ',.2f')) + " | color=" + finalColor
print "---"
print("Portfolio - $" + str(format(portfolioValue,',.2f')) + " (" + str(format(portfolioPercentGained,',.2f')) + "%)" + " | color=" + finalColor)

for key, value in portfolio.iteritems():
	response = get_stock_price(key)
	print(create_output_string(key, value))

#TODO: Improve from O(2N), just requires some refactoring.
