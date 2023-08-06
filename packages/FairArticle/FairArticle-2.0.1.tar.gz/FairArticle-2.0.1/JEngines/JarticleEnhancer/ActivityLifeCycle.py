from FSON import DICT
from FList import LIST
import os
from Jarticle.jProvider import jPro


class BaseActivity(jPro):
    pid = None
    isTest = False
    articles = []

    def __init__(self, **kwargs):
        super().__init__()
        self.handle_kwargs(**kwargs)
        self.onCreate()
        self.onStart("this is a test")

    def handle_kwargs(self, **kwargs):
        self.isTest = DICT.get("isTest", kwargs, default=False)
        self.articles = DICT.get("articles", kwargs, default=[])

    def onCreate(self):
        Alert.send_alert(f"{message}")
        self.pid = os.getpid()

    def onStop(self, message):
        Alert.send_alert(f"{message}")

    def get_func(self, func):
        return getattr(self, func)

    def get_callable(self, attr):
        return callable(attr)

    def safe_get_att(self, attr):
        try:
            item = getattr(self, attr)
            return item
        except Exception as e:
            Log.e("Failed to get attribute/function.", error=e)
            return False

    @staticmethod
    def get_arg(key, value, default=False):
        return DICT.get(key, value, default=default)

    def addArticles(self, articles):
        self.articles = LIST.flatten(articles)

    def update_article_in_db(self, updated_article):
        if not self.isTest:
            self.update_article(updated_article)