class BasePokemon:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def to_str(self):
        return f'{self.name}/{self.category}'


class Pokemon(BasePokemon):
    def __init__(self, name, category, weaknesses):
        super().__init__(name, category)
        self.weaknesses = weaknesses


if __name__ == '__main__':
    charmander = Pokemon(name='Charmander', category='Lizard',
                         weaknesses=('water', 'ground', 'rock'))

    print(charmander.to_str())
    print(charmander.__dict__)
    