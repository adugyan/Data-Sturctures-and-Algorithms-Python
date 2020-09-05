#Returns the top 10 words that recur most often.
Nevermore ="Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore— While I nodded, nearly napping, suddenly there came a tapping, As of some one gently rapping, rapping at my chamber door. Tis some visitor, I muttered, tapping at my chamber door— Only this and nothing more."
words = Nevermore.split()
d = dict()

for word in words:
  d[word] = d.get(word, 0) + 1


lst = []
for (k, v) in d.items():
  lst.append((v,k))

srt = sorted(lst, reverse=True)
print(srt[:10])
