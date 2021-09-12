from os import path
from main import  export_ebook_wordlist
from oulu import  export_csv
from nltk.stem import WordNetLemmatizer
import time

lemmatizer = WordNetLemmatizer()

def test_excel():
    t1 = time.time()
    my_word_count = 3000
    book_name = "pg1342"
    book_path = 'resource/{}.epub'.format(book_name)
    export_path = path.join(path.expanduser("~"), 'Desktop/{}.xlsx'.format(book_name))
    print(book_path)
    export_ebook_wordlist(book_path, export_path, my_word_count)
    result = time.time() - t1
    print(result)  # 0.000000xxxx

def test_csv():
    t1 = time.time()
    my_word_count = 3000
    book_name = "pg1342"
    book_path = 'resource/{}.epub'.format(book_name)
    export_path = path.join(path.expanduser("~"), 'Desktop/{}.txt'.format(book_name))
    print(book_path)
    export_csv(book_path, export_path, my_word_count)
    result = time.time() - t1
    print(result)  # 0.000000xxxx
    print("test b")

def test_lemmatization():
    test_array = ["rocks","birds","tired","gone","corpora"]
    processed_array = [lemmatizer.lemmatize(word) for word in test_array]
    print(processed_array)

if __name__ == "__main__":
    test_csv()
