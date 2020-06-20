import wordcloud
import numpy as np
from matplotlib import pyplot as plt
import re

# method for wordcloud egneration

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just","in",\
    "not","for","said","on","thou","one","into","up","then","ye","would","so","must","thee","there","out","back","could",\
                          "again"]
    
    # LEARNER CODE START HERE
    w = {}
    file_contents = re.sub(r'[^\w\s]','',file_contents).lower()
    list_of_words = file_contents.split()
    for word in list_of_words:
        if word not in uninteresting_words:
            if word not in w:
                w[word] = 1
            else:
                w[word] += 1
        else:
            continue
        
      
    #wordcloud
    x, y = np.ogrid[:300, :300]
    mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
    mask = 255 * mask.astype(int)
    cloud = wordcloud.WordCloud(max_words=10000, background_color="white",mask=mask)
    cloud.generate_from_frequencies(w)
    return cloud.to_array()


def image_wordcloud(file_contents, target):
    myimage = calculate_frequencies(file_contents)
    plt.imshow(myimage, interpolation = 'nearest')
    plt.axis('off')
    plt.savefig(target,dpi=300)
    return "hello"

