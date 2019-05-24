from django.shortcuts import render
from .forms import summary_form
#load Dependancies
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.summarizers.lex_rank import LexRankSummarizer as Summarizer
import sys, os
from newspaper import Article
import nltk
nltk.download('punkt')








# Create your views here.
def summary(request): 
    keyW = None
    results = None
    form = summary_form(request.POST or None)
    if form.is_valid():        
        SUMMARIZE = form.cleaned_data['SUMMARIZE']
        LANGUAGE = form.cleaned_data['LANGUAGE']
        SENTENCES_COUNT = form.cleaned_data['SENTENCES_COUNT'] 
        url = SUMMARIZE
        LANGUAGE = LANGUAGE
        SENTENCES_COUNT = SENTENCES_COUNT
   
        try:
            article = Article(url)           
            article.download()
            article.parse() 
            article.nlp()
            keyW = article.keywords         
            parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
            # or for plain text files
            # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
            stemmer = Stemmer(LANGUAGE)

            summarizer = Summarizer(stemmer)
            summarizer.stop_words = get_stop_words(LANGUAGE)            
            for sentence in summarizer(parser.document, SENTENCES_COUNT):
                print(sentence)

            results = summarizer(parser.document, SENTENCES_COUNT)
             

        except:          
            keyW = 'Invalid Entry'
            results = '-'   
            pass 
            

    context = {'form':form, 'keywords':keyW, 'results':results}
    template = 'index.html'
    return render(request, template, context)
    
    
    
    