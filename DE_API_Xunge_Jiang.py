import argparse
import requests
import pandas as pd
import time
import warnings
warnings.filterwarnings('ignore')

# IQAir api key
API_KEY = 'c05a32e6-c52b-4333-83e9-b2911e009b96'
BASE_URL = 'http://api.airvisual.com/v2'


def call_iq_air_api(param, state, country, city=None):
    try:
        url = f'{BASE_URL}/{param}?state={state}&country={country}&key={API_KEY}'
        if city:
            url += f'&city={city}'
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
    except Exception:
        raise


def get_air_quality(country, state):
    # get json and city name list within the state
    city = call_iq_air_api('cities', state, country)
    city_lst = [c['city'] for c in city['data']]

    # extract air quality information based on the city name and write to pandas dataframe
    df_aq = pd.DataFrame()
    for i, city_name in enumerate(city_lst[0:4]):
        if (i + 1) % 5 == 0:
            # pause after every 5 api calls but in this case, it will never reach this condition
            time.sleep(60)
        response_stations = call_iq_air_api('city', state, country, city_name)

        # flatten json files
        df_temp = pd.json_normalize(response_stations)
        df_aq = df_aq.append(df_temp)

    return df_aq.reset_index(drop=True)


def output_air_quality_data(country, state, schema=None):
    print("Getting air quality data...")
    aq = get_air_quality(country, state)

    if schema and schema == 'y':
        aq.info()

    # Write to files
    file_name = f'Air_Quality_{country}_{state}.csv'
    aq.to_csv(file_name,
              encoding='utf-8', index=False, header=True)
    print("Done writing to file:", file_name)


if __name__ == '__main__':
    # Read in-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-c",
                        "--country",
                        help="country name"
                        )
    parser.add_argument("-s",
                        "--state",
                        help="state name"
                        )
    parser.add_argument("-sch",
                        "--schema",
                        help="data schema"
                        )
    args = parser.parse_args()

    if not args.country:
        raise Exception('Missing country argument')

    if not args.state:
        raise Exception('Missing state argument')

    output_air_quality_data(args.country, args.state, args.schema)
