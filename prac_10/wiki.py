import wikipedia

def main():
    query = input("Enter page title: ")

    while query != "":
        try:
            page = wikipedia.page(query, auto_suggest=False)

            print(page.title)
            print(page.summary)
            print(page.url)

        except wikipedia.exceptions.PageError:
            print(f'Page id "{query}" does not match any pages. Try another id!')

        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)

        query = input("Enter page title: ")

    print("Thank you.")

if __name__ == "__main__":
    main()