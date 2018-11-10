class TeamStatistics:
	def __init__(self, win, draw, defeat, scored, missed):
		self.wins = win
		self.draws = draw
		self.loss = defeat
		self.goals_scored = scored
		self.goals_missed = missed


	def get_overall_points(self):
		result = (self.wins * 3) + (self.draws * 1) + (self.loss * 0)
		return result

	def goals_difference(self):
		result = self.goals_scored - self.goals_missed
		return result

	def __repr__(self):
		return "Team gets {} points and scored {} goals".format(self.get_overall_points(), self.goals_difference())



class ExtendsStatistics(TeamStatistics):
	def __init__(self, win, draw, defeat, scored, missed):
		super().__init__(win, draw, defeat, scored, missed)

	def get_all_played_matches(self):
		result = self.wins + self.draws + self.loss
		return "{} matches were played".format(result)



if __name__ == '__main__':

	dynamo = TeamStatistics(20, 6, 6, 56, 19)
	print(dynamo)
	print(dynamo.get_overall_points())
	print(dynamo.goals_difference())

	shahtar = ExtendsStatistics(25, 3, 4, 78, 21)
	print(shahtar)
	print(shahtar.get_overall_points())
	print(shahtar.goals_difference())
	print(shahtar.get_all_played_matches())








		