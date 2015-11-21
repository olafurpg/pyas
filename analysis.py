import codecs
import collections
import glob
import nltk


def analyze(path):
    txt = codecs.open(path, "r", "utf-8").read()
    tokens = nltk.word_tokenize(txt)
    tagged = nltk.pos_tag(tokens)
    counts = collections.defaultdict(int)
    counts["tokens"] = len(tokens)
    for word, tag in tagged:
        # print word, tag
        # counts[tag] += 1
        if tag.startswith("R"):
            counts["adverbs"] += 1
            # print 16, word
        if tag.startswith("J"):
            counts["adjectives"] += 1
        if tag.startswith("NNP"):
            counts["nouns"] += 1
        if tag.startswith("VB"):
            counts["verbs"] += 1
    counts["adj2nouns"] = counts["adjectives"] / float(counts["nouns"])
    counts["adv2verbs"] = counts["adverbs"] / float(counts["verbs"])
    return dict(counts)


def files():
    return glob.glob("corpus/*")

print "================================="
for media in files():
    print media, analyze(media)
print "DONE"
