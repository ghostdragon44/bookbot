def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print(file_contents)

if __name__ == "__main__":
    main()

def count_words(text):
    words = text.split()
    return len(words)

with open('books/frankenstein.txt', 'r', encoding='utf-8') as file:
    book_text = file.read()

print(count_words(book_text))

def count_Characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

result = count_Characters(book_text)

print(result)

char_counts = {'p': 6121, 'r': 20818, 'o': 25225,
               'j': 504, 'e': 46043, 'c': 9243, 
               't': 30365, 'g': 5974, 'u': 10407, 
               'n': 24367, 'b': 5026, 's': 21155, 
               'f': 8731, 'a': 26743, 'k': 1755, 
               'i': 24613, 'y': 7914, 'm': 10604, 
               'w': 7638, 'l': 12739, 'd': 16863, 
               'h': 19725, 'v': 3833, 'z': 243, 
               'x': 677, 'q': 324}

char_list = []
for char, count in char_counts.items():
    char_list.append({"char": char, "num": count})

def sort_on(dict):
    return dict["num"]

char_list.sort(reverse=True, key=sort_on)

print(char_list)

total_words = 77986

print("--- Begin report of books/frankenstein.txt ---")
print(f"{total_words} words found in the document")

for entry in char_list:
    char = entry['char']
    num = entry['num']
    print(f"The '{char}' character was found {num} times")

print("--- End Report ---")