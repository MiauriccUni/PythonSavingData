import json
#Importamos el conector de MySQL
import mysql.connector
#Importamos las librerias que nos dan el formato de fechas 
from datetime import datetime

def tweetsave(myJson):
    #Con esta línea de codigo haremos conexión con la base de datos 
    conn = mysql.connector.connect(user='root', password='Calamarino22', host='localhost', database='twiter')
    #Instanciaremos el cursor para guardar nuestros datos
    c = conn.cursor()
    #Abrimos nuestro archivo .json
    with open(myJson) as content:
        data = json.load(content)
        
        for item in data:
            fecha = datetime.strptime(item['fecha'][:-5], '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')

            c.execute("INSERT INTO Tweets (id, texto, usuario, fecha, retweets, favoritos) VALUES (%s, %s, %s, %s, %s, %s)",
                (item['id'], item['texto'], item['usuario'], fecha, item['retweets'], item['favoritos']))
            
        conn.commit()
        conn.close()
              
if __name__=='__main__':
    myJson = 'tweets_extraction (1).json'
    tweetsave(myJson)

