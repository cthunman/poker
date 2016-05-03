
class Table():
	def __init__(self, player_list, game='NLHE'):
		self.player_list = player_list
		self.game = game


class Player():
	def __init__(self, name, seat=None):
		self.name = name
		self.seat = seat

	