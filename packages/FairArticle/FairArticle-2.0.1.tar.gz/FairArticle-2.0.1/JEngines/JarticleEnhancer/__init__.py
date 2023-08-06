from jarEngine.Enhancements import SozinEngine as sp
from JEngines import CategoryEngine
from jarEngine.Content.NLP import NLTK
from fairNLP import Language
from FList import LIST
from FSON import DICT
from FDate import DATE
import Alert
from Jarticle.jProvider import jPro

from Jarticle.jdexes.jCompany import jCompany
from FLog.LOGGER import Log
Log = Log("Jarticle.Engine.Processor.ArticleProcessor_v2")

WORDS = "words"
BODY = "body"
TITLE = "title"
DESCRIPTION = "description"

"""
-> Maintains the lifecycle of processing a list of hookups
"""

LAST_UPDATE = "May 19 2022"

JP = jPro()

def categorizer(article):
    return CategoryEngine.process_single_article(article, isUpdate=True)

def sozin(content):
    tickers = sp.extract_all(content)
    stock_tickers = LIST.get(0, tickers)
    crypto_tickers = LIST.get(1, tickers)
    Log.d("Tickers: " + str(tickers))
    if stock_tickers and crypto_tickers:
        return tickers
    elif stock_tickers:
        return stock_tickers
    elif crypto_tickers:
        return crypto_tickers
    return False

def get_company_reference(article):
    tickers = DICT.get("tickers", article)
    if not tickers:
        return False
    jc = jCompany.constructor_jcompany()
    references = {}
    for key in tickers:
        id = jc.get_company_id_for_ticker(key)
        if id and key not in references.keys():
            references[key] = id
    return references

def get_summary(article):
    body = DICT.get("body", article, default="False")
    summary = NLTK.summarize_v2(body, 4)
    # summary = Language.text_summarizer(body, 4)
    return summary

def get_keywords(article):
    title = DICT.get("title", article, default="False")
    body = DICT.get("body", article, default="False")
    keywords = NLTK.keywords(str(body) + str(title))
    newList = []
    for item in keywords:
        newList.append(item)
    return newList

def get_sentiment(content):
    sentiment = NLTK.get_content_sentiment(content)
    return sentiment

def get_source_page_rank(article):
    from jarEngine.Helper import PageRank
    url = DICT.get("url", article, "unknown")
    rank = PageRank.get_page_rank(url)
    return rank

# -> [MASTER]
def enhance_article(article, content):
    article = categorizer(article)
    article["keywords"] = get_keywords(article)
    article["summary"] = get_summary(article)
    article["tickers"] = sozin(content)
    article["company_ids"] = get_company_reference(article)
    article["sentiment"] = get_sentiment(content)
    article["source_rank"] = get_source_page_rank(article)
    article["updatedDate"] = DATE.mongo_date_today_str()
    return article

def update_enhanced_summary(article):
    article["summary"] = get_summary(article)
    return article
