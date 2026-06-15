# Campus Marketplace

Lightweight Streamlit app to let students buy and sell academic resources on campus.

Features
- Home (hero, overview, featured listings)
- Browse listings with search, category and price filters
- Sell an item (form + image upload)
- My Listings (edit, delete, mark sold)
- Dashboard (basic analytics)
- About (PDD summary)

Quick start (local)

1. Clone the repository:

```bash
git clone <your-repo-url>
cd streamlit-demo
```

2. Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

The app stores data in `data/listings.csv` and uploaded images under `assets/uploads`.

Deploying
- GitHub: push the repo to GitHub.
- Vercel: you can deploy with a Dockerfile or use Streamlit Community Cloud. For Vercel deploy, add a `Dockerfile` and configure project to use it (not included by default).

Notes
- The app uses a CSV file backend; there's no external database.
- Missing files are created automatically on first run.
# streamlit-demo
my first streamline application
