import requests
import pandas as pd
import configparser
import os

config = configparser.ConfigParser()
config_file = 'config.ini'

if os.path.exists(config_file):
    config.read(config_file)
else:
    raise FileNotFoundError(f"{config_file} not found.")


class WorldBankAPI:
    """
    A class to fetch and process data from the World Bank API.
    """
    def __init__(self, url):
        self.url = url
        self.data = None 

    def get_countries(self, file_path):
        """
        Processes the retrieved data to extract the list of countries.
        Saves the resulting DataFrame to a CSV file.
        """
        country_url = config.get('countries_api', 'url')
        response = requests.get(country_url)
        response.raise_for_status() # raise an error if there's an issue with the API call
        data = response.json()
        countries = []
        for item in data[1]:
            country = {
                "country": item["name"],
                "country_code": item["id"],
                "capital": item["capitalCity"],
                "region": item["region"]["value"]
            }
            countries.append(country)
        country_df = pd.DataFrame(countries, columns=['country',
                                                       'country_code','capital','region'])
        country_df.to_csv(file_path, index=False)
        return country_df

    def get_gdp(self, file_path):
        """
        Processes the retrieved data to extract the economic data for the given indicator.
        Saves the resulting DataFrame to a CSV file.
        """
        gdp_url = config.get('gdp_api', 'url')
        response = requests.get(gdp_url)
        response.raise_for_status() # raise an error if there's an issue with the API call
        data = response.json()
        gdp_data = []
        for item in data[1]:
            country_data = {
                "country": item["country"]["value"], 
                "year":item["date"],
                "gdp": item["value"]
            }
            gdp_data.append(country_data)
        gdp_data_df = pd.DataFrame(gdp_data, columns=['country', 'year', 'gdp'])
        gdp_data_df.to_csv(file_path, index=False)
        return gdp_data_df

    def get_life_expectancy(self, file_path):
        life_expectancy_url = config.get('life_expectancy_api', 'url') 
        response = requests.get(life_expectancy_url) 
        response.raise_for_status() 
        data = response.json() 
        life_expectancy_data = [] 
        for item in data[1]:
            country_data = {
                "country": item["country"]["value"], 
                "country_code": item["countryiso3code"],
                "year":item["date"],
                "Life expectancy at birth, total (years)": item["value"]    
            } 
            life_expectancy_data.append(country_data) 
        life_expectancy_df = pd.DataFrame(life_expectancy_data, columns=['country', 'country_code',
                                                                          'year','Life expectancy at birth, total (years)']) 
        life_expectancy_df.to_csv(file_path, index=False) 
        return life_expectancy_df 
    
    def get_unemployment_rate(self, file_path):
        unemployment_rate_url = config.get('unemployment_rate', 'url') 
        response = requests.get(unemployment_rate_url) 
        response.raise_for_status() 
        data = response.json() 
        unemployment_rate_data = [] 
        for item in data[1]:
            country_data = {
                "country": item["country"]["value"], 
            }
    
# create an instance of the WorldBankAPI classi
api = WorldBankAPI(url="https://api.worldbank.org/v2/")

# get the list of countries and save it to a CSV file
countries_df = api.get_countries(file_path="countries.csv")

# get GDP data for all countries and save it to a CSV file
gdp_df = api.get_gdp(file_path="gdp_data.csv")


