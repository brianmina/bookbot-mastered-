
def main():
    with open("/home/brian17/workspace/github.com2025/brianmina2025/bookbot-mastered-/books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_counter = count_words(words)
        character_counter = count_characters(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_counter} words found in the document")

        for character, frequency in character_counter:
            print(f"The '{character}' character was found {frequency} times")



def count_words(words):
    return len(words)


def count_characters(text):
    lowered_text = text.lower()
    counter = {}
    for c in lowered_text:
        if c.isalpha() == True:
            if c not in counter:
                counter[c] = 1
            else:
                counter[c] += 1
    sorted_list = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    
    return sorted_list

#TODO:
# create a report




if __name__ == "__main__":
    main()
