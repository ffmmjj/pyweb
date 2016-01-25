from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cluster import KMeans
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.snowball import *
from sklearn.decomposition import NMF
from collections import defaultdict

class NLPService():
    def __init__(self):
        self.stopwords_extended = ['nao', 'ja', 'pois', 'pra', 'sobre', 'deste', 'ta', 'bom', 'obrigado', 'obrigada']
        self.stopwords_extended.extend(['gostaria', 'saber', 'fazer', 'boa', 'ate'])
        self.stopwords_extended.extend(stopwords.words('portuguese'))

    def getTokens(self, text):
        lowers = text.lower()
        no_punctuation = lowers.translate(None, string.punctuation)
        tokens = nltk.word_tokenize(no_punctuation)
        return tokens

    def stemTokens(self, tokens, stemmer):
        stemmed = []
        for item in tokens:
            stemmed.append(stemmer.stem(item))
        return stemmed

    def prepareMessage(self, text):
        tokens = self.getTokens(text)
        filtered = [w for w in tokens if not w in self.stopwords_extended]
        stemmer = SnowballStemmer('portuguese')
        stemmed = self.stemTokens(filtered, stemmer)
        return ' '.join(stemmed)

    def vectorize(self, messages):
        vectorizer = TfidfVectorizer(max_df=0.5, max_features=10000,
                                 min_df=2, stop_words=self.stopwords_extended,
                                 use_idf=True)
        return vectorizer.fit_transform(messages)

    def clusterizeKMeans(self, vector, numberOfClusters):
        km = KMeans(n_clusters=numberOfClusters, init='k-means++', max_iter=100, n_init=1,verbose=False)
        return km.fit(vector)

    def clusterizeNNMF(self, vector, numberOfClusters):
        nmf = NMF(n_components=numberOfClusters, random_state=1).fit(vector)
        return nmf

    def processMessages(self, messages, algorithm="K-Means"):
        clusters = []
        nonEmptyMessages = [m for m in messages if m.content.strip() != ""]
        preparedMessages = [self.prepareMessage(m.content) for m in nonEmptyMessages if m.content.strip() != ""]
        vector = self.vectorize(preparedMessages)
        
        prediction = None
        if algorithm == "K-Means":
            model = self.clusterizeKMeans(vector, 5)
            prediction = zip(nonEmptyMessages, model.predict(vector))
        else:
            model = self.clusterizeNNMF(vector, 5)        
            prediction = zip(nonEmptyMessages, model.transform(vector))

        clusters = defaultdict(list)
        [clusters[c].append(m) for m,c in prediction]

        return clusters