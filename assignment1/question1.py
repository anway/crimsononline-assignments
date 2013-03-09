
def common_words(filename):
    """question 1a

    Write a function that takes a path to a text file as input. The function
    should open the file, count the number of occurrences of each word, and
    return a sorted list of the most common words.
    """
    import string
    f = open(filename,'r')
    allwords = f.read().translate(None, string.punctuation).translate(None, '\n').lower().split(" ")
    d = dict()
    for word in allwords:
        if (word in d):
            d[word]=d[word]+1
        else:
            d[word]=1
    for word in sorted(d, key=d.get, reverse=True):
      print word
    f.close()

def common_words_min(filename, min_chars):
    """question 1b

    Modify this function to take a second argument that specifies the
    minimum number of characters long a word can be to be counted.
    """
    import string
    f = open(filename,'r')
    allwords = f.read().translate(None, string.punctuation).translate(None, '\n').lower().split(" ")
    d = dict()
    for word in allwords:
        if len(word) <= min_chars:
            if (word in d):
                d[word]=d[word]+1
            else:
                d[word]=1
    for word in sorted(d, key=d.get, reverse=True):
      print word
    f.close()

def common_words_tuple(filename, min_chars):
    """question 1c

    Modify this function to return a list of tuples rather than just a list
    of strings. Each tuple should be of the format
        (word, number of occurrences)    Of course, the list of tuples should still be sorted as in part a.
    """
    import string
    f = open(filename,'r')
    allwords = f.read().translate(None, string.punctuation).translate(None, '\n').lower().split(" ")
    d = dict()
    for word in allwords:
        if len(word) <= min_chars:
            if (word in d):
                d[word]=d[word]+1
            else:
                d[word]=1
    for word in sorted(d, key=d.get, reverse=True):
      print '({},{})'.format(word,d[word])
    f.close()

def common_words_safe(filename, min_chars):
    """question 1d

    Modify your function so that it catches the IOError exception and prints
    a friendly error message.
    """
    import string
    try:
        f = open(filename,'r')
        allwords = f.read().translate(None, string.punctuation).translate(None, '\n').lower().split(" ")
        d = dict()
        for word in allwords:
            if len(word) <= min_chars:
                if (word in d):
                    d[word]=d[word]+1
                else:
                    d[word]=1
        for word in sorted(d, key=d.get, reverse=True):
            print '({},{})'.format(word,d[word])
        f.close()
    except IOError:
        print "trouble opening file"
