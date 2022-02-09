import json
import src.DAO
import pandas as pd

result = {}


def start(output_json: str) -> None:
    dao = src.DAO
    cursor, mydb = dao.get_database_reference()

    __create_parlamenti_ciklus(mydb)
    __create_cap_kod(mydb)
    __create_partok(mydb)
    __create_kepviselok(mydb)
    __create_felszolalasok(mydb)
    __create_kodolja(mydb)
    __create_mondatok(mydb)
    __create_conll_szavak(mydb)

    with open(output_json, "w", encoding="utf8") as json_file:
        json.dump(result, json_file, indent=4, ensure_ascii=False)


def __create_mondatok(mydb):
    query = "SELECT * FROM mondat;"
    df = pd.read_sql(query, mydb)

    mondatok_tmp = {}
    fields = df.columns
    for index, row in df.iterrows():
        mondat_tmp = {}
        for field_index, field in enumerate(fields):
            if field_index > 0:
                mondat_tmp[str(field)] = str(row[field])
        mondatok_tmp[str(row["mondat_id"])] = mondat_tmp     # primary key

    global result
    result["mondatok"] = mondatok_tmp


def __create_conll_szavak(mydb):
    query = "SELECT * FROM CONLL_SZO;"
    df = pd.read_sql(query, mydb)

    conll_szavak_tmp = {}
    fields = df.columns
    for index, row in df.iterrows():
        conll_szo_tmp = {}
        for field_index, field in enumerate(fields):
            if field_index > 0:
                conll_szo_tmp[str(field)] = str(row[field])
        conll_szavak_tmp[str(row["szo_id"])] = conll_szo_tmp     # primary key

    global result
    result["conll_szavak"] = conll_szavak_tmp



def __create_kodolja(mydb):
    query = "SELECT * FROM kodolja;"
    df = pd.read_sql(query, mydb)

    kodolja_tmp = {}
    for index, row in df.iterrows():
        kodolja_tmp[str(row['text_id'])] = str(row['major_topic'])  # egy-egy relációban álló elempár - legyenek: text_id -- major_topic

    global result
    result["kodolasok"] = kodolja_tmp


def __create_felszolalasok(mydb):

    query = "SELECT * FROM felszolalas;"
    df = pd.read_sql(query, mydb)

    felszolalasok_tmp = {}
    fields = df.columns
    for index, row in df.iterrows():
        felszolalas_tmp = {}
        for field_index, field in enumerate(fields):
            if field_index > 0:
                felszolalas_tmp[str(field)] = str(row[field])
        felszolalasok_tmp[str(row["text_id"])] = felszolalas_tmp     # primary key

    global result
    result["felszolalasok"] = felszolalasok_tmp


def __create_kepviselok(mydb):
    query = "SELECT * FROM kepviselo;"
    df = pd.read_sql(query, mydb)

    kepviselok_tmp = {}
    fields = df.columns
    for index, row in df.iterrows():
        kepviselo_tmp = {}
        for field_index, field in enumerate(fields):
            if field_index > 0:
                kepviselo_tmp[str(field)] = str(row[field])
        kepviselok_tmp[str(row["parliamentary_id"])] = kepviselo_tmp    # primary key

    global result
    result["kepviselok"] = kepviselok_tmp


def __create_cap_kod(mydb):
    query = "SELECT * FROM cap_kod;"
    df = pd.read_sql(query, mydb)

    cap_kodok_tmp = {}
    fields = df.columns
    for index, row in df.iterrows():
        cap_kod_tmp = {}
        for field_index, field in enumerate(fields):
            if field_index > 0:
                cap_kod_tmp[str(field)] = str(row[field])
        cap_kodok_tmp[str(row["cap_id"])] = cap_kod_tmp     # primary key

    global result
    result["cap_kodok"] = cap_kodok_tmp


def __create_parlamenti_ciklus(mydb):
    query = "SELECT * FROM parlamenti_ciklus;"
    df = pd.read_sql(query, mydb)

    ciklusok_tmp = {}
    fields = df.columns
    for index, row in df.iterrows():
        ciklus_tmp = {}
        for field_index, field in enumerate(fields):
            if field_index > 0:
                ciklus_tmp[str(field)] = str(row[field])
        ciklusok_tmp[str(row["cycle_number"])] = ciklus_tmp     # primary key

    global result
    result["ciklusok"] = ciklusok_tmp


def __create_partok(mydb):
    query = "SELECT * FROM part;"
    df = pd.read_sql(query, mydb)

    partok_tmp = {}
    fields = df.columns
    for index, row in df.iterrows():
        part_tmp = {}
        for field_index, field in enumerate(fields):
            if field_index > 0:                   # first index is the primary key, which is the "key" in the "big" dict
                part_tmp[str(field)] = str(row[field])
        partok_tmp[str(row["party_id"])] = part_tmp     # primary key

    global result
    result["partok"] = partok_tmp
