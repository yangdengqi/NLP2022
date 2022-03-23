from nltk.corpus.reader import PlaintextCorpusReader
from nltk.probability import FreqDist

import urllib
file = urllib.request.urlopen(url="https://raw.githubusercontent.com/stopwords-iso/stopwords-zh/master/stopwords-zh.txt")
stopwords = file.read().decode("utf8").split()
#print(stopword)

from string import printable
n=300

Boy_Girl_dir = "Boy_Girl/"
pcr = PlaintextCorpusReader(root=Boy_Girl_dir, fileids=".*\.txt")
fd = FreqDist(samples=pcr.words())
Boy_Girl_words = [word for word,freq in fd.most_common(n=n) if word not in stopwords and word[0] not in printable]

Cat_dir = "Cat/"
pcr = PlaintextCorpusReader(root=Cat_dir, fileids=".*\.txt")
fd = FreqDist(samples=pcr.words())
Cat_words = [word for word,freq in fd.most_common(n=n) if word not in stopwords and word[0] not in printable]

print(Boy_Girl_dir)
print([word for word in Boy_Girl_words if word not in Cat_words])

print(Cat_dir)
print([word for word in Cat_words if word not in Boy_Girl_words])


# 1. What are the most common words in your two PTT boards respectively? 
#    Do they correspond to what you have expected?
#    (Please upload your Python script to GitHub, and paste your GitHub link on the online text of eCourse homework.)


from gensim.models import Word2Vec
from gensim.models.word2vec import PathLineSentences
corpus = PathLineSentences(Cat_dir)#"Cat")

#model = Word2Vec(sentences=corpus, vector_size=100, window=5, min_count=1, workers=4)
#print(model.wv.most_similar(positive=['女生',"老婆"], negative=['男生']))

# 2. By using the GenSim Word2Vec module, 
#    find a word x in an analogy like "man : king :: woman : x" (read: man is to king as woman is to x) 
#    in your PTT texts.
#    (Please upload your Python script to GitHub, and paste your GitHub link on the online text of eCourse homework.)
