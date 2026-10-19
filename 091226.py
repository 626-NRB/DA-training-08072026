from gensim.models import Word2Vec

model = Word2Vec.load("models/092026-nawaf_w2v.model")

# Get vector for a material
#vector = model.wv["measure"]

# Find similar materials
similar = model.wv.most_similar("resistance", topn=15)
print(similar)