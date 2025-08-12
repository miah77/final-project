# fetch_cot.py
# Prototype COT fetcher: attempts to pull CFTC weekly DEA text dump and parse; falls back to sample data
import requests
import pandas as pd
from pathlib import Path
import sys

SAMPLE = Path('sample_cot_data.csv')
OUT = Path('cot_data_latest.csv')

def fetch_dea_text():
    url = 'https://www.cftc.gov/dea/futures/deanybtsf.htm'
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    return r.text

def build_from_sample():
    print('Using sample data')
    df = pd.read_csv(SAMPLE)
    df.to_csv(OUT, index=False)
    return df

def main():
    try:
        txt = fetch_dea_text()
        # NOTE: parsing DEA text is non-trivial and site format can change.
        # For Phase 1 we fallback to sample data. Implement robust CSV parsing later.
        return build_from_sample()
    except Exception as e:
        print('Fetch failed:', e)
        return build_from_sample()

if __name__ == '__main__':
    main()
