from typing import List
import services.database as db;
import models.Cliente as cliente;


def Incluir (cliente):
    count = db.cursor.execute("""
    INSERT INTO Cliente (cliNome, cliIdade, cliProfissao, cliEmail) 
    VALUES (?,?,?,?)""",
    cliente.nome, cliente.idade, cliente.profissao, cliente.email).rowcount
    db.cnxn.commit()

def SelecionarById(id):
    db.cursor.execute("SELECT * FROM CLIENTE WHERE ID = ?", id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(cliente.Cliente(row[0], row[1], row[2], row[3], row[4]))

    return costumerList [0]

def Alterar (cliente):
    count = db.cursor.execute("""
    UPDATE Cliente
    SET cliNome = ?, cliIdade = ?, cliProfissao = ?, cliEmail = ? 
    WHERE id = ?
    """,
    cliente.nome, cliente.idade, cliente.profissao, cliente.email, cliente.id).rowcount
    db.cnxn.commit()

def Excluir(id):
    count = db.cursor.execute("""
    DELETE FROM CLIENTE WHERE id = ?""",
    id).rowcount
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM CLIENTE")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(cliente.Cliente(row[0], row[1], row[2], row[3], row[4]))

    return costumerList    
