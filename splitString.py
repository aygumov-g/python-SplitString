from random import randint as _______

def _(_):
	_____ = {}
	def __(______):
		def ___(__, ___: int):
			__________ = _____["parts"] = []
			for ____ in range(0, len(__), ___):
				__________.append(__[____:____+___])
		if len(______) % 2 == 0:
			___(_, len(______) // 2)
		elif len(______) % 3 == 0:
			___(_, len(______) // 3)
		else:
			________ = len(______)
			if _______(1, 2) == 1:
				while not ________ % 2 == 0:
					________ += 1
				___(_, ________ // 2)
			else:
				while not ________ % 3 == 0:
					________ += 1
				___(_, ________ // 3)
	def ____(______):
		_____["words"] = ______.split()
	__(_)
	____(_)
	return _____

print(_("Here you can put any text that the program will later divide into: equal 2 or 3 parts; words."))