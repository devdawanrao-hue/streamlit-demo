"""
Simple CSV-backed data manager for listings.
Handles loading, saving, adding, updating and deleting listings stored in data/listings.csv
"""
import os
import csv
import uuid
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
LISTINGS_CSV = os.path.join(DATA_DIR, 'listings.csv')

FIELDNAMES = ['id','title','description','category','price','condition','seller','contact','image','status','created_at']


def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)


def load_listings():
    """Return list of listings (dicts). Creates default file if missing."""
    ensure_data_dir()
    listings = []
    if not os.path.exists(LISTINGS_CSV):
        # no file yet, create empty CSV with header
        with open(LISTINGS_CSV, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
        return listings

    with open(LISTINGS_CSV, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # convert price to float
            try:
                row['price'] = float(row.get('price') or 0)
            except Exception:
                row['price'] = 0.0
            listings.append(row)
    # sort newest first
    listings.sort(key=lambda r: r.get('created_at',''), reverse=True)
    return listings


def save_listings(listings):
    ensure_data_dir()
    with open(LISTINGS_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        for r in listings:
            row = {k: (r.get(k) if k!='price' else str(r.get('price','')) ) for k in FIELDNAMES}
            writer.writerow(row)


def add_listing(data):
    listings = load_listings()
    new_id = str(uuid.uuid4())
    now = datetime.utcnow().isoformat()
    record = {
        'id': new_id,
        'title': data.get('title',''),
        'description': data.get('description',''),
        'category': data.get('category',''),
        'price': float(data.get('price') or 0),
        'condition': data.get('condition',''),
        'seller': data.get('seller',''),
        'contact': data.get('contact',''),
        'image': data.get('image',''),
        'status': 'active',
        'created_at': now,
    }
    listings.insert(0, record)
    save_listings(listings)
    return record


def update_listing(listing_id, updates):
    listings = load_listings()
    changed = False
    for r in listings:
        if r.get('id') == listing_id:
            r.update(updates)
            changed = True
            break
    if changed:
        save_listings(listings)
    return changed


def delete_listing(listing_id):
    listings = load_listings()
    new = [r for r in listings if r.get('id') != listing_id]
    if len(new) != len(listings):
        save_listings(new)
        return True
    return False


def mark_sold(listing_id):
    return update_listing(listing_id, {'status':'sold'})
