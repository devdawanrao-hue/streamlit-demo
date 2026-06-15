import streamlit as st
import pandas as pd
from data_manager import load_listings

st.set_page_config(page_title='Dashboard')

def main():
    """Simple analytics dashboard using Streamlit charts."""
    st.title('Dashboard')
    listings = load_listings()
    df = pd.DataFrame(listings)
    total = len(df)
    sold = len(df[df['status']=='sold']) if not df.empty else 0
    active = total - sold

    # Key metrics at top
    c1,c2,c3 = st.columns(3)
    c1.metric('Total listings', total)
    c2.metric('Active', active)
    c3.metric('Sold', sold)

    st.markdown('---')
    st.subheader('Listings by Category')
    if not df.empty:
        cat_counts = df['category'].value_counts()
        st.bar_chart(cat_counts)

    st.subheader('Price distribution')
    if not df.empty:
        # show basic stats and a simple line chart of sorted prices
        st.write(df['price'].astype(float).describe())
        st.line_chart(df['price'].astype(float).sort_values().reset_index(drop=True))

if __name__ == '__main__':
    main()
