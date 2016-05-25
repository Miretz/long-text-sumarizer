# long-text-sumarizer
Machine learning tool to summarize long text.
Based on the sumy library.

#Install requirements via pip

```
pip install -r requirements.txt
```

Download NLTK tokenizers by following command:

```
python -c "import nltk; nltk.download('punkt')"
```

#Run


To summarize a text file
```
python sumarizer.py -f testdata.txt
```


To summarize a website
```
python sumarizer.py -u https://en.wikipedia.org/wiki/World_War_II
```
