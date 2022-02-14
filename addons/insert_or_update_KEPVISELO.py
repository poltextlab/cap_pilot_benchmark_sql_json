import src.DAO


def main():
    dao = src.DAO
    cursor, mydb = dao.get_database_reference()


if __name__ == '__main__':
    main()
