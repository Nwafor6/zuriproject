# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}



import string
count=dict()
def read_file_content(filename):
    with open(filename) as f:
        lines=f.readlines()
    for line in lines:
        #removing punctuations so words with punctuations are not not treated as another word as that without punctuation
        line=line.translate(line.maketrans('', '', string.punctuation))
        # lower all the words so it becomes case insensitive
        line1=line.lower()
        # make a list of all words
        words=line1.split()
        for word in words:
            if not word in count:
                count[word] =1
            else:
                count[word] +=1
    return "Hello World"


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    # return {"as": 10, "would": 20}
    return print(count)




count_words()



