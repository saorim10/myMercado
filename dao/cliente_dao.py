from util import conector


def criar_tabela():
    sql_cria_tabela = """CREATE TABLE `cliente` (""" \
        """`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY, """ \
        """`nome` VARCHAR(50) NOT NULL, """ \
        """`cpf` VARCHAR(11) NOT NULL, """ \
        """`rg` VARCHAR(15) NOT NULL, """ \
        """`telefone` VARCHAR(14), """ \
        """`email` VARCHAR(30))"""
    conector.cursor.execute(sql_cria_tabela)


def inserir(cliente): # CREATE

    nome = cliente.nome
    cpf = cliente.cpf
    rg = cliente.rg
    telefone = cliente.telefone
    email = cliente.email

    dados = (nome, cpf, rg, telefone, email)
    sql = 'INSERT INTO cliente (nome, cpf, rg, telefone, email) VALUES (%s, %s, %s, %s, %s)'
    conector.cursor.execute(sql, dados)
    conector.conn.commit()


def consulta(): # READ

    sql = 'SELECT * FROM cliente'
    conector.cursor.execute(sql)
    lista = conector.cursor.fetchall()
    for item in lista:
        print('================================')
        print(f'ID: {item[0]}')
        print(f'Nome: {item[1]}')
        print(f'CPF: {item[2]}')
        print(f'RG: {item[3]}')
        print(f'TELEFONE: {item[4]}')
        print(f'E-MAIL: {item[5]}')


def atualiza(nome, id): # UPDATE
    sql = 'UPDATE cliente SET nome = %s WHERE id=%s'
    dados = (nome, id)

    conector.cursor.execute(sql, dados)
    conector.conn.commit()


def apaga(id): # DELETE
    sql = 'DELETE FROM cliente WHERE id=%s'
    conector.cursor.execute(sql, id)
    conector.conn.commit()


def endpoint(id):
    sql = 'SELECT * FROM cliente WHERE id=%s'
    conector.cursor.execute(sql, id)
    dados = conector.cursor.fetchone()
    saida = f'"id": "{dados[0]}", ' \
            f'"nome": "{dados[1]}", ' \
            f'"cpf": "{dados[2]}", ' \
            f'"rg": "{dados[3]}", ' \
            f'"telefone": "{dados[4]}", ' \
            f'email: "{dados[5]}"'
    return '[{' + saida + '}]'
