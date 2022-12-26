class Pokemon:
    def __init__(self, name, poketype):
        self.name = name
        self.poketype = poketype

    def __repr__(self):
        return f'{self.name}/{self.poketype}'

    # def __str__(self):
        # return f'{self.name}/{self.poketype}!'

if __name__ == '__main__':
    bulbasaur = Pokemon(name='Bulbasaur', poketype = 'grass')
    print(bulbasaur)