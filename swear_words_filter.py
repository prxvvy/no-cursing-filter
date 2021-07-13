"""
Read a file and returns a list of those words in it
"""


def read_file(file, type_to):
    with open(file, type_to, encoding="UTF8") as file_to_read:
        return [i.strip("\n") for i in file_to_read]


"""
Take two lists and return a dictionary
The items of l1 will be the keys and l2 will be the values
"""


def create_dic(l1, l2):
    dic = {}
    for i, j in zip(l1, l2):
        dic[i] = j
    return dic


"""
Take a dictionary containing the swear words as the keys and a its-ok-to-say word as their value of each key
Take a text possibly including a swear word
Replace the swear word for its its-ok-to-say word in that text and return that mutated text
"""


def replace_word(dic, text):
    for k, v in dic.items():
        if k in text:
            text = text.replace(k, v)
    return text


def main():
    # Files' names are just a sample
    swears = read_file("swearwords.txt", "r")
    ok_words = read_file("itsoktosaywords.txt", "r")
    dic = create_dic(swears, ok_words)
    text = input("Type anything in: ")
    with open("mutatedmgs", "a", encoding="UTF8") as final_file:
        final_file.write(replace_word(dic, text) + "\n")


if __name__ == "__main__":
    main()
