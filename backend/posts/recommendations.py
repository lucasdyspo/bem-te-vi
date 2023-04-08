from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import download
import sys
import os
from django.db.models import Q

# Adiciona o caminho ao diretório libs
# libs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'libs'))
# sys.path.append(libs_path)
from models import Post
from users.models import User



# from ...users.models import User
# from ...posts.models import Post
# from ....backend.posts.models import Post


# import requests
# import numpy as np
# import tensorrec






# def get_location_by_ip(ip_address):
#     response = requests.get(f"https://api.ipdata.co/{ip_address}?api-key=API_KEY")
#     if response.status_code == 200:
#         data = response.json()
#         city = data.get('city')
#         state = data.get('region')
#         country = data.get('country_name')
#         return f"{city}, {state}, {country}"
#     return None




class recom:
    def __init__(self, term, lang=None):

        download('stopwords')


        pula = '\n\n\n\n\n\n\n\n\n'
        if lang == None:
            self.lang = 'portuguese'
        else:
            self.lang = lang

        stop_words = set(stopwords.words(self.lang))
        print(self.lang, pula, stop_words)


        self.stemmer = SnowballStemmer(self.lang)

        print(self.stemmer, pula)

        tokens = []

        for li in (term.split()):
            tokens.append(li)


        print(self.stemmer, pula, tokens)

        self.stop_words = stop_words

        self.tokens = [token for token in tokens if not token in self.stop_words]
        self.stemmed_tokens = [self.stemmer.stem(token) for token in tokens]

        print(self.stemmed_tokens)



# po = recom('sala pro quarto filhao')




class pull:
    def __init__(self, user):
        self.user = user




class Posts_man:

    search_limit = 3
    random_limit = 10

    def search_by_query(self, query):
        # title_posts = Post.objects.filter(title__icontains=query)

        # desc_posts = Post.objects.filter(description__icontains=query)


        # # [:self.search_limit]
        # posts = title_posts.union(desc_posts)
        myposts = Post.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return myposts

    def get_latest_posts(self):
        posts = Post.objects.order_by('-created_at')[:10]
        return posts

    @classmethod
    def set_search_limit(cls, limit):
        """Método de classe para alterar o limite de resultados da busca."""
        cls.search_limit = limit
