#gerenciamento de escola
class Aluno:
    def __init__(self, nome, matricula, notas=[]):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def __str__(self):
        return f"Aluno: {self.nome}, Matrícula: {self.matricula}, Média: {self.calcular_media()}"


class Turma:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        for aluno in self.alunos:
            print(aluno)

    def encontrar_aluno(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno
        return None

    def salvar_em_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            for aluno in self.alunos:
                arquivo.write(f"{aluno.nome},{aluno.matricula},{','.join(map(str, aluno.notas))}\n")

    def carregar_de_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(',')
                nome = partes[0]
                matricula = partes[1]
                notas = list(map(float, partes[2:]))
                aluno = Aluno(nome, matricula, notas)
                self.alunos.append(aluno)


# Exemplo de uso:
turma = Turma()
turma.carregar_de_arquivo("alunos.txt")

aluno1 = Aluno("Alice", "A001", [8.5, 7.0, 9.3])
aluno2 = Aluno("Bob", "A002", [6.5, 8.0, 7.5])
turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)

turma.listar_alunos()

aluno_encontrado = turma.encontrar_aluno("A001")
if aluno_encontrado:
    print(f"Aluno encontrado: {aluno_encontrado}")
else:
    print("Aluno não encontrado.")

turma.salvar_em_arquivo("alunos.txt")
