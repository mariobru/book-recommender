def githubRequestAuthorized(isbn):

    # Importing Libraries
    import os
    from dotenv import load_dotenv
    import requests
    load_dotenv()

    # Function
    authToken = os.getenv("GOOGLE_BOOKS_API_TOKEN")
    if not authToken:
        raise ValueError("NECESITAS UN TOKEN")
    url = "https://www.googleapis.com/books/v1/volumes?q=isbn:{}&key={}".format(isbn,authToken)

    res = requests.get(url)
    data = res.json()
    return data