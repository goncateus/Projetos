from database import connect

def adicionar_pessoa(nome, endereco, telefone):
    with connect() as conn:
        conn.execute('INSERT INTO pessoas (nome, endereco, telefone) VALUES (?, ?, ?)', (nome, endereco, telefone))
        print("Pessoa adicionada com sucesso!")

def listar_pessoas():
    with connect() as conn:
        cursor = conn.execute('SELECT * FROM pessoas')
        pessoas = cursor.fetchall()
        for pessoa in pessoas:
            print(pessoa)

def buscar_pessoa_por_nome(nome):
    with connect() as conn:
        cursor = conn.execute('SELECT * FROM pessoas WHERE nome LIKE ?', ('%' + nome + '%',))
        resultado = cursor.fetchall()
        if resultado:
            for pessoa in resultado:
                print(pessoa)
        else:
            print("Nenhuma pessoa encontrada.")

def atualizar_pessoa(id_pessoa, nome, endereco, telefone):
    with connect() as conn:
        conn.execute('UPDATE pessoas SET nome = ?, endereco = ?, telefone = ? WHERE id = ?', (nome, endereco, telefone, id_pessoa))
        print("Pessoa atualizada com sucesso!")

def deletar_pessoa(id_pessoa):
    with connect() as conn:
        conn.execute('DELETE FROM pessoas WHERE id = ?', (id_pessoa,))
        print("Pessoa deletada com sucesso!")

