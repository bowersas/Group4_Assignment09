'''
Created on Apr 2, 2024

@author: Carto
'''
import requests

class DataFetcher:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_data(self, endpoint):
        """Fetch data from a given endpoint."""
        full_url = f"{self.base_url}/{endpoint}"
        response = requests.get(full_url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def process_data(self, endpoint):
        """Process and print data from the server in a friendly format."""
        try:
            coffees = self.fetch_data(endpoint)
            for coffee in coffees:
                print(f"Name: {coffee.get('title', 'No Name')}\nDescription: {coffee.get('description', 'No Description')}\n---")
        except Exception as e:
            print(f"An error occurred: {e}")

