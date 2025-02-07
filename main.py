if __name__ == "__main__":
    book_path = "books/frankenstein.txt"
    def main():
        with open(book_path) as f:
            file_contents = f.read()
            book_as_string = str(file_contents)
            word_count = len(book_as_string.split())
            print(f"{word_count} words found in the document")
    
    def character_count():
        with open(book_path) as f:
            file_contents = f.read()
            lowercased_book = str(file_contents).lower()
            character_dict = {}
            
            for character in lowercased_book:
                if character not in character_dict and character.isalpha():
                    character_dict[character] = 0
                if character.isalpha():
                    character_dict[character] += 1

            sorted_dict = {k:v for k,v in sorted(character_dict.items(), reverse=True, key=lambda item: item[1])}
            for key,value in sorted_dict.items():
                print(f"The '{key}' character was found {value} times")
    


    print(f"--- Begin report of {book_path} ---")
    main()
    print()
    character_count()
    print("--- End Report ---")