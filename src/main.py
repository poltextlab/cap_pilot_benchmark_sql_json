import src.DAO
import src.loadExcelToDataframe
import src.populate_tables
import src.handle_text_analysis
import src.create_tables
import hu_core_news_lg
import datetime

dao = None
df = None
nlp = None

# test runtime
start_time = None
end_time = None
RUNTIME_TEST = False


def main():

    if RUNTIME_TEST:
        start_time = datetime.datetime.now()

    loader = src.loadExcelToDataframe
    creator = src.create_tables
    creator.create_all(True)

    nlp = hu_core_news_lg.load()

    files = {
        "parlamenti_ciklus" : "resoures/cycle_kész.xlsx",
        "cap_code" : "resoures/CAP_CODE.xlsx",
        "part" : "resoures/party_name_full_hun.xlsx",
        "kepviselo" : "resoures/demo_kész.xlsx",
        "felszolalas" : "resoures/text_jav.xlsx"
    }

    inserter = src.populate_tables
    inserter.populate_table("parlamenti_ciklus", loader.load(files["parlamenti_ciklus"]), nlp)
    print("parlamenti_ciklus created")

    inserter.populate_table("cap_code", loader.load(files["cap_code"]), nlp)
    print("cap_code created")

    inserter.populate_table("part", loader.load(files["part"]), nlp)
    print("part created")

    inserter.populate_table("kepviselo", loader.load(files["kepviselo"]), nlp)      # reads "resoures/party_person.xlsx" internally!
    print("kepviselo created")

    inserter.populate_table("felszolalas", loader.load(files["felszolalas"]), nlp)
    print("felszolalas created")
    print("Database creation sucessfully finished!")

    if RUNTIME_TEST:
        end_time = datetime.datetime.now()
        time_diff = (end_time - start_time)
        execution_time = time_diff.total_seconds() * 1000
        print(f"Elapsed time : {execution_time} ms")


if __name__ == '__main__':
    main()
