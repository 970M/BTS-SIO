## I - Installation / préparation

#### 1 - Installer / Démarrer WAMP

> https://www.wampserver.com/

#### 2 - Lancer mysql

    sudo /etc/init.d/mysql start

#### 3 - Lancer apache server

    $> sudo systemctl start apache2

#### 4 - Se connecter à mysql

    $> mysql -u phpmyadminGD -p

Reconfigurer phpmyadmin :

    $> sudo dpkg-reconfigure p hpmyadmin

    $> sudo cat /etc/mysql/debian.cnf

## II - Initialiser la base de données

#### 1 - Créer la base de donnée **_registration_**

    mysql> CREATE DATABASE registration

    mysql> show databases;

#### 2 - Se connecter à la base de données

    mysql> USE registration;

#### 3 - Créer la table **_users_**

    mysql> CREATE TABLE users (id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, username varchar(100) NOT NULL, email varchar(100) NOT NULL, password varchar(100) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=latin1;

    mysql> show tables;

## II - Récupérer les fichiers du projet en local

#### 1 - Créer le repertorie **registration**

    mkdir registration

#### 2 - Récupérer les fichiers

https://drive.google.com/drive/folders/14Ahluo8KjcSSMZiXbMgJLPl57oYVQ7cJ?usp=sharing

> touch config.php
> touch index.php
> touch login.php
> touch logout.php
> touch register.php
> touch style.css
