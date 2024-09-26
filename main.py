from collections import Counter

def get_content(path="") :
    try :
        with open(path,'r') as file :
            return file.read();
    except (FileNotFoundError, OSError):
        raise Exception("Either Permission not granted, or file not found!"); 

def count_char(text="") :
    return Counter(x.lower() for x in text if x.isalpha());

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

if __name__ == "__main__" :
    main("books/frankenstein.txt")

