import codecs
import glob
import nltk


def analyze(path):
    txt = codecs.open(path, "r", "utf8").read()
    tokens = nltk.word_tokenize(txt)
    tagged = nltk.pos_tag(tokens)
    normalized = []
    skipped = 0
    for ((word1, tag1), (word2, tag2)) in nltk.bigrams(tagged):
        word1 = word1.encode('utf8')
        word2 = word2.encode('utf8')
        if tag1.startswith("J") and tag2.startswith("NN"):
            skipped += 1
            print 15, word1, word2
            continue
        normalized.append(word1)
    print 17, skipped
    return " ".join(normalized)


def files():
    return glob.glob("corpus/*")

print "================================="
for media in files():
    if "fox" in media:
        print analyze(media).encode("utf8")
print "DONE"
