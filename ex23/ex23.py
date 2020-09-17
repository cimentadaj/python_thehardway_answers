import wget
import sys

wget.download(
    "https://learnpythonthehardway.org/python3/languages.txt",
    "./languages.txt"
)

script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    # Removes any leading/trailing spaces, /n or any args
    # you might provide as arguments
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<=====>", cooked_string)

languages = open("./languages.txt", encoding="utf-8")
main(languages, input_encoding, error)

# my_list = [1, 2, 3, 4]

# def summer(a):
#     print(a)
#     a[0] = a[0] + a[1]
#     a.pop(1)

#     if len(a) != 1:
#         summer(a)

#     return a

# res = summer(my_list)
