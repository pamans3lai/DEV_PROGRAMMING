class Murid:
    def __init__(self, name):
        self.name = name
        self._score = 0 #penyimpanan internal

    @property
    def score(self):
        """The score property."""
        return self._score
    
    @score.setter
    def score(self, value):
        if 0 <= value <=100:
            self._score = value
        else:
            raise ValueError("nilai harus antara 0 dan 100")

#penggunaan

s = Murid("Ihsan")
try:
    s.score = 95
    print(f"{s.name}' score: {s.score}")
    s.score = 105
except ValueError as e:
    print(f"Error: {e}")

