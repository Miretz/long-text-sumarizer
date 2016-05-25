
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import sys, argparse
from PyPDF2 import PdfFileReader

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

LANGUAGE = "english"
SENTENCES_COUNT = 3

def analyze(parser):
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)  

def analyze_text_file(file):
    print("Main Points: %s \n" % file)
    parser = PlaintextParser.from_file(file, Tokenizer(LANGUAGE))
    analyze(parser)

def analyze_web_site(url):
    print("Main Points: %s \n" % url)
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    analyze(parser)    

def analyze_pdf_file(file):
    tempfile="temp.txt"
    print("Extracting PDF text to file %s" % tempfile)
    pdf_file = PdfFileReader(open(file, "rb"))
    data = ""
    for i in range(0, pdf_file.getNumPages()):
        data += pdf_file.getPage(i).extractText() + u"\n"
    data = u" ".join(data.replace(u"\xa0", " ").strip().split())
    f = open(tempfile,'w')
    f.write(data.encode("ascii", "ignore"))
    f.close()
    analyze_text_file(tempfile)
    
if __name__ == "__main__":
    argp = argparse.ArgumentParser(description='Text summarizer application')
    argp.add_argument('-f','--file', help='Input TXT file',required=False)
    argp.add_argument('-u','--url',help='Input url address', required=False)
    argp.add_argument('-p','--pdf',help='Input PDF file', required=False)
    args = argp.parse_args()
    if args.file:
        analyze_text_file(args.file)
    elif args.url:
        analyze_web_site(args.url)
    elif args.pdf:
        analyze_pdf_file(args.pdf)
    else:
        print("Usage: %s -f input_file -u input_url" % sys.argv[0])
