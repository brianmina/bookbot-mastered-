
def main():
    with open("/home/brian17/workspace/github.com2025/brianmina2025/bookbot-mastered-/books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_counter = count_words(words)
        print(word_counter)
        character_counter = count_characters(file_contents)
        print(character_counter)



def count_words(words):
    return len(words)


def count_characters(text):
    lowered_text = text.lower()
    counter = {}
    for c in lowered_text:
        if c not in counter:
            counter[c] = 1
        else:
            counter[c] += 1
    return counter

#TODO:
# create a report




if __name__ == "__main__":
    main()
