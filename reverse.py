from cs50 import get_string

def r1(word):
    print(word[::-1])

def r2(word):
    rev = ""
    for letter in word:
        rev = letter + rev
    print(rev)

def r3(word):
    for i in range(len(word) - 1, -1, -1):
        print(word[i], end="")
    print()

def r4(word):
    for i in range(len(word)):
        print(word[len(word) - 1 - i], end="")
    print()

def r5(word):
    letters = [word[len(word) - 1 - i] for i in range(len(word))]
    print("".join(letters))

def main():
    word = get_string("Text: ")
    r1(word)
    r2(word)
    r3(word)
    r4(word)
    r5(word)

main()