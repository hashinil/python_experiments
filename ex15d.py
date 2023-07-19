import webbrowser

search = input("Enter search term: ")
search = search.replace(" ", "+")
webbrowser.open("https://google.com/search?q="+search)