def get_content(path="") :
    with open(path,'r') as file :
      return file.read();

def count_char(text="") :
    char_map = {}
    for char in text :
        char = char.lower();
        if char in char_map :
            char_map[char] += 1;
        else :
            char_map[char] = 1;
    return char_map

def count_words(content="") :
    words = content.split();
    return len(words);

def main(path= "") :
    content = get_content(path);
    print(f"---- Begin report of the book {path.split('/')[-1]} ----\n")  
    print(f"{count_words(content)} words found in the document");
    sorted_list = sorted(list(count_char(content).items()), key=lambda a : a[1],reverse=True)
    for k,v  in  sorted_list:
        if k.isalpha() :
            print(f"The '{k}' character was found times {v}");
    print("---- End of Report ----")

main("books/frankenstein.txt")

