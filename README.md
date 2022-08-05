# DE-API-Project-XJ

### Introduction

The goal of this project is to extract and transform data from IQAir Website that can return air quality information for all cities within a certain state and country using Python.

### Credentials and Limitations

API Key: 'c05a32e6-c52b-4333-83e9-b2911e009b96'

Public API limit:
- 5 calls/min
- 10,000/month

__Note__: Because of the limitation of API, the current code only output 4 rows of data to avoid system sleep time. Otherwise it will return `"TypeError: string indices must be integers"`

### Requirements
`pip install -r requirements.txt`

### Instructions

Run `DE_API_Xunge_Jiang.py` file with inline argument -c for country -s for state -sch for schema
If need to print schema, add -sch y
Example: 
`python3 DE_API_Xunge_Jiang.py -c USA -s California`

`python3 DE_API_Xunge_Jiang.py -c USA -s Georgia -sch y`


### Details
+ Country and state (inputs) can be outputs from other APIs. 
+ Output 'Air_Quality_{country_name}_{state_name}.csv'
+ Data schemas as follows:

<img width="523" alt="Data_Schema" src="https://user-images.githubusercontent.com/39220278/183000245-39220282-d820-4a52-93fe-59e56b237e54.png">


### Helpful Links
- API introduction: https://api-docs.iqair.com/?version=latest#intro
- Website: https://www.iqair.com/us/commercial/air-quality-monitors/airvisual-platform/api

