import streamlit as st
from data_manager import load_listings
import os

# Browse page lists all active items and provides search/filters
st.set_page_config(page_title='Browse Listings')

def render_card(l):
    # Render a single listing card (image + details)
    st.markdown('<div class="listing-card">', unsafe_allow_html=True)
    cols = st.columns([1,3])
    with cols[0]:
        if l.get('image') and os.path.exists(l.get('image')):
            st.image(l.get('image'), use_column_width=True)
        else:
            st.markdown('<div style="font-size: 3rem;">📦</div>', unsafe_allow_html=True)
    with cols[1]:
        st.subheader(l.get('title'))
        st.markdown(f"<div class='listing-meta'>**{l.get('category')}** • {l.get('condition')} • ₹{l.get('price')}</div>", unsafe_allow_html=True)
        st.write(l.get('description'))
        st.markdown(f"<div class='listing-meta'>Seller: <strong>{l.get('seller')}</strong> — {l.get('contact')}</div>", unsafe_allow_html=True)
        if l.get('status')=='sold':
            st.info('SOLD')
    st.markdown('</div>', unsafe_allow_html=True)

def main():
    st.title('Browse Listings')
    # Load listings from CSV
    listings = load_listings()

    # Search and filters
    q = st.text_input('Search titles or descriptions')
    categories = ['All','Textbooks','Study Materials','Lab Coats','Scientific Calculators','Academic Tools']
    cat = st.selectbox('Category', categories)
    price_min, price_max = st.slider('Price range (₹)', 0.0, 10000.0, (0.0, 3000.0), step=50.0)
    sort = st.selectbox('Sort by', ['Newest','Price: Low→High','Price: High→Low'])

    filtered = []
    for l in listings:
        # text search
        if q and q.lower() not in (l.get('title','').lower() + l.get('description','').lower()):
            continue
        # category filter
        if cat!='All' and l.get('category')!=cat:
            continue
        # price range filter
        try:
            price = float(l.get('price') or 0)
        except Exception:
            price = 0
        if price < price_min or price > price_max:
            continue
        filtered.append(l)

    # sorting
    if sort == 'Price: Low→High':
        filtered.sort(key=lambda r: float(r.get('price') or 0))
    elif sort == 'Price: High→Low':
        filtered.sort(key=lambda r: float(r.get('price') or 0), reverse=True)

    st.write(f'{len(filtered)} results')
    for l in filtered:
        render_card(l)

if __name__ == '__main__':
    main()
