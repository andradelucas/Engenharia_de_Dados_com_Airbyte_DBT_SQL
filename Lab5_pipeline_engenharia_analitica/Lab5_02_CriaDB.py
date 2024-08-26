import psycopg2 

# Função para executar script SQL
def dsa_executa_script_sql(filename):
    # Conecta ao banco de dados PostgresSQL com as credenciais fornecidas
    conn = psycopg2.connect(
        dbname="dsadb",
        user="dsa",
        password="dsa1010",
        host="localhost",
        port="5959"
    )
    # Abre um cursor para realizar operações no banco de dados
    cur = conn.cursor()
    # Lê o conteudo do rquivo SQL
    with open(filename,'r') as file:
        sql_script = file.read()

    try:
        # excuta o script SQL
        cur.execute(sql_script)

        # Confirma as mudanças no banco de dados
        conn.commit()
        print("\nScript executando com sucesso\n")
    except Exception as e:
        #Reverte as mudanças em caso de erro
        conn.roolback()
        print(f"Erro ao executar o script: {e}")
    finally:
        # FEcha a comunicação com o banco de dados
        cur.close()
        conn.close()
# Executa o script SQL
dsa_executa_script_sql('Lab05_01.sql')

        