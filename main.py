
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        counter = count_words(words)
        



def count_words(words):
    return len(words)


def count_characters(text):
    lowered_text = file_contents.lower()
    return lowered_text

#TODO:
# fix and complete the character function
# understand the conection between main and the other functions



if __name__ == "__main__":
    main()
