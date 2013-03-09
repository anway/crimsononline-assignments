
def parse_links_regex(filename):
    """question 2a

    Using the re module, write a function that takes a path to an HTML file
    (assuming the HTML is well-formed) as input and returns a dictionary
    whose keys are the text of the links in the file and whose values are
    the URLs to which those links correspond. Be careful about how you handle
    the case in which the same text is used to link to different urls.
    
    For example:

        You can get file 1 <a href="1.file">here</a>.
        You can get file 2 <a href="2.file">here</a>.

    What does it make the most sense to do here? 
    """
    import re
    f = open(filename,'r')
    all = f.read()
    target = re.findall('<a href="(.*?)">(.*?)</a>', all)
    d = dict()
    for link in target:
        if link[1] in target:
            d[link[1]].append(link[0])
        else:
            d[link[1]] = link[0]
    pairs = zip(d.keys(), d.values())
    for pair in pairs:
        print'{}: {}'.format(pair[0],pair[1])

def parse_links_xpath(filename):
    """question 2b

    Do the same using xpath and the lxml library from http://lxml.de rather
    than regular expressions.
    
    Which approach is better? (Hint: http://goo.gl/mzl9t)
    """
    import lxml.html
    f = open(filename,'r')
    all = f.read()
    tree = lxml.html.fromstring(all)
    text = tree.xpath('//a//text()')
    link = tree.xpath('//a//@href')
    d=dict()
    for i in range (1,min(len(text), len(link))):
        if text[i] in d:
            d[text[i]].append(link[i])
        else:
            d[text[i]]=[link[i]]
    print d
