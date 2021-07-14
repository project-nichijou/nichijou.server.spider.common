import ahocorasick


class ACAutomaton():

	def __init__(self, patterns: list):
		self.ac = ahocorasick.Automaton()
		for pattern in set(patterns):
			self.ac.add_word(pattern, pattern)
		self.ac.make_automaton()


	def query(self, queries: list):
		'''
		`queries`: the `list` of `str` to query

		return values:
		`list` of `tuples`: `(<end position of pattern>, <pattern>)`
		
		e.g. `patters = ['abc']`, `queries = ['abcdefg']`, then returns:
		`[(2, 'abc')]`
		'''
		res = []
		for query in queries:
			res_query = []
			for item in self.ac.iter(query):
				res_query.append(item)
			res.append(res_query)
		return res


	def match(self, query: str):
		return len(self.query([query])[0]) > 0
