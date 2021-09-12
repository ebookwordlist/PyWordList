import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk import FreqDist
from nltk.corpus import brown
from functools import reduce
import string
from os import path
from nltk.stem import WordNetLemmatizer

# nltk.set_proxy('http://127.0.0.1:1087')
# nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

frequency_list = FreqDist(i.lower() for i in brown.words())

def split(word):
    return [char for char in word]

def remove_duplicate_keep_order(a):
    return list(dict.fromkeys(a))

def process_chapter(sentences,my_words_dict):
    wordlist = reduce(lambda x, y: x + y, [nltk.word_tokenize(s) for s in sentences])
    stop_words = set(stopwords.words("english") + split(string.punctuation) + ["“", "”"])
    filtered_list = [word for word in wordlist if word.casefold() not in stop_words]
    filtered_list = [lemmatizer.lemmatize(word) for word in filtered_list]
    filtered_list = remove_duplicate_keep_order(filtered_list)
    filtered_list = [word for word in filtered_list if word.casefold() not in my_words_dict]
    filtered_list = [word for word in filtered_list if word.casefold() in frequency_list]
    return filtered_list


def export_csv(book_path,export_path,my_word_count):
    book = epub.read_epub(book_path)
    chapters = [doc.get_body_content() for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT)]
    soups = [BeautifulSoup(chapter, 'html.parser') for chapter in chapters]
    my_words_dict = dict(frequency_list.most_common()[:my_word_count])

    # soups = soups[0:2]

    f = open(export_path, "a")
    for index, soup in enumerate(soups):
        sentences = [x.getText() for x in soup.findAll('p')]
        if len(sentences) == 0:
            continue
        word_list = process_chapter(sentences,my_words_dict)
        print(word_list)
        chapter_name  = "#p&p{}".format(index)
        f.write(chapter_name)
        f.write("\n")
        for w in word_list:
            print(w)
            f.write(w)
            f.write("\n")
        f.write("\n")


    f.close()

def get_default_export_path():
    export_path = path.join(path.expanduser("~"), 'Desktop/english_world_list.xlsx')
    return export_path

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        "import epub book and export xlsx file which contains the word list of book"
                                    )
    parser.add_argument("--importPath", help="the path of epub book", type=str)
    parser.add_argument("--exportPath", help="the path of export xlsx", type=str,default=get_default_export_path())
    parser.add_argument("--level", help="your english world level/count default is 3000", type=int,default=3000)
    args = parser.parse_args()
    print(args.importPath)
    print(args.exportPath)
    print(args.level)
    export_csv(book_path=args.importPath,export_path=args.exportPath,my_word_count=args.level)

