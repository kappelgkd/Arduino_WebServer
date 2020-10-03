import sqlite3
import serial

conn = sqlite3.connect(database='dados.db')
cur = conn.cursor()


# Abre porta serial
ser = serial.Serial('COM5', 9600)

while True:
    print("Aguardando comando...")

    # Lê uma linha a partir da porta serial
    linha = ser.readline()

   # print("Linha recebida.")

    # Codifica dados lidos para uma string UTF-8
    linha = linha.decode('utf-8','ignore').strip()

    # Recupera os campos da linha recebida
    values = linha.split('|')

    # Valida o registro recebido. Como sao valores ciclicos
    # para nao acontecer o encerramento do programa
    # caso o sensor não passe a mensagem correta, por qualquer motivo.
    # Configurar de acordo com o 
    if len(values) == '\n':
        print("Registro Malformado: Quantidade invalida de campos")
        continue

  #  print(values)

        try:
            # Insere registro na tabela
            cur.execute("""
                INSERT INTO dados (estado)
                VALUES()""", values)
            conn.commit()
        except Exception as e:
            print("O registro nao pode ser gravado: {}".format(e))
            continue

    print("Registro gravado com sucesso")

cur.close()
conn.close()