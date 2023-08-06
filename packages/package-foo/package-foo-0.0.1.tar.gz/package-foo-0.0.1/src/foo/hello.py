# coding = utf8

"""
Hello is module including only one function hello

hello is a demo method to print a message Hello <msg>
msg is parameter received user input string
"""

def hello(msg='World'):
    """
    show a welcome words

    Args:
        msg(str): object to welcome

    Return:
        None

    Output:
        Hello, msg!

    >>> hello()
    Hello, World!
    """
    print("Hello, " + msg + "!")


if __name__ == '__main__':
    hello()
