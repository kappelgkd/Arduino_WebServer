import serial
import sqlite3
comport = serial.Serial('COM3', 9600)

print('BEM VINDO')


conn = sqlite3.connect(database = 'dados.db')

cursor = conn.cursor()
print('Conectado...')

cursor.execute("""

CREATE TABLE IF NOT EXISTS dados(
       
);
""")
print('Tabela criada.')
