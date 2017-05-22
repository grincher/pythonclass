store = []


def function(myStrings):
    """
    define a function that takes a string parameter
    defines a local function that returns the last letter of the string
    return a sorted list based on the last letter
    :param myStrings: list of strings
    :return: sorted list of strings
    """
    def last_letter(s):
        """
        Local helper function
        :param s: a string
        :return: last letter of string s
        """
        return(s[-1])
    store.append(last_letter)
    print(last_letter)
    for item in store:
        print(item)
    return(sorted(myStrings, key=last_letter))


def logger(msg):
    def log_message():
        print("Log:", msg)
    return(log_message)


def html_tag(tag):
    """
    Creates an html tag based on input
    :param tag: Tag
    :return: a callable function
    """
    def wrap_text(msg):
        print("<{0}>{1}</{0}>".format(tag, msg))
    return wrap_text

"""
Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
>>> from sort_by_last_letter import html_tag
>>> tagname = html_tag("tagname")
>>> tagname("value")
<tagname>value</tagname>
"""

def main():
    print(function(["z", "one","two","four", "three", "zebra"]))


if __name__ == '__main__':
    main()
    exit(0)
