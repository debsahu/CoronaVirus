# Coronavirus Michigan Readings

Python based webscraper to get live readings from [Michigan Coronavirus COVID-19 page](https://www.michigan.gov/coronavirus)

## Python3 (recommended: use virtual environment)

Install required Python3 libraries

```
pip install --no-cache-dir -r requirements.txt
```

Run Python3 script

```
python coronavirus.py
```
## Docker

Build and Run

```
docker build -t coronavirus .
docker run --rm coronavirus
```