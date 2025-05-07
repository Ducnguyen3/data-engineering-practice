import requests
import pandas as pd
from bs4 import BeautifulSoup
import os

def main():
    url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    table = soup.find('table')
    
    target_timestamp = "2024-01-19 10:27"
    
    target_file = None
    for row in table.find_all('tr')[1:]: 
        cells = row.find_all('td')
        if len(cells) >= 2:
            timestamp = cells[1].text.strip()
            if timestamp == target_timestamp:
                target_file = cells[0].text.strip()
                break
    
    if not target_file:
        print("Could not find file with the specified timestamp")
        return
    
    download_url = f"{url}{target_file}"
    
    print(f"Downloading file: {target_file}")
    response = requests.get(download_url)
    
    with open(target_file, 'wb') as f:
        f.write(response.content)
    
    df = pd.read_csv(target_file)
    
    max_temp = df['HourlyDryBulbTemperature'].max()
    
    max_temp_records = df[df['HourlyDryBulbTemperature'] == max_temp]
    
    print(f"\nMaximum HourlyDryBulbTemperature: {max_temp}°F")
    print("\nRecords with maximum temperature:")
    
    important_columns = ['STATION', 'DATE', 'HourlyDryBulbTemperature', 'HourlyRelativeHumidity', 
                        'HourlyWindSpeed', 'HourlyPrecipitation']
    
    print(max_temp_records[important_columns].to_string())
    
    os.remove(target_file)

if __name__ == "__main__":
    main()
