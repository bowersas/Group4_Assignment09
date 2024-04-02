'''
Created on Apr 2, 2024

@author: Carto
'''
from data_fetcher import DataFetcher

def main():
    # Instantiate the DataFetcher class with the base URL of JSONPlaceholder
    fetcher = DataFetcher("https://jsonplaceholder.typicode.com")

    # Fetch and process posts data
    print("Fetching and displaying posts data...\n")
    fetcher.process_data("posts")

if __name__ == "__main__":
    main()
