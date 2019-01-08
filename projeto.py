import sqlite3

BD = 'boletimEscolar.db'


# matricular Aluno no banco de dados
def matricular(matricula, nome, aprovado, recuperacao, reprovado):
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = ("INSERT INTO aluno (matricula,nome,aprovado, recuperacao, reprovado) VALUES ('%d', '%s','%s','%s','%s')"
           % (matricula, nome, aprovado, recuperacao, reprovado))
    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
        print('Aluno ', nome, 'matricula de  N°: ', matricula)
    else:
        conexao.rollback()
        print('Não foi possível matricular Aluno!')
    cursor.close()
    conexao.close()


# listar todos os alunos
def listar_aluno():
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM aluno  "
    cursor.execute(sql)
    alunos = cursor.fetchall()
    if alunos:
        for aluno in alunos:
            print('-matricula: ', aluno[0], ' - nome: ', aluno[1])
    else:
        print('Nenhum Aluno Matriculado!')
    cursor.close()
    conexao.close()


# listar todos os aluno reprovado

def listar_aluno_aprovado():
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = " SELECT * FROM Aluno WHERE aprovado = 'TRUE' "
    cursor.execute(sql)
    alunos = cursor.fetchall()
    if alunos:
        for aluno in alunos:
            print('-matricula: ', aluno[0], ' - nome: ', aluno[1],
                  ' - aprovado: ', aluno[2])
    else:
        print('Nenhum Aluno aprovado!')
    cursor.close()
    conexao.close()


# alunos de recuperação

def listar_aluno_recuperacao():
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = " SELECT * FROM Aluno WHERE recuperacao = 'True' "
    cursor.execute(sql)
    alunos = cursor.fetchall()
    if alunos:
        for aluno in alunos:
            print('-matricula: ', aluno[0], ' - nome: ', aluno[1],
                  ' - recuperacao: ', aluno[3])
    else:
        print('Nenhum Aluno de recuperação!')
    cursor.close()
    conexao.close()


# listar alunos reprovados
def listar_aluno_reprovado():
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = " SELECT * FROM Aluno WHERE reprovado = 'True' "
    cursor.execute(sql)
    alunos = cursor.fetchall()
    if alunos:
        for aluno in alunos:
            print('-matricula: ', aluno[0], ' - nome: ', aluno[1],
                  ' - reprovado: ', aluno[4])
    else:
        print('Nenhum Aluno reprovado!')
    cursor.close()
    conexao.close()


# buscar por matricular

def buscar_por_matricula(matricula):
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM aluno WHERE matricula LIKE '%d'" % matricula
    cursor.execute(sql)
    aluno = cursor.fetchall()
    if aluno:
        for aluno in aluno:
            print('-matricula: ', aluno[0], ' - nome: ', aluno[1],
                  ' - aprovado: ', aluno[2], ' - recuperacao: ', aluno[3],
                  ' - reprovado: ', aluno[4], )
        return True
    else:
        print('Nenhum aluno matriculado!')
        return False
    cursor.close()
    conexao.close()


# excluir aluno por matricular
def excluir(matricula):
    if buscar_por_matricula(matricula):
        resposta = input('Deseja realmente exlcuir este aluno ?').lower()
        if resposta == 's':
            conexao = sqlite3.connect(BD)
            cursor = conexao.cursor()
            sql = "DELETE FROM aluno WHERE matricula ='%d'" % matricula
            cursor.execute(sql)
            if cursor.rowcount == 1:
                conexao.commit()
                print('Aluno excluido!')
            else:
                conexao.rollback()
                print('Não foi possível exclui aluno')


def Lancar_notas(matricula_aluno, nota1, nota2, media):
    """lançar notas de alunos """
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = ("INSERT INTO notas (matricula_aluno, nota1, nota2, media) VALUES ('%d', '%f', '%f', '%f')"
           % (matricula_aluno, nota1, nota2, media))
    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
        print(' Notas do Aluno de matricula: ', matricula_aluno, 'foram lançadas com sucesso!')
    else:
        conexao.rollback()
        print('Não foi possivel lançar notas !')
    cursor.close()
    conexao.close()


def listar_notas():
    """listar todas as notas"""
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM notas  "
    cursor.execute(sql)
    notas = cursor.fetchall()
    if notas:
        for nota in notas:
            print('- matricula: ', nota[0], ' - nota1: ', nota[1], ' - nota2: ', nota[2], ' - media: ', nota[3])
    else:
        print('Nenhum Aluno Matriculado!')
    cursor.close()
    conexao.close()


def excluir_notas(matricula_aluno):
    # if matricula_aluno(matricula_aluno):
    resposta = input('Deseja realmente exlcuir este aluno ?').lower()
    if resposta == 's':
        conexao = sqlite3.connect(BD)
        cursor = conexao.cursor()
        sql = "DELETE FROM notas WHERE matricula_aluno = %d " % matricula_aluno
        cursor.execute(sql)
        if cursor.rowcount == 1:
            conexao.commit()
            print('Aluno excluido!')
        else:
            conexao.rollback()
            print('Não foi possível exclui aluno')


print('***********************************************************')
print('*        Bem Vindo ao Sistema de Boletim Escolar          *')
print('***********************************************************')
print('*              1 - Matricular Aluno                       *')
print('*              2 - Listar Todos os Alunos                 *')
print('*              3 - Listar Alunos Aprovados                *')
print('*              4 - Listar Aluno de Recuperação            *')
print('*              5 - Listar Aluno Reprovados                *')
print('*              6 - Buscar Aluno por Matricula             *')
print('*              7 - Excluir Aluno                          *')
print('*              8 - Lançar Notas                           *')
print('*              9-  Listar Notas                           *')
print('*              10- Excluir Notas                          *')
print('*              11- Sair                                   *')
print('*                                                         *')
print('***********************************************************')

opc = int(input(' Escolhar uma opção :  '))

if opc == 1:
    listar_aluno()
elif opc == 2:
    listar_aluno_aprovado()
elif opc == 3:
    listar_aluno_recuperacao()
elif opc == 4:
    listar_aluno_reprovado()
elif opc == 5:
    matricula = int(input('matricula: '))
    nome = input('Nome: ')
    situação = False
    matricular(matricula, nome, situação, situação, situação)
elif opc == 6:
    matricula = int(input('Digite a matricula: '))
    buscar_por_matricula(matricula)
elif opc == 7:
    matricula = int(input('Digite a matricula: '))
    excluir(matricula)
elif opc == 8:
    matricula = int(input('matricula: '))
    nota1 = float(input("digite a primeira nota: "))
    nota2 = float(input("digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    Lancar_notas(matricula, nota1, nota2, media)
elif opc == 9:
    listar_notas()
elif opc == 10:
    matricula = int(input('Digite a matricula: '))
    excluir_notas(matricula)

elif opc == 11:
    exit()





