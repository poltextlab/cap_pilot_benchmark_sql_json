import pandas as pd
import src.DAO
import src.loadExcelToDataframe
from collections import defaultdict
import src.handle_text_analysis
import hu_core_news_lg
import config


# import previously saved ones at the beginning, but only modify them when we generate the last table (felszolalas)
# where they actually used

sentence_id = config.SENTENCE_ID
word_id = config.WORD_ID


def populate_table(name: str,
                   df: pd.DataFrame,
                   nlp: hu_core_news_lg,
                   drop: bool = False) -> None:
    """
    Method to switch between creatable tables based on "name" parameter. Use only with tables that without FOREIGN KEYS!

    :param nlp: only used when FELSZOLALAS table is generated
    :param drop: If True, then the potentially existing earlier version of the table is Dropped at the beginning of the
    process.
    :param name: name of the created Table in SQL
    :param df: Dataframe that contains the records to be inserted
    :return:
    """

    if name == "parlamenti_ciklus":
        __populate_table_parlamenti_ciklus(df, drop)
    elif name == "cap_code":
        __populate_table_cap_code(df, drop)
    elif name == "part":
        __populate_table_part(df, drop)
    elif name == "kepviselo":
        __populate_table_kepviselo(df, drop)
    elif name == "felszolalas":
        __populate_table_felszolalas(df, drop, nlp)
    else:
        raise NameError(name + " table not found in Schema! ")


