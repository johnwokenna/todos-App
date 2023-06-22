import webbrowser

""" important module for search in browser"""

user_term = input("Enter a search term: ")

webbrowser.open("https://www.google.com/search?q=" + user_term)
