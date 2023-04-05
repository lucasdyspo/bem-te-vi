from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import download
from users.models import User
from posts.models import Post
import requests

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
    limit = 3
    def posts_search(self, word):
        posts = Post.objects.filter(title__icontains=word)




    def lasts(self):
        ...

    @classmethod
    def change_limit(cls):
        ...
