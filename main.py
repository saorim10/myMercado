from util import conector
from dao import cliente_dao, endereco_dao
from model.endereco_model import Endereco
from model.cliente_model import Cliente


nome = 'Marcelo Saorim'
cpf = '09265610816'
rg = '18216219-9'
telefone = '(12)982634529'
email = 'marcelo/@email.com'
c1 = Cliente(nome, cpf, rg, telefone, email)

nome = 'Melissa Saorim'
cpf = '11122233300'
rg = '11111111-0'
telefone = '(12)982634529'
email = 'melissa/@email.com'
c2 = Cliente(nome, cpf, rg, telefone, email)

nome = 'Sophie Saorim'
cpf = '55522999300'
rg = '222222222-0'
telefone = '(12)982634529'
email = 'sophie/@email.com'
c3 = Cliente(nome, cpf, rg, telefone, email)


cliente_dao.inserir(c1)
# cliente_dao.inserir(c2)
# cliente_dao.inserir(c3)
cliente_dao.consulta()
print('==============================================')
# cliente_dao.atualiza('Marcelo Rocha Saorim', 4)
# cliente_dao.apaga(4)
# cliente_dao.consulta()

# endereco_dao.criar_tabela()
# endereco_dao.conector.cursor.execute('SHOW TABLES')
# tabelas = endereco_dao.conector.cursor.fetchall()
# for linha in tabelas:
#     print(linha)

cep = '11668-350'
logradouro = 'Rua Alfenas'
numero = '104'
complemento = ''
bairro = 'Perequê-Mirim'
cidade = 'Caraguatatuba'
estado = 'SP'
e1 = Endereco(cep, logradouro, numero, complemento, bairro, cidade, estado)
endereco_dao.inserir(e1)
endereco_dao.consulta()
print('=============================================')
print('EndPoint')
print(cliente_dao.endpoint(5))
print(endereco_dao.endpoint(1))
conector.desconectar()
