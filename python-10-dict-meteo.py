# vos imports ici
import csv

FILENAME = "python-08-fichiers-zip-data-meteo-france-synop.2015110112.csv"

def read_data_to_dicts(filename):
    
    with open(filename, newline='') as f:
        return list(csv.DictReader(f,delimiter=';'))

def filter_data(d):
    return {
        'numer_sta': d.get('numer_sta'),
        'date': d.get('date'),
        't': d.get('t'),
    }

def main():
    data = read_data_to_dicts(FILENAME)
    print(isinstance(data,list))
    print(isinstance(data[0], dict))
    print(filter_data(data[9]))
    pass


if __name__ == "__main__":
    main()