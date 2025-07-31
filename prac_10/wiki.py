import wikipedia

def main():
    query = input("Enter page title: ")

    while query != "":
        page = wikipedia.page(query)

        print(f"Title: {page.title}")
        query = input("Enter page title: ")

if __name__ == "__main__":
    main()