import sqlite3

# 1. Configuração de uma base de dados temporária (em RAM)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('CREATE TABLE users (username TEXT, password TEXT)')
cursor.execute('INSERT INTO users VALUES ("admin", "p@ssword123")')

def login_vulneravel(user, pw):
    # ERRADO: Concatenar strings permite que o atacante "feche" a aspa e escreva código SQL
    query = f"SELECT * FROM users WHERE username = '{user}' AND password = '{pw}'"
    print(f"\n [QUERY EXECUTADA]: {query}")
    cursor.execute(query)
    if cursor.fetchone():
        print("Resultado: Login efetuado! (Vulnerabilidade explorada com sucesso)")
    else:
        print("Resultado: Login falhou.")

def login_seguro(user, pw):
    # CORRETO: O '?' serve como placeholder. O motor do SQL trata a entrada apenas como texto.
    query = "SELECT * FROM users Where username = ? AND password = ?"
    print(f"\n[QUERY SEGURA]: {query}")
    cursor.execute(query, (user, pw)) # Os valores são passados separadamente
    if cursor.fetchone():
        print("Resultado: Login efetuado com sucesso.")
    else:
        print("Resultado: Login bloqueado! (O ataque foi neutralizado)")

# --- TESTES ---
print("=== FASE 1: O ATAQUE (SQL iNJECTION) ===")
# O atacante usa ' -- para anular o resto da consulta
ataque_sql = "admin' --"
login_vulneravel(ataque_sql, "qualquer_coisa")

print("\n=== FASE 2: A DEFESA (PARAMETRIZAÇÃO) ===")
login_seguro(ataque_sql, "qualquer_coisa")
