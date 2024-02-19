#!/usr/bin/env python3
import argparse
import sys

from habrArticleDowld import HabrArticleDowld
from unittest import TestCase

base_url = "https://habr.com/ru/users/"
test_posts = ""


#OPTIMIZE: urls
DIR_ARCTICLE = 'article'
DIR_FAVORITES = 'favorites'
DIR_PICTURE = 'picture'
DIR_VIDEO = 'video'
DIR_SINGLES = 'singles'
HABR_TITLE = "https://habr.com"

class TestHabr(TestCase):
    def setArguments(self):
        # parser = argparse.ArgumentParser(description="Скрипт для скачивания статей с https://habr.com/")
        # parser.add_argument('-q', '--quiet', help="Quiet mode", action='store_true')
        # parser.add_argument('-l', '--local-pictures',
        #                     help="Использовать абсолютный путь к изображениям в сохранённых файлах",
        #                     action='store_true')
        # parser.add_argument('-i', '--meta-information', help="Добавить мета-информацию о статье в файл",
        #                     action='store_true')
        #
        # group = parser.add_mutually_exclusive_group(required=True)
        # group.add_argument('-u', help="Скачать статьи пользователя", type=str, dest='user_name_for_articles')
        # group.add_argument('-f', help="Скачать закладки пользователя", type=str, dest='user_name_for_favorites')
        # group.add_argument('-s', help="Скачать одиночную статью", type=str, dest='article_id')
        # group.add_argument('-c', help="Скачать несколько статей", type=str, dest='article_count')
        #
        # self.args = parser.parse_args()
        pass

    def setUp(self):
        self.setArguments()
        self.habrArticleDowld = HabrArticleDowld()





class TestInit(TestHabr):
    # def test_main(self):
    #     type_articles = None
    #     args = self.args
    #     if args.user_name_for_articles:
    #         output_name = args.user_name_for_articles + "/publications/articles/"
    #         output = habrArticleSrcDownloader.DIR_ARCTICLE
    #         type_articles = 'u'
    #     elif args.user_name_for_favorites:
    #         output_name = args.user_name_for_favorites + "/bookmarks/articles/"
    #         output = habrArticleSrcDownloader.DIR_FAVORITES
    #         type_articles = 'f'
    #     else:
    #         output_name = args.article_id
    #         type_articles = 's'
    #     try:
    #         if not args.article_id:
    #             self.habrSD.main("https://habr.com/ru/users/" + output_name, output, type_articles)
    #         else:
    #             self.habrSD.get_article("https://habr.com/ru/post/" + output_name, type_articles)
    #     except Exception as ex:
    #         print("[error]: Ошибка получения данных от :", output_name)
    #         print(ex)

    def test_get_articles(self):
        user_name = "Amaderu"
        test_url = base_url + user_name+"/bookmarks/articles/"

        self.habrArticleDowld.get_articles(test_url,"f",40)
        self.assertIsNotNone(self.habrArticleDowld.posts,f"Posts object is None or null or []")

    def test_main(self):
        test_url = base_url + "Amaderu/bookmarks/articles/"

        self.habrArticleDowld.main(test_url, DIR_FAVORITES,"f",40)
        self.assertIsNotNone(self.habrArticleDowld.posts,f"Posts object is None or null or []")




if __name__ == '__main__':

    pass
