### SQL corpus generator

This project is intended to support automatic SQL corpus generation from `.xlsx` input file.<br>

### Schema definition

| Tables_in_tk_parlament |
| :------------------------: |
| cap_kod                |
| conll_szo              |
| felszolalas            |
| kepviselo              |
| kodolja                |
| mondat                 |
| parlamenti_ciklus      |
| part                   |
<br>

**CAP_KOD** 

| Field      | Type         | Null | Key | Default | Extra |
|------------|--------------|------|-----|---------|-------|
| cap_id     | int          | NO   | PRI | NULL    |       |
| nev_magyar | varchar(100) | YES  |     | NULL    |       |
| nev_angol  | varchar(100) | YES  |     | NULL    |       |

**CONLL_SZO**

| Field          | Type         | Null | Key | Default | Extra |
|----------------|--------------|------|-----|---------|-------|
| szo_id         | int          | NO   | PRI | NULL    |       |
| sorszam        | int          | YES  |     | NULL    |       |
| szoalak        | varchar(40)  | YES  |     | NULL    |       |
| lemma          | varchar(40)  | YES  |     | NULL    |       |
| entity_IOB     | varchar(10)  | YES  |     | NULL    |       |
| POS            | varchar(20)  | YES  |     | NULL    |       |
| morf_analysis  | varchar(100) | YES  |     | NULL    |       |
| dependencia_el | varchar(20)  | YES  |     | NULL    |       |
| mondat_id      | int          | YES  | MUL | NULL    |       |

**FELSZOLALAS**

| Field                 | Type         | Null | Key | Default | Extra |
|-----------------------|--------------|------|-----|---------|-------|
| text_id               | varchar(20)  | NO   | PRI | NULL    |       |
| exact_date            | date         | YES  |     | NULL    |       |
| tokenszam             | int          | YES  |     | NULL    |       |
| text                  | text         | YES  |     | NULL    |       |
| napirendi_pont        | varchar(200) | YES  |     | NULL    |       |
| video_felszolalas_ido | time         | YES  |     | NULL    |       |
| video_feszolalas_url  | varchar(200) | YES  |     | NULL    |       |
| felszolalas_url       | varchar(500) | YES  |     | NULL    |       |
| cycle_number          | int          | YES  | MUL | NULL    |       |
| parliamentary_id      | varchar(20)  | YES  | MUL | NULL    |       |

**KEPVISELO**

| Field            | Type         | Null | Key | Default | Extra |
|------------------|--------------|------|----|---------|-------|
| parliamentary_id | varchar(100) | NO   | PRI | NULL    |       |
| seat_type        | varchar(20)  | YES  |     | NULL    |       |
| seniority        | varchar(20)  | YES  |     | NULL    |       |
| birth_year       | int          | YES  |     | NULL    |       |
| birth_place      | varchar(30)  | YES  |     | NULL    |       |
| sex              | int          | YES  |     | NULL    |       |
| death_date       | date         | YES  |     | NULL    |       |
| death_place      | varchar(20)  | YES  |     | NULL    |       |
| first_name       | varchar(20)  | YES  |     | NULL    |       |
| surname          | varchar(30)  | YES  |     | NULL    |       |
| change_name      | tinyint(1)   | YES  |     | NULL    |       |
| surname_new      | varchar(20)  | YES  |     | NULL    |       |
| surname_from     | date         | YES  |     | NULL    |       |
| party_id         | int          | YES  | MUL | NULL    |       |

**KODOLJA**

| Field       | Type        | Null | Key | Default | Extra |
|-------------|-------------|------|-----|---------|-------|
| major_topic | int         | YES  | MUL | NULL    |       |
| text_id     | varchar(20) | YES  | MUL | NULL    |       |

**MONDAT**

| Field     | Type        | Null | Key | Default | Extra |
|-----------|-------------|------|-----|---------|-------|
| mondat_id | int         | NO   | PRI | NULL    |       |
| raw_text  | text        | YES  |     | NULL    |       |
| text_id   | varchar(20) | YES  | MUL | NULL    |       |

**PARLAMENTI_CIKLUS**

| Field            | Type | Null | Key | Default | Extra |
|------------------|------|------|-----|---------|-------|
| cycle_number     | int  | NO   | PRI | NULL    |       |
| cycle_years_from | int  | YES  |     | NULL    |       |
| cycle_years_to   | int  | YES  |     | NULL    |       |
| cycle_from       | date | YES  |     | NULL    |       |
| cycle_to         | date | YES  |     | NULL    |       |

**PART**

| Field                     | Type        | Null | Key | Default | Extra |
|---------------------------|-------------|------|-----|---------|-------|
| party_id                  | int         | NO   | PRI | NULL    |       |
| party_name_full_HUN       | varchar(60) | YES  |     | NULL    |       |
| party_name_full_HUN_from  | date        | YES  |     | NULL    |       |
| party_name_full_HUN_to    | date        | YES  |     | NULL    |       |
| party_name2_full_HUN      | varchar(60) | YES  |     | NULL    |       |
| party_name2_full_HUN_from | date        | YES  |     | NULL    |       |
| party_name2_full_HUN_to   | date        | YES  |     | NULL    |       |
| party_name3_full_HUN      | varchar(60) | YES  |     | NULL    |       |
| party_name_full3_HUN_from | date        | YES  |     | NULL    |       |
| party_name_full3_HUN_to   | date        | YES  |     | NULL    |       |

### Prerequisites
- - - -

* MySQL installed ([link](https://dev.mysql.com/downloads/windows/installer/8.0.html))
* MySQL Service is running:
    * at Start menu, search for 'Services' ('szolgáltatások'),
    * search for MySQL,
    * if not running, start the process manually (right click, then 'start'),
    
    ![sqlrunnig](./Assets/sqlprocess.PNG)
    
    * user + pw (user has privilege to create, modify and delete databases)

### Export/Import created database

#### Common requirements

MySQL Service is running! (see details at Prerequisites)

- add mysql(.exe location) to PATH (environment variable):

    mysql.exe (default) location: C:\Program Files\MySQL\MySQL Server 8.0\bin

    - type in to command prompt: <br>
    `set path=C:\Program Files\MySQL\MySQL Server 8.0\bin`

- Check if ti was a success:

    - type in to command prompt: <br>
    `mysql -u root -p`

WARNING: by simply typing `mysql` you will got an error message:<br>
`ERROR 1045 (28000): Access denied for user 'ODBC'@'localhost' (using password: NO)`

This is because, for some reason, the ODBC user is the default username under windows even if you didn't create that user at setup time...

#### Export database

- In command line, change your folder to the default, where your databases are (dafault location: `C:\ProgramData\MySQL\MySQL Server 8.0\Data`)

- Enter (to command line):<br>
    `mysqldump -u username -p dbname > filename.sql`

    Where username, dbname and filename are filled appropriately (eg.:)

    `mysqldump -u root -p test > test.sql`

You should see the newly created file (ending with `.sql`) there!

#### Import existing database

- Open MySQL Shell, and create the databse you want to import:

    `create database test`
    
- Then, you have an empty database, you just have to import the previously saved data. Open cmd again, and switch to the folder, where your databases are (remember, dafault location is: C:\ProgramData\MySQL\MySQL Server 8.0\Data)

    Copy the previously created .sql file (**which you want to import**) into this folder!
    
- Type in to command line: 

    `mysql -u username -p dbname < filename.sql.`
    
    Where username, dbname and filename are filled appropriately, eg.:

    `mysql -u root -p test < test.sql`

(Enter your password if prompted to)

You have successfully imported your database! :) 

### Usage

#### Quick start

Before you can start, you should set some variables at `config.py`. These are the followings:

![database](./Assets/variable.PNG) <br>

Please set your HOST name, USER name and PASSWORD appropriately to your SQL credentials, and choose a desired name for the database to be created (DATABASE). <br>
Do not change the values of SENTENCE_ID and WORD_ID at the beginning. <br>

After the variables set up, take your `.xlsx` files to the projets' `/resources` folder, following the naming convention you see on github, at the example files. 


#### After creating a corpus

project/docs/docs/images/emotion_2.png

You can get the location of the generated database by following these steps:
- open MySQL Shell (installed with MySQL by default)<br>
![mysqlshell](./Assets/mysqlshell.PNG) <br>
- connect to mysql (type in `\sql`), then log in with your username (e.g.: `\connect root@localhost`, if you are using the root user to handle your databases). <br>
![connect](./Assets/connect.PNG)<br>
After, select the name of your newly generated database (specified in config.py, as "DATABASE" variable): <br><br>
![database](./Assets/variable.PNG) <br>
- type in: `SHOW VARIABLES WHERE Variable_Name LIKE "%dir" ;`. In the given list of variables, `datadir` will show the exact path to your database: <br>
![show](./Assets/datadir.PNG) <br>

The location of your corpus is determined by the [my.ini](https://www.tutorialspoint.com/can-t-find-my-ini-in-mysql-directory#:~:text=The%20my.,to%20the%20MySQL%20version%20directory.) file.
