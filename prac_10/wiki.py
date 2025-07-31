import wikipedia

def main():
    print("Wikipedia Search")
    query = input("Enter a page title or phrase (blank to quit): ")
    while query != "":
        try:
            page = wikipedia.page(query, auto_suggest=False)
            print(f"Title: {page.title}")
            print(f"URL: {page.url}")
            print(f"Summary: {wikipedia.summary(query, sentences=3)}")
        except wikipedia.exceptions.DisambiguationError as e:
            print("Disambiguation Error. Possible options:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print("Page not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

        query = input("Enter a page title or phrase (blank to quit): ")


if __name__ == '__main__':
    main()