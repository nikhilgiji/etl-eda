# World Bank Open Data API Project

This project aims to extract data from the World Bank Open Data API on various indicators such as population, mortality rate, etc. The extracted data is then transformed using Pandas and loaded into a MySQL database. Finally, the data is used to create interactive dashboards using Plotly Dash.

## Requirements

To run this project, you will need the following:

- Python 3.x
- Pandas
- Requests
- MySQL
- Plotly Dash

## Installation

1. Clone the repository to your local machine.

```
https://github.com/nikhilgiji/worldbank-opendata-etl-eda.git
``` 


2. Install the required packages using pip.
```
pip install -r requirements.txt
```

3. Set up the MySQL database and configure the connection in the `config.py` file.

## Usage

To run the project, execute the following command:
```
python main.py
```

The script will fetch the data from the API, transform it, and load it into the MySQL database. Then, it will start the Plotly Dash app and display the interactive dashboards in your web browser.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

lastname 1, firstname1, matno1  
lastname 2, firstname2, matno2  

1) Write down the value of your seed:  
(your value here)
