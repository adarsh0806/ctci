# T: O(1), S: O(1)
class TempTracker(object):
	"""docstring for TempTracker"""
	def __init__(self):
		self.min_temp = None
		self.max_temp = None
		self.mean = None
		self.mode = None
		# for mean
		self.total_numbers = 0
		self.total_sum = 0.0
		# for mode
		self.occurrences = 0
		self.max_occurrences = [0] * (100)

	# 'ahead of time' approach as opposed to the 'just in time' approach
	def insert(self, t):
		# for mean
		self.total_numbers += 1
		self.total_sum += t
		self.mean = self.total_sum / self.total_numbers

		# for mode
		self.occurrences[t] += 1
		if self.occurrences[t] > self.max_occurrences:
			self.mode = t
			self.max_occurrences = self.occurrences[t]

		# for max and min
		if (self.max_temp is None) or (t > self.max_temp):
			self.max_temp = t
		elif (self.min_temp is None) or (t < self.min_temp):
			self.min_temp = t

	def get_max(self):
		return self.max_temp

	def get_min(self):
		return self.min_temp

	def get_mean(self):
		return self.mean

	def get_mode(self):
		return self.mode

if __name__ == '__main__':
		print TempTracker().insert(5)	
		
	
		