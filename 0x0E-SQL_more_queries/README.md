#  0x0E. SQL - More queries

## Resources
### Read or watch:
* [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
* [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-administration/mysql-grant/)
* [MySQL constraints](https://zetcode.com/mysql/constraints/)
* [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
* [Basic query operation: the join](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/join.php)
* [SQL technique: multiple joins and the distinct keyword](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/multijoin.php)
* [SQL technique: join types](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/jointypes.php)
* [SQL technique: union and minus]()
* [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
* [The Seven Types of SQL Joins](https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html)
* [MySQL Tutorial](https://www.youtube.com/watch?v=yPu6qV5byu4)
* [SQL Style Guide](https://www.sqlstyle.guide/)
* [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-data-definition-statements.html)

## Extra resources around relational database model design:
* [Design](https://www.guru99.com/database-design.html)
* [Normalization](https://www.guru99.com/database-normalization.html)
* [ER Modeling](https://www.guru99.com/er-modeling.html)


## General
* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s a PRIMARY KEY
* What’s a FOREIGN KEY
* How to use NOT NULL and UNIQUE constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are JOIN and UNION

# More Info
## Comments for your SQL file:
* -- 3 first students in the Batch ID=3
* -- because Batch 3 is the best!
* SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;

## Install MySQL 8.0 on Ubuntu 20.04 LTS
* $ sudo apt update
* $ sudo apt install mysql-server
* ...
* $ mysql --version
* mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
* $

## Connect to your MySQL server:
* $ sudo mysql
* Welcome to the MySQL monitor.  Commands end with ; or \g.
* Your MySQL connection id is 11
* Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)
* Copyright (c) 2000, 2021, Oracle and/or its affiliates.

* Oracle is a registered trademark of Oracle Corporation and/or its
* affiliates. Other names may be trademarks of their respective
* owners.

* Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

* mysql>
* mysql> quit
* Bye
* $

## How to import a SQL dump
* $ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
* Enter password:
* $ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
* Enter password:
* $ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
* Enter password:
* id  name
* 1   Drama
* 2   Mystery
* 3   Adventure
* 4   Fantasy
* 5   Comedy
* 6   Crime
* 7   Suspense
* 8   Thriller
* $
