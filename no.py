class sg_state(object):
	"""docstring for sg_state"""
	def __init__(self, board):
		super().__init__()
		self.board = board

	# choose best deciding factor for this
	def __lt__(self, otherState):
		#if self.nrGroups < otherState.nrGroups:
		# 	return self
		# else:
		# 	return otherState



class same_game(Problem):
	"""Receives a initial board, the objective of this problem is
	to reach an empty board"""
	def __init__(self, board):
		#create a goal board
		emptyBoard = []
		for line in board:
			emptyBoard.append([])
			for column in line:
				line.append(0)
		super().__init__(board, emptyBoard)


	def actions(self, state):
		"""Only action possible is to remove a group, therefore
		get all removable groups"""
		groups = board_find_groups(state.board)
		removableGroups = []

		for group in groups:
			if len(group) > 1:
				removableGroups.append(group)

		return removableGroups

	def result(self, state, action):
		"""Remove group from state's board"""

		newBoard = board_remove_group(state.board, action)
		newState = sg_state(newBoard)

		return newState


	def h(self, node):
		state = node.state
		removableGroups = board_find_groups(state.board)




	# mesma coisa para o path cost
