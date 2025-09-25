from __future__ import annotations

class Film:
	
	__id: int 
	__title: str

	def __init__(self, id: int, title: str) -> None:
		self.__id = id
		self.__title = title

	def setID(self, id: int) -> None:
		self.__id = __id

	def setTitle(self, title: str) -> None:
		self.__title = title

	def getID(self) -> int:
		return self.__id

	def getTitle(self) -> str:
		return self.__title

	def isEqual(self, otherFilm: Film) -> bool:
		if self.getID() == otherFilm.getID():
			return True

		return False

	def __repr__(self) -> str:
		return self.getTitle()


