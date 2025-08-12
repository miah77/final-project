# Bliss Tide — COT FX Insights (Phase 1)

This repo is the Phase 1 foundation for a COT-based FX trend insight system.

## What is included
- app.py : Streamlit skeleton dashboard (loads sample data)
- fetch_cot.py : COT fetcher with sample-data fallback
- sample_cot_data.csv : sample dataset for offline testing
- config.example.json : template for SMTP/email and options
- requirements.txt : python dependencies

## Quickstart
1. Install dependencies: `pip install -r requirements.txt`
2. Run the Streamlit app: `streamlit run app.py`

## Next steps
- Replace sample data with real CFTC parsing in `fetch_cot.py`
- Add GitHub Actions to run `fetch_cot.py` weekly and commit updates
- Enhance dashboard with COT indicators and alerts
