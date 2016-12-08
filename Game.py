
class Game():
	def __init__(self, name, numHoleCards):
		self.name = name
		self.numHoleCards = numHoleCards

games = {
	'plo' : Game('plo', 4),
	'nlh' : Game('nlh', 2)
}
