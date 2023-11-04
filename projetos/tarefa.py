class Tarefa:
    def __init__(self, descricao, responsavel, concluida=False):
        self.descricao = descricao
        self.responsavel = responsavel
        self.concluida = concluida

    def marcar_como_concluida(self):
        self.concluida = True

    def __str__(self):
        status = "Concluída" if self.concluida else "Pendente"
        return f"Descrição: {self.descricao}, Responsável: {self.responsavel}, Status: {status}"


class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}"


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        self.usuarios = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_tarefas(self):
        for tarefa in self.tarefas:
            print(tarefa)

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)


# Exemplo de uso:
gerenciador = GerenciadorTarefas()

usuario1 = Usuario("Alice", "alice@example.com")
usuario2 = Usuario("Bob", "bob@example.com")

tarefa1 = Tarefa("Completar o projeto", usuario1)
tarefa2 = Tarefa("Revisar documentação", usuario2)
tarefa3 = Tarefa("Realizar teste de unidade", usuario1)

gerenciador.adicionar_usuario(usuario1)
gerenciador.adicionar_usuario(usuario2)
gerenciador.adicionar_tarefa(tarefa1)
gerenciador.adicionar_tarefa(tarefa2)
gerenciador.adicionar_tarefa(tarefa3)

tarefa1.marcar_como_concluida()

gerenciador.listar_usuarios()
gerenciador.listar_tarefas()
