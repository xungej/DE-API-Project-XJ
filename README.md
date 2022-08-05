# DE-API-Project-XJ

### Introduction

The goal of this project is to extract and transform data from IQAir Website that can return air quality information for all cities within a certain state and country using Python.

### Requirements
`pip install -r requirements.txt`

### Instructions

Run `DE_API_Xunge_Jiang.py` file with inline argument `-c` for country `-s` for state `-sch` for schema

If need to print schema which is optional, add `-sch y`

###### Example: 

`python3 DE_API_Xunge_Jiang.py -c USA -s California` <br /> 
`python3 DE_API_Xunge_Jiang.py -c USA -s Georgia -sch y`

### Details
+ Country and state (inputs) can be outputs from other APIs
+ Functions are reusable
+ Output 'Air_Quality_{country_name}_{state_name}.csv'
+ Data schemas as follows:

<img width="523" alt="Data_Schema" src="https://user-images.githubusercontent.com/39220278/183000245-39220282-d820-4a52-93fe-59e56b237e54.png">

### Helpful Links
- API introduction: https://api-docs.iqair.com/?version=latest#intro
- Website: https://www.iqair.com/us/commercial/air-quality-monitors/airvisual-platform/api

### Limitations

IQAir Public API limit:
- 5 calls/min
- 10,000/month

__Note__: 
Because of the API limitation, the current code only writes 4 rows of data to avoid system sleep time. If the whole code runs more than once within 60 seconds, it will return the error - `"requests.exceptions.HTTPError: 429 Client Error: Too Many Requests for url"`
