# ------------------------Imports-------------------------- #
import mysql.connector
from time import sleep
import os

# --------------------------------------------------------- #

__copyright__ = "WTFPL - http://www.wtfpl.net/about/"
__credit__ = ["Helgi"]


def test_if_number(text, float_or_int):
    # Function that tests if the value entered is a number or not.
    while True:
        try:
            # If the input gets an error (e.g. string entered) the code will stop and "return" wont run.
            question = float_or_int(input(text))
            return question
        except ValueError:
            # When the code stops "except" will run and tells the user to try again and there it loops again.
            # This way the code wont crash of the user enters something i don't want.
            print("Not a number.. Try again.")


def run_again():
    # Function that asks the user if he wants to run the just executed code again
    yes_list = ["ja", "já", "jamm", "j", "jam", "y", "ye", "yes", "ya", "mhm", "yep"]  # Both Icelandic and English
    no_list = ["nei", "ne", "na", "n", "no", "huh", "nje", "nah", "nop", "nope"]  # Both Icelandic and English
    while True:
        question = input("\nDo you want to run that code again?[Y/N]: ")
        # The code checks if the entered value is in one of the lists and return either 1 or 0 depending on the results.
        if question.lower() in yes_list:
            p_nr = 1
            return p_nr
        elif question.lower() in no_list:
            p_nr = 0
            return p_nr
        else:
            print("Don't understand you...")


class ConnectAndCommit:
    def __init__(self, query):
        self.query = query
        # self.data = data
        self.connection = None  # The reason for this is to get rid of an annoying PEP8 warning
        self.cursor = None  # The reason for this is to get rid of an annoying PEP8 warning

    def est_connection(self):
        self.connection = mysql.connector.connect(
            user='helgiste_test',
            password='ab123',
            host='108.167.160.53',
            database='helgiste_DataProject'
        )

    def execute_n_commit(self):
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, """ self.data""")

        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()


class Data:
    def __init__(self):
        pass

    def get_text_data(self):
        Inpdata = input("Type here: ")
        query = ("INSERT INTO test"
                 "(name, secname) "
                 "VALUES ('" + Inpdata + "', 'johnson')")
        cac = ConnectAndCommit(query)
        cac.est_connection()
        cac.execute_n_commit()
        cac.close_connection()



class Choices:
    def __init__(self):
        pass

    def choice_add_data(self):
        print("Kind of data\n[1]Text i enter")
        choice = test_if_number(">: ", int)
        if choice == 1:
            data = Data()
            data.get_text_data()


def main():

    """os.system("start data_logo.cmd")
    print("Starting up", end="", flush=True)
    for i in range(4):
        print(".", end="", flush=True)
        sleep(1)"""

    print("\n " + "_" * 29, "\n| What do you want to do?     |\n|[1]Display all my data       |")
    print("|[2]Add data")
    main_choice = test_if_number(">: ", int)
    choice = Choices()
    if main_choice == 2:
        choice.choice_add_data()




if __name__ == '__main__':
    main()


# ---DUMP-MIGHT-BE-USED-LATER--- #

"""

-[OPEN LOGO - start]- (Used before data_logo.cmd)

def open_logo():
    line_list = []
    with open("DataShit.txt", "r") as logo:
        file_list = logo.read().split("\n")
        for i in range(len(file_list)):
            line_list.append(file_list[i])
        return line_list


line_list = open_logo()
longest_line = 0
length = 0
for i in range(len(line_list)):
    if len(line_list[i]) > longest_line:
        longest_line = len(line_list[i])
    length = longest_line + 4
print(" " + "".rjust(length + 3, "_"))
for i in range(len(line_list)):
    print("|", line_list[i], " ".rjust(length - len(line_list[i])), "|")
print("|" + "".rjust(length + 3, "_") + "|")

-[OPEN LOGO - End]-
"""