-- Se crea la tabla donde se almacenara la informacion de los tweets
CREATE TABLE Tweets (
	id_tweet INT AUTO_INCREMENT PRIMARY KEY,
    id VARCHAR(255),
    texto TEXT,
    usuario VARCHAR(255),
    fecha TIMESTAMP,
    retweets FLOAT,
    favoritos FLOAT
);
-- Se crea otra tabla para almacenar los hashtag's utilizados
CREATE TABLE Hashtags (
-- Se crea un atributo que se incremente cada vez que que se agregue un nuevo dato de hashtag
    id INT AUTO_INCREMENT PRIMARY KEY,
    hashtag VARCHAR(255)
);
-- Se crea una nueva tabla para almacenar la relacion entre los tweets y los hashtags
CREATE TABLE TweetHashtags (
    tweet_id VARCHAR(255),
    hashtag_id INT,
    FOREIGN KEY (tweet_id) REFERENCES Tweets(id),
    FOREIGN KEY (hashtag_id) REFERENCES Hashtags(id),
    PRIMARY KEY (tweet_id, hashtag_id)
);