# T: O(n), S: O(1)
class AppleStocks(object):
	"""docstring for AppleStocks"""
	def apple_stocks(self, l):
		max_profit = l[1] - l[0]
		min_price = l[0]
		for index, current_price in enumerate(l):
			if index == 0:
				continue
			profit = current_price - min_price
			max_profit = max(profit, max_profit)
			min_price = min(current_price, min_price)

		return max_profit

if __name__ == '__main__':
	print AppleStocks().apple_stocks([10,5,3,2])	