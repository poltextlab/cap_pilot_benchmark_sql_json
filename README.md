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
| COVID                 | int          | YES  |     | NULL    |       |
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
    * at Start menu, search for 'Services' ('szolg??ltat??sok'),
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

IMPORTANT: In `main.py`, please set the `CREATE_SQL` variable to 'True'!


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

### json generation functionality

AFTER creating an SQL corpus, you have the opportunity to create a corresponding .json file, which mirrors the structure the SQL database.

If you want to do so, please set the followings:<br> 

- In `config.py`, plese specify the realtive path for the desired json file, e.g.: `OUTPUT_JSON = "resoures/tk_parlament.json"`
- In `main.py`, please set the `CREATE_JSON_AFTER_SQL` variable to 'True'

Prerequisite: the json generation just mirrors the **already existing** SQL databases' structure to a json file! Your sql file must exist, and available (see Prerequisits; 
MySQL service is installed and running, etc.) before you can start the json generation (meaning: you can create the sql AND the json at the same time \[both `CREATE_SQL` 
and `CREATE_JSON_AFTER_SQL` variables set True\], or you can create the SQL, and later, you can crate the json separately!)

#### Example (entries in json file)

In the json file, you will find the following keys:

- "ciklusok"
- "cap_kodok"
- "partok"
- "kepviselok"
- "felszolalasok"
- "kodolasok"
- "mondatok"
- "conll_szavak"

Each key contains a dictionary itself. In this dictionaries, the keys are the primary keys from the corresponding SQL tables 
(pairs: 

- ciklusok\[json]  - parlamenti_ciklus\[SQL], 
- partok\[json] - part\[SQL]
- kepviselok\[json] - kepviselo\[SQL]
- felszolalasok\[json] - felszolalas\[SQL]
- cap_kodok\[json] - cap_kod\[SQL]
- kodolasok\[json] - kodolja\[SQL]
- mondatok\[json] - mondat\[SQL]
- conll_szavak\[json] - CONLL_SZO\[SQL]
)

Example entries in the json file: 

