import ast

"""
First, execute statement in MySQL Shell:

    select * from conll_szo where entity_IOB IN ("B ORG", "B LOC", "B PER", "B MISC", "I ORG", "I LOC", "I PER", "I MISC") INTO OUTFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/test.txt";

It results a file named "test.txt". This python script uses this file!

IMPORTANT: Insert this line as a first line into "test.txt":
0	0	0	0	0	0	0	0	0

Please define the expected output file at line 17!
"""

OUTPUT = "C:\\Users\\uvege\\OneDrive\\Asztali gép\\test\\Named_Entities.txt"

def main():

    entities = {}
    aslist = []

    with open("C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\test.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            tmp_line = line.replace("\n", "")
            aslist.append(tmp_line.split("\t"))

        tmp_NE = ""

        for index, line_array in enumerate(aslist):
            # ez is, és az előző is "B" vel kezdődik
            if line_array[4].startswith("B") and aslist[index-1][4].startswith("B"):
                # az előzőt beteszük a dict -be
                if tmp_NE not in entities:
                    entities[tmp_NE] = 1
                else:
                    entities[tmp_NE] += 1
                # eltároljuk a jelenlegit
                tmp_NE = line_array[3]
            elif line_array[4].startswith("B") and aslist[index-1][4].startswith("I"):
                # az előzőt beteszük a dict -be
                if tmp_NE not in entities:
                    entities[tmp_NE] = 1
                else:
                    entities[tmp_NE] += 1
                # eltároljuk a jelenlegit
                tmp_NE = line_array[3]
            else:
                tmp_NE += " "
                tmp_NE += line_array[3]

        with open(OUTPUT, "w+", encoding="utf8") as output:
            for key, value in entities.items():
                output.write(key + "\t" + str(value) + "\n")


if __name__ == '__main__':
    main()
