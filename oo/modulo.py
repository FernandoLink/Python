class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.likes}'
    

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} - {self.likes}'
    

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} - {self.likes}'
    
    
class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)
   

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
tmep = Filme('Todo mundo em pâncio', 1999, 100)
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor = Serie('Demolidor', 2016, 2)
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
for programa in filmes_e_series:
    print(programa)

playlist_fim_de_semana = Playlist("fim de semana", filmes_e_series)
for programa in playlist_fim_de_semana:
    print(programa)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')    
print(f'Tá ou não tá? {demolidor in playlist_fim_de_semana}')