def filter_a(ls):
    new_ls = []
    for word in ls:
        if word.find("a") != -1:
            new_ls.append(word)
    return new_ls

def main():
    ls = ["apple", "car", "shoe", "desk", "happy"]
    new_ls = filter_a(ls)
    print(new_ls)

main()