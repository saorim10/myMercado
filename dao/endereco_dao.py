from util import conector


def criar_tabela():
    sql_cria_tabela = """CREATE TABLE `endereco` (""" \
        """`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY, """ \
        """`cep` VARCHAR(10) NOT NULL, """ \
        """`logradouro` VARCHAR(50) NOT NULL, """ \
        """`numero` VARCHAR(10), """ \
        """`complemento` VARCHAR(20), """ \
        """`bairro` VARCHAR(25), """ \
        """`cidade` VARCHAR(25), """ \
        """`estado` VARCHAR(2))"""
    conector.cursor.execute(sql_cria_tabela)


def inserir(endereco): # CREATE
    cep = endereco.cep
    logradouro = endereco.logradouro
    numero = endereco.numero
    complemento = endereco.complemento
    bairro = endereco.bairro
    cidade = endereco.cidade
    estado = endereco.estado

    dados = (cep, logradouro, numero, complemento, bairro, cidade, estado)
    sql = 'INSERT INTO endereco (cep, logradouro, numero, complemento, bairro, cidade, estado) ' \
          'VALUES (%s, %s, %s, %s, %s, %s, %s)'
    conector.cursor.execute(sql, dados)
    conector.conn.commit()


def consulta(): # READ

    sql = 'SELECT * FROM endereco'
    conector.cursor.execute(sql)
    lista = conector.cursor.fetchall()
    for item in lista:
        print('================================')
        print(f'ID: {item[0]}')
        print(f'CEP: {item[1]}')
        print(f'LOGRADOURO: {item[2]}')
        print(f'NÚMERO: {item[3]}')
        print(f'COMPLEMENTO: {item[4]}')
        print(f'BAIRRO: {item[5]}')
        print(f'CIDADE: {item[6]}')
        print(f'ESTADO: {item[7]}')


def atualiza(logradouro, id): # UPDATE
    sql = 'UPDATE endereco SET logradouro = %s WHERE id=%s'
    dados = (logradouro, id)

    conector.cursor.execute(sql, dados)
    conector.conn.commit()


def apaga(id): # DELETE
    sql = 'DELETE FROM endereco WHERE id=%s'
    conector.cursor.execute(sql, id)
    conector.conn.commit()


def endpoint(id):
    sql = 'SELECT * FROM endereco WHERE id=%s'
    conector.cursor.execute(sql, id)
    dados = conector.cursor.fetchone()
    saida = f'"id": "{dados[0]}", ' \
            f'"cep": "{dados[1]}", ' \
            f'"logradouro": "{dados[2]}", ' \
            f'"numero": "{dados[3]}", ' \
            f'"complemento": "{dados[4]}", ' \
            f'"bairro": "{dados[5]}", ' \
            f'"cidade": "{dados[6]}", ' \
            f'estado: "{dados[7]}"'
    return '[{' + saida + '}]'
