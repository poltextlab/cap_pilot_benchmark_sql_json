import src.DAO


def create_all(drop: bool = False) -> None:
    """
    Initializes the Database AND create all the tables (Schema creation).

    :param drop: If True, the already existing table are DROPped at the beginning of the process
    :return: None
    """

    dao = src.DAO
    dao.delete_database()
    dao.start()

    # delete previous version if asked
    if drop:
        drop_stmt = """DROP TABLE IF EXISTS `parlamenti_ciklus` """
        dao.execute_statement(drop_stmt)
        drop_stmt = """DROP TABLE IF EXISTS `part` """
        dao.execute_statement(drop_stmt)
        drop_stmt = """DROP TABLE IF EXISTS `kepviselo` """
        dao.execute_statement(drop_stmt)
        drop_stmt = """DROP TABLE IF EXISTS `felszolalas` """
        dao.execute_statement(drop_stmt)
        drop_stmt = """DROP TABLE IF EXISTS `cap_kod` """
        dao.execute_statement(drop_stmt)
        drop_stmt = """DROP TABLE IF EXISTS `kodolja` """
        dao.execute_statement(drop_stmt)
        drop_stmt = """DROP TABLE IF EXISTS `mondat` """
        dao.execute_statement(drop_stmt)
        drop_stmt = """DROP TABLE IF EXISTS `CONLL_SZO` """
        dao.execute_statement(drop_stmt)


    # create new version of the Table
    stmt = """
    CREATE TABLE IF NOT EXISTS `parlamenti_ciklus` (
      `cycle_number` INT(2) PRIMARY KEY NOT NULL,
      `cycle_years_from` INT(4),
      `cycle_years_to` INT(4),
      `cycle_from` DATE,
      `cycle_to` DATE
    )
    """
    dao.execute_statement(stmt)

    stmt = """
     CREATE TABLE IF NOT EXISTS `part` (
       `party_id` INT(3) PRIMARY KEY NOT NULL,
       `party_name_full_HUN` VARCHAR(60),
       `party_name_full_HUN_from` DATE,
       `party_name_full_HUN_to` DATE,
       `party_name2_full_HUN` VARCHAR(60),
       `party_name2_full_HUN_from` DATE,
       `party_name2_full_HUN_to` DATE,
       `party_name3_full_HUN` VARCHAR(60),
       `party_name_full3_HUN_from` DATE,
       `party_name_full3_HUN_to` DATE
     )
     """
    dao.execute_statement(stmt)

    stmt = """
     CREATE TABLE IF NOT EXISTS `kepviselo` (
       `parliamentary_id` VARCHAR(100) PRIMARY KEY NOT NULL,
       `seat_type` VARCHAR(20),
       `seniority` VARCHAR(20),
       `birth_year` INT(4),
       `birth_place` VARCHAR(30),
       `sex` INT(1),
       `death_date` DATE,
       `death_place` VARCHAR(20),
       `first_name` VARCHAR(20),
       `surname` VARCHAR(30),
       `change_name` BOOLEAN,
       `surname_new` VARCHAR(20),
       `surname_from` DATE,
       `party_id` INT(3),
       FOREIGN KEY (`party_id`) REFERENCES part(`party_id`)
     )
     """
    dao.execute_statement(stmt)

    stmt = """
     CREATE TABLE IF NOT EXISTS `felszolalas` (
       `text_id` VARCHAR(20) PRIMARY KEY NOT NULL,
       `exact_date` DATE,
       `tokenszam` INT(4),
       `text` TEXT,
       `napirendi_pont` VARCHAR(400),
       `video_felszolalas_ido` TIME,
       `video_feszolalas_url` VARCHAR(200),
       `felszolalas_url` VARCHAR(500),
       `cycle_number` INT(2),
       `parliamentary_id` VARCHAR(100),
       FOREIGN KEY (`cycle_number`) REFERENCES parlamenti_ciklus(`cycle_number`),
       FOREIGN KEY (`parliamentary_id`) REFERENCES kepviselo(`parliamentary_id`)
     )
     """
    dao.execute_statement(stmt)

    stmt = """
     CREATE TABLE IF NOT EXISTS `cap_kod` (
       `cap_id` INT(2) PRIMARY KEY NOT NULL,
       `nev_magyar` VARCHAR(100), 
       `nev_angol` VARCHAR(100)
     )
     """
    dao.execute_statement(stmt)

    stmt = """
     CREATE TABLE IF NOT EXISTS `kodolja` (
       `major_topic` INT(2),
       `text_id` VARCHAR(20),
       FOREIGN KEY (`text_id`) REFERENCES FELSZOLALAS(`text_id`),
       FOREIGN KEY (`major_topic`) REFERENCES cap_kod(`cap_id`)
     )
     """
    dao.execute_statement(stmt)

    stmt = """
     CREATE TABLE IF NOT EXISTS `mondat` (
       `mondat_id` INT(6) PRIMARY KEY NOT NULL,
       `raw_text` TEXT,
       `text_id` VARCHAR(20),
       FOREIGN KEY (`text_id`) REFERENCES FELSZOLALAS(`text_id`)
     )
     """
    dao.execute_statement(stmt)

    stmt = """
     CREATE TABLE IF NOT EXISTS `CONLL_SZO` (
       `szo_id` INT(8) PRIMARY KEY NOT NULL,
       `sorszam` INT(3),
       `szoalak` VARCHAR(40),
       `lemma` VARCHAR(40),
       `entity_IOB` VARCHAR(10),
       `POS` VARCHAR(20),
       `morf_analysis` VARCHAR(100),
       `dependencia_el` VARCHAR(20),
       `mondat_id` INT(6),
       FOREIGN KEY (`mondat_id`) REFERENCES MONDAT(`mondat_id`)
     )
     """
    dao.execute_statement(stmt)