from JEngines.JarticleEnhancer.ActivityLifeCycle import BaseActivity

class JarticleActivity(BaseActivity):

    def onPrepare(self):
        pass

    # -> Master Runner of Single Article
    # def process_article(self, article, isUpdate):
    #     updated_date = DICT.get("updatedDate", article, False)
    #     source = DICT.get("source", article, "False")
    #     if not isUpdate and updated_date or source == "twitter" or source == "reddit":
    #         return
    #     if isUpdate and updated_date == LAST_UPDATE:
    #         return
    #     # -> Setup
    #     self.overall_count += 1
    #     id = DICT.get("_id", article)
    #     date = DICT.get("published_date", article, "unknown")
    #     Log.i(f"Enhancing Article ID=[ {id} ], DATE=[ {date} ], COUNT=[ {self.overall_count} ]")
    #     title = DICT.get("title", article)
    #     body = DICT.get("body", article)
    #     description = DICT.get("description", article)
    #     # -> Combine All Main Content (Title, Body, Description)
    #     content = Language.combine_args_str(title, body, description)
    #     # -> Enhancers
    #     enhanced_article = enhance_article(article=article, content=content)
    #     # -> Update Article in MongoDB
    #     if not self.isTest:
    #         self.update_article_in_db(enhanced_article)

j = JarticleActivity()
