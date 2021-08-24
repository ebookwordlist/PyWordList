`PywordList` can help you export english word list from a `epub` book.
you can check [exported xlsx](https://github.com/ebookwordlist/PyWordList/blob/master/resource/pg1342.xlsx) to get the point

### Download script 
```
git clone https://github.com/ebookwordlist/PyWordList.git 
cd PyWordList
python3 -m venv venv/ 
source venv/bin/activate 

### if you are in chinese mainland:
pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com

### else:
pip install -r requirements.txt

```


### Use commandline 
```
python3 main --importPath="your_epub_book_path.epub" --exportPath="your_excel_path.xlsx" --level=3000
```
your can use 

```
python3 main -h
```
to check the arguments detail

### Use GUI:
```
python3 gui.py
```
![](img/app_ui.png)

### Build MacOS app 
Via [py2app](https://py2app.readthedocs.io/en/latest/) we can build a `PyWorldList` app on MacOS systerm 

```
python setup.py py2app
```
later you will see a `gui.app` in `dist/` folder