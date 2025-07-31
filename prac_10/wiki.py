import wikipedia

def main():
    print("Wikipedia Search")
    query = input("Enter a page title or phrase (blank to quit): ")
    while query != "":
        page = wikipedia.page(query)
        print(f"Title: {page.title}")
        print(f"URL: {page.url}")
        print(f"Summary: {wikipedia.summary(query, sentences=3)}")

        query = input("Enter a page title or phrase (blank to quit): ")


if __name__ == '__main__':
    main()