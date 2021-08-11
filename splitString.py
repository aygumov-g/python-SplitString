from random import randint as _______

def _(_):
	_____ = {}
	def __(______):
		def ___(__, ___: int):
			__________ = _____["_"] = []
			for ____ in range(0, len(__), ___):
				__________.append(__[____:____+___])
		def ____(____, __, ______):
			__________ = ____
			for _________ in __:
				if ______ % _________ == 0:
					___(_, ______ // _________)
				else:
					__________ -= 1
			return __________
		________ = [
			5,
			4,
			3,
			2
		]
		if ____(len(________), ________, len(______)) == 0:
			___________ = 10
			while ___________ > 0:
				____(len(________), ________, len(______) + _______(0, len(________) - 1))
				___________ -= 1
			_____["check"] = True
		_____["choice"] = ________
	__(_)
	_____["len"] = len(_)
	return _____

print(_("Here you can put any text that the program will later divide into: equal 2 or 3 or 4 or 5 parts; words."))