##### ciklusok

        "1": {
            "cycle_years_from": "1990",
            "cycle_years_to": "1994",
            "cycle_from": "1990-05-02",
            "cycle_to": "1994-06-27"
        },
        "2": { ...`

##### partok

`        "1": {
            "party_name_full_HUN": "Agr??rsz??vets??g",
            "party_name_full_HUN_from": "1990-05-02",
            "party_name_full_HUN_to": "1997-02-22",
            "party_name2_full_HUN": "Agr??rsz??vets??g - Nemzeti Agr??rp??rt",
            "party_name2_full_HUN_from": "1997-02-22",
            "party_name2_full_HUN_to": "1998-06-17",
            "party_name3_full_HUN": "None",
            "party_name_full3_HUN_from": "None",
            "party_name_full3_HUN_to": "None"
        },
        "2": { ... `

##### kepviselok

`        "a001": {
            "seat_type": "None",
            "seniority": "None",
            "birth_year": "1951.0",
            "birth_place": "K??tegyh??za",
            "sex": "1.0",
            "death_date": "None",
            "death_place": "None",
            "first_name": "Gy??rgy",
            "surname": "??rgy??l??n",
            "change_name": "None",
            "surname_new": "None",
            "surname_from": "None",
            "party_id": "nan"
        },
        "a003": { ... `

##### felszolalasok

`"1": {
            "exact_date": "2014-05-12",
            "tokenszam": "665",
            "text": "DR. SCHIFFER ANDR??S (LMP): K??sz??n??m a sz??t, eln??k ??r. Tisztelt Orsz??ggy??l??s! Szombaton, negyedsz??zad ut??n el??sz??r korm??nyprogram n??lk??l v??lasztott minisztereln??k??t az Orsz??ggy??l??s. ??n??k annyit mondtak, hogy folytatj??k. Mit folytatnak? Az elm??lt n??gy ??vben Magyarorsz??gon a GDP 2,1 sz??zal??kkal emelkedett, mik??zben az eur??pai uni??s ??tlag 4,4 sz??zal??k, a rom??n 5,3, a szlov??k 9 f??l??tt, a lengyel 12 sz??zal??k ugyanebben az id??szakban, a bolg??r majdnem 4 sz??zal??k. Ha ??n??k ??gy folytatj??k, 2020-ra Magyarorsz??g Eur??pa szeg??nyh??za lesz. Mit folytatnak? Az ??llamad??ss??g ??pp??gy 80 sz??zal??k k??r??l van, mint amikor ??n??k ??tvett??k a korm??nyrudat, k??zben leny??ltak 3000 milli??rdot a mag??n-nyugd??jp??nzt??ri megtakar??t??sokb??l, teh??t ennyi ad??ss??got halmoztak fel a k??vetkez?? gener??ci??k fel??. A paksi hitelszerz??d??s ??jabb 3000 milli??rdos plusz ad??ss??gteher, teh??t ??gy ??sszess??g??ben az fenyeget, hogy val??j??ban az ??llamad??ss??g a GDP 100 sz??zal??ka f??l?? tud ugrani, ez??rt k??vetelj??k t??bbek k??z??tt a paksi szerz??d??s azonnali felmond??s??t. Mit folytatnak? El sem kezdt??k a j??vedelemszivatty??knak az elz??r??s??t, hiszen az offshore-biznisz ma is vir??gzik Magyarorsz??gon, a l??ncolatos ??facsal??sok kivizsg??l??s??t megakad??lyozt??k, ellenben k??tik a strat??giai partners??gi meg??llapod??sokat nagy multic??gekkel, amelyek a transzfer??rakon kereszt??l hatalmas j??vedelmeket szivatty??znak ki, ??s m??jus 1-j??t??l szabad a gazda a term??f??ld-spekul??ci?? el??tt. Mit folytatnak? Hiszen 2010 ??ta nincs t??bb meg??lhet??st ad?? munkahely, viszont egyre t??bb a dolgoz?? szeg??ny Magyarorsz??gon. Az a helyzet, hogy a minim??lb??rt hi??ba emelt??k 38 sz??zal??kkal, a nett?? b??remelked??s 10 sz??zal??k volt az elm??lt n??gy ??vben. Az ad????k emelkedett meg, az OECD-tagorsz??gokon bel??l a negyedik legmagasabb Magyarorsz??gon. Ma a magyar emberek kevesebb p??nz??rt t??bbet dolgoznak, hiszen az ??j munka t??rv??nyk??nyve azt is lehet??v?? tette, hogy a t??l??rap??nznek, a p??tl??koknak reszeljenek, n?? a munkaid??, cs??kken a szabads??g. Tisztelt Orsz??ggy??l??s! 2009-r??l 2012-re a fels?? j??vedelmi tizednek a j??vedelme majdnem 18 sz??zal??kkal n??tt, mik??zben az als?? tizednek m??r 2007 ??ta folyamatosan romlanak a j??vedelmi viszonyai, az elm??lt n??gy ??vben 6 sz??zal??kkal cs??kkent. T??z ??vvel ezel??tt a j??vedelemk??l??nbs??g h??tszeres volt Magyarorsz??gon, az elm??lt n??gy ??vben kilencszeres??re n??tt. Magyarorsz??gon a szeg??nys??g, a n??lk??l??z??sben ??l??k ar??nya a legnagyobb az Eur??pai Uni??n bel??l, 26 sz??zal??kos, G??r??gorsz??g a m??sodik 20 sz??zal??kkal. Az Uni??n bel??l 4 sz??zal??kkal n??tt a szeg??nys??g, Magyarorsz??gon 14 sz??zal??kkal. Aligha gondolhatjuk azt, hogy az a j??vedelmi helyzet alapvet??en v??ltozni fog, hogy a keres??knek a k??tharmada Magyarorsz??gon a 225 ezer forintos ??tlagkereset alatt keres, hiszen am??g a nemzetgazdas??g nem termel hozz??adott ??rt??ket, a magyar b??rek a nyom??ban sem lesznek az eur??pai b??reknek. De hogyan is lenne v??ltoz??s akkor, amikor az oktat??snak a GDP-ar??nyos h??nyada folyamatosan zuhan? 2003-ban majdnem 6 sz??zal??k volt, 2011-ben 4,3 sz??zal??k. A fels??oktat??sb??l ??ves szinten hossz?? ??vek ??ta 60-70 milli??rdot vonnak ki, 1,5 sz??zal??k alatt van a fels??oktat??snak a GDP-ar??nyos r??szar??nya. Magyarorsz??g az elm??lt n??gy ??vben a 300 ezer k??zmunk??s orsz??ga lett, a k??zmunk??b??l ??l??k k??z??l 2013-ban ??sszesen 17 ezren, alig 6 sz??zal??k az, aki el tudott helyezkedni az els??dleges munkaer??piacon. Magyarorsz??g a 28 uni??s tag??llam k??z??tt 24. a foglalkoztat??s tekintet??ben, ??s a fiatalok k??z??tt m??g riaszt??bb a tendencia: ma m??r 12 sz??zal??ka a fiataloknak korai iskolaelhagy??, holott a c??lkit??z??s az Eur??pai Uni??n bel??l 2020-ra 10 sz??zal??k lenne. N??tt a birtokkoncentr??ci?? az elm??lt n??gy ??vben, az agr??rt??mogat??sok nagy r??sz??t a fels?? 10 sz??zal??k nyeli le. Azt l??tjuk, hogy mik??zben n?? az elv??ndorl??s, hiszen n??h??ny ??v alatt 2,5-szeres??re n??vekedett azoknak a fiataloknak az ar??nya, akik el akarj??k hagyni ezt az orsz??got, lassan a munka??gyi statisztik??kat az tudja kozmetik??zni, hogy h??nyan dolgoznak Londonban. Ha ??n??k ezt folytatj??k, a magyar t??rsadalom egy k??zmunkaalap?? t??rsadalom lesz, Magyarorsz??g pedig egy unok??k n??lk??li ??sszeszerel?? orsz??g marad. K??sz??n??m sz??pen. (Taps az LMP ??s a f??ggetlen k??pvisel??k soraiban.)",
            "napirendi_pont": "Mit folytatnak?",
            "video_felszolalas_ido": "0 days 05:04:00",
            "video_feszolalas_url": "https://sgis.parlament.hu/archive/playseq.php?date1=20140512&time1=121752&offset1=001901.201&date2=20140512&time2=121752&offset2=002405.96&type=real",
            "felszolalas_url": "https://www.parlament.hu:443/web/guest/orszaggyulesi-naplo-elozo-ciklusbeli-adatai?p_p_id=hu_parlament_cms_pair_portlet_PairProxy_INSTANCE_9xd2Wc9jP4z8&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&p_auth=JieFdrJ9&_hu_parlament_cms_pair_portlet_PairProxy_INSTANCE_9xd2Wc9jP4z8_pairAction=%2Finternet%2Fcplsql%2Fogy_naplo.naplo_fadat%3Fp_ckl%3D40%26p_uln%3D3%26p_felsz%3D2%26p_szoveg%3D%26p_felszig%3D2",
            "covid" : "0",
            "cycle_number": "7",
            "parliamentary_id": "s100"
        },
        "10": { ... `

##### cap_kodok

`        "1": {
            "nev_magyar": "Macroeconomics",
            "nev_angol": "Makrogazdas??gi politika"
        },
        "2": { ... `

##### kodolasok

(Schema: "text_id" : "major_topic")

`"1": "1", ...
`

##### mondatok

`        "0": {
            "raw_text": "DR. SCHIFFER ANDR??S (LMP): K??sz??n??m a sz??t, eln??k ??r.",
            "text_id": "1"
        },
        "1": { ...`

##### conll_szavak

`        "0": {
            "sorszam": "0",
            "szoalak": "DR.",
            "lemma": "DR.",
            "entity_IOB": "O ",
            "POS": "PROPN",
            "morf_analysis": "Case=Nom|Number=Sing",
            "dependencia_el": "nsubj",
            "mondat_id": "0"
        },
        "1": { ...`