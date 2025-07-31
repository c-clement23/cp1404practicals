import wikipedia

def main():
    query = input("Enter page title: ")

    while query != "":
        page = wikipedia.page(query)

        print(f"Title: {page.title}")
        print(f"Summary: \n{wikipedia.summary(query,sentences=3)}")
        query = input("Enter page title: ")

if __name__ == "__main__":
    main()