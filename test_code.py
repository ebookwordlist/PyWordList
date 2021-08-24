from os import path
from main import  export_ebook_wordlist

import time

t1 = time.time()
my_word_count = 3000
book_name = "pg1342"
book_path = 'resource/{}.epub'.format(book_name)
export_path = path.join(path.expanduser("~"), 'Desktop/{}.xlsx'.format(book_name))
print(book_path)
export_ebook_wordlist(book_path,export_path,my_word_count)
result = time.time() - t1
print(result) # 0.000000xxxx