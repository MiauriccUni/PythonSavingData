import json
#Importamos el conector de MySQL.
import mysql.connector
#Importamos las librerias que nos dan el formato de fechas.
from datetime import datetime

def tweetsave(myJson):
    #Con esta línea de codigo haremos conexión con la base de datos .
    conn = mysql.connector.connect(user='root', password='Calamarino22', host='localhost', database='twiter')
    #Instanciaremos el cursor para guardar nuestros datos.
    c = conn.cursor()
    #Abrimos nuestro archivo .json.
    with open(myJson) as content:
        #Cargamos nuestro archivo en una variable tipo data.
        data = json.load(content)
#Recorreremos nuestros datos para agregar nuestros datos.
        for item in data:
#Manipularemos el formato de la fecha para agregarlo correctamente en la base de datos.
            fecha = datetime.strptime(item['fecha'][:-5], '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
#Insertamos los items en general, todo lo que instanciemos como un tweet se guardara como uno.
            c.execute("INSERT INTO Tweets (id, texto, usuario, fecha, retweets, favoritos) VALUES (%s, %s, %s, %s, %s, %s)",
                (item['id'], item['texto'], item['usuario'], fecha, item['retweets'], item['favoritos']))
            
            tweet_id = c.lastrowid
            
            for hashtag in item['hashtags']:
                
                c.execute("INSERT INTO Hashtags (hashtag) VALUES (%s)", (hashtag,))
                
                hashtag_id = c.lastrowid
                
                c.execute("INSERT INTO TweetHashtags (tweet_id, hashtag_id) VALUES (%s, %s)", (tweet_id, hashtag_id))
        conn.commit()
        conn.close()
              
if __name__=='__main__':
    myJson = 'tweets_extraction (1).json'
    tweetsave(myJson)

