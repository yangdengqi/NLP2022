from nltk.corpus.reader import PlaintextCorpusReader
source_dir = "Boy_Girl/"
#source_dir = "Cat/"

pcr = PlaintextCorpusReader(root=source_dir, fileids=".*\.txt")
from nltk.probability import FreqDist
fd = FreqDist(samples=pcr.words())
print(fd.most_common(n=100))

# 1. What are the most common words in your two PTT boards respectively? 
#    Do they correspond to what you have expected?
#    (Please upload your Python script to GitHub, and paste your GitHub link on the online text of eCourse homework.)


from gensim.models import Word2Vec
from gensim.models.word2vec import PathLineSentences
corpus = PathLineSentences(source_dir)#"Boy_Girl")

model = Word2Vec(sentences=corpus, vector_size=100, window=5, min_count=1, workers=4)
print(model.wv.most_similar(positive=['女生',"老婆"], negative=['男生']))

#model = Word2Vec(sentences=corpus, vector_size=100, window=5, min_count=1, workers=4)
#print(model.wv.most_similar(positive=['貓',"貓咪"], negative=['狗']))

# 2. By using the GenSim Word2Vec module, 
#    find a word x in an analogy like "man : king :: woman : x" (read: man is to king as woman is to x) 
#    in your PTT texts.
#    (Please upload your Python script to GitHub, and paste your GitHub link on the online text of eCourse homework.)