def __populate_table_felszolalas(df: pd.DataFrame, drop: bool, nlp: hu_core_news_lg) -> None:
    """
    Creates the FELSZOLALAS table in the database.

    :param df: Input dataframe that contains the records' raw data.
    :param drop: If true, the previous version of the table is deleted at the beginning of the process.
    :param nlp: language model that the underlying functions use the generate records for MONDAT and CONLL_SZO tables
    during the process
    :return: None
    """

    dao = src.DAO

    text_analysis = src.handle_text_analysis

    if drop:
        drop_stmt = """DROP TABLE IF EXISTS `felszolalas` """
        dao.execute_statement(drop_stmt)

    for index, row in df.iterrows():

        text_id = row['text_id']
        exact_date = __replace_zero_to_none(row['exact_date'])
        tokenszam = __replace_zero_to_none(row['tokenszam'])
        text = __replace_zero_to_none(row['text'])
        napirendi_pont = __replace_zero_to_none(row['napirendi_pont'])
        video_felszolalas_ido = __replace_zero_to_none(row['video_felszolalas_ido'])
        video_feszolalas_url = __replace_zero_to_none(row['video_feszolalas_url'])
        felszolalas_url = __replace_zero_to_none(row['felszolalas_url'])
        cycle_number = __replace_zero_to_none(row['cycle_number'])
        parliamentary_id = __replace_zero_to_none(row['parliamentary_id'])
        covid = __replace_zero_to_none(row['COVID'])

        insert_statement = ("INSERT INTO `felszolalas` (`text_id`, `exact_date`, `tokenszam`, `text`, `napirendi_pont`, `video_felszolalas_ido`, `video_feszolalas_url`, `felszolalas_url`, `covid`, `cycle_number`, `parliamentary_id`) " "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data = (text_id, exact_date, tokenszam, text, napirendi_pont, video_felszolalas_ido, video_feszolalas_url, felszolalas_url, covid, cycle_number, parliamentary_id)
        dao.execute_insert(insert_statement, data)

        major_topic = __replace_zero_to_none(row['major_topic'])
        insert_statement = ("INSERT INTO `kodolja` (`text_id`, `major_topic`) " "VALUES(%s, %s)")
        data = (text_id, major_topic)
        dao.execute_insert(insert_statement, data)

        # creation of "mondat" and "CONLL_SZO" records in the corresponding tables
        global sentence_id, word_id
        sentence_id, word_id = text_analysis.process_text(nlp, text_id, text, sentence_id, word_id)
        print(f"{index} records created in FELSZOLALAS table...")

    # global sentence_id, word_id
    # print(f"Please update SENTENCE_ID variable to {sentence_id}, and WORD_ID variable to {word_id} in config.py file, "
    #       f"if you are planning to expand this database later!")


def __populate_table_kepviselo(df: pd.DataFrame, drop: bool) -> None:
    """
    Creates the KEPVISELO table in the database.

    :param df: Input dataframe that contains the records' raw data.
    :param drop: If true, the previous version of the table is deleted at the beginning of the process.
    :return: None
    """

    dao = src.DAO

    if drop:
        drop_stmt = """DROP TABLE IF EXISTS `kepviselo` """
        dao.execute_statement(drop_stmt)

    # party_id -hoz előbb be kell olvasni a párt-képviselő kapcsolatokat tartalmazó táblát egy dict-be
    reader = src.loadExcelToDataframe
    df_party_person = reader.load("C:\\Users\\uvege\\PycharmProjects\\xlsToSQL\\resoures\\party_person.xlsx")
    dict_party_person = dict()

    for index, row in df_party_person.iterrows():
        if row['parliamentary_id'] not in dict_party_person:
            dict_party_person[row['parliamentary_id']] = [row['party_id'], row['party_pers_from'], row['party_pers_to']]
        else:
            dict_party_person[row['parliamentary_id']].append([row['party_id'], row['party_pers_from'], row['party_pers_to']])

    for index, row in df.iterrows():

        parliamentary_id = row['parliamentary_id']
        birth_year = __replace_zero_to_none(row['birth_year'])
        birth_place = __replace_zero_to_none(row['birth_place'])
        sex = __replace_zero_to_none(row['sex'])
        death_date = __replace_zero_to_none(row['death_date'])
        death_place = __replace_zero_to_none(row['death_place'])
        first_name = __replace_zero_to_none(row['first_name'])
        surname = __replace_zero_to_none(row['surname'])
        change_name = __replace_zero_to_none(row['change_name'])
        surname_new = __replace_zero_to_none(row['surname_new'])
        surname_from = __replace_zero_to_none(row['surname_from'])
        try:
            party_id = __replace_zero_to_none(dict_party_person[parliamentary_id][0][0])
        except:
            party_id = None

        insert_statement = ("INSERT INTO `kepviselo` (`parliamentary_id`, `birth_year`, `birth_place`, `sex`, `death_date`, `death_place`, `first_name`, `surname`, `change_name`, `surname_new`, `surname_from`, `party_id`) " "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data = (parliamentary_id, birth_year, birth_place, sex, death_date, death_place, first_name, surname, change_name, surname_new, surname_from, party_id)
        dao.execute_insert(insert_statement, data)


def __populate_table_part(df: pd.DataFrame, drop: bool) -> None:
    """
    Creates the PART table in the database.

    :param df: Input dataframe that contains the records' raw data.
    :param drop: If true, the previous version of the table is deleted at the beginning of the process.
    :return: None.
    """

    dao = src.DAO

    if drop:
        drop_stmt = """DROP TABLE IF EXISTS `part` """
        dao.execute_statement(drop_stmt)

    for index, row in df.iterrows():

        party_id = row['party_id']
        party_name_full_HUN = __replace_zero_to_none(row['party_name_full_HUN'])
        party_name_full_HUN_from = __replace_zero_to_none(row['party_name_full_HUN_from'])
        party_name_full_HUN_to = __replace_zero_to_none(row['party_name_full_HUN_to'])
        party_name2_full_HUN = __replace_zero_to_none(row['party_name2_full_HUN'])
        party_name2_full_HUN_from = __replace_zero_to_none(row['party_name2_full_HUN_from'])
        party_name2_full_HUN_to = __replace_zero_to_none(row['party_name2_full_HUN_to'])
        party_name3_full_HUN = __replace_zero_to_none(row['party_name3_full_HUN'])
        party_name_full3_HUN_from = __replace_zero_to_none(row['party_name_full3_HUN_from'])
        party_name_full3_HUN_to = __replace_zero_to_none(row['party_name_full3_HUN_to'])

        insert_statement = ("INSERT INTO `part` (`party_id`, `party_name_full_HUN`, `party_name_full_HUN_from`, `party_name_full_HUN_to`, `party_name2_full_HUN`, `party_name2_full_HUN_from`, `party_name2_full_HUN_to`, `party_name3_full_HUN`, `party_name_full3_HUN_from`, `party_name_full3_HUN_to`) " "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data = (party_id, party_name_full_HUN, party_name_full_HUN_from, party_name_full_HUN_to, party_name2_full_HUN, party_name2_full_HUN_from, party_name2_full_HUN_to, party_name3_full_HUN, party_name_full3_HUN_from, party_name_full3_HUN_to)
        dao.execute_insert(insert_statement, data)


def __populate_table_cap_code(df: pd.DataFrame, drop: bool) -> None:
    """
    Creates the CAP_KOD table in the database.

    :param df: Input dataframe that contains the records' raw data.
    :param drop: If true, the previous version of the table is deleted at the beginning of the process.
    :return: None.
    """

    dao = src.DAO

    if drop:
        drop_stmt = """DROP TABLE IF EXISTS `cap_kod` """
        dao.execute_statement(drop_stmt)

    # Insert the records to it
    for index, row in df.iterrows():

        cap_id = row['cap_id']
        nev_magyar = __replace_zero_to_none(row['nev_magyar'])
        nev_angol = __replace_zero_to_none(row['nev_angol'])

        insert_statement = ("INSERT INTO `cap_kod` (`cap_id`, `nev_magyar`, `nev_angol`) " "VALUES(%s, %s, %s)")
        data = (cap_id, nev_magyar, nev_angol)
        dao.execute_insert(insert_statement, data)


def __populate_table_parlamenti_ciklus(df: pd.DataFrame, drop: bool) -> None:
    """
    Creates the PARLAMENTI_CIKLUS table in the database.

    :param df: Input dataframe that contains the records' raw data.
    :param drop: If true, the previous version of the table is deleted at the beginning of the process.
    :return: None.
    """

    dao = src.DAO

    if drop:
        drop_stmt = """DROP TABLE IF EXISTS `parlamenti_ciklus` """
        dao.execute_statement(drop_stmt)

    # Insert the records to it
    for index, row in df.iterrows():

        cycle_number = row['cycle_number']
        cycle_years_from = __replace_zero_to_none(row['cycle_years_from'])
        cycle_years_to = __replace_zero_to_none(row['cycle_years_to'])
        cycle_from = __replace_zero_to_none(row['cycle_from'])
        cycle_to = __replace_zero_to_none(row['cycle_to'])

        insert_statement = ("INSERT INTO `parlamenti_ciklus` (`cycle_number`, `cycle_years_from`, `cycle_years_to`, `cycle_from`, `cycle_to`) " "VALUES(%s, %s, %s, %s, %s)")
        data = (cycle_number, cycle_years_from, cycle_years_to, cycle_from, cycle_to)
        dao.execute_insert(insert_statement, data)


def __replace_zero_to_none(value):
    """
    Helper function to generate Null values for the database, where data is missing from the input.

    :param value: 0 or None
    :return: None value if input == 0, original input otherwise
    """

    return None if value == 0 else value
