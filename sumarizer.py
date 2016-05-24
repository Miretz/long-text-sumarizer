
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import sys, argparse

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

if __name__ == "__main__":
    argp = argparse.ArgumentParser(description='Text summarizer application')
    argp.add_argument('-f','--file', help='Input file name',required=False)
    argp.add_argument('-u','--url',help='Input url address', required=False)
    args = argp.parse_args()
    if args.file:
        analyze_text_file(args.file)
    elif args.url:
        analyze_web_site(args.url)
    else:
        print("Usage: %s -f input_file -u input_url" % sys.argv[0])
