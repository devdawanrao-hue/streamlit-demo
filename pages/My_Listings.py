import streamlit as st
from data_manager import load_listings, update_listing, delete_listing, mark_sold

st.set_page_config(page_title='My Listings')

def main():
    """Allow seller to manage their listings (edit, mark sold, delete)."""
    st.title('My Listings')
    st.write('Enter your seller name to view and manage your listings.')
    seller = st.text_input('Seller name')
    if not seller:
        st.info('Enter your name to see listings you created.')
        return

    # Filter listings by seller name (case-insensitive)
    listings = [l for l in load_listings() if l.get('seller','').lower() == seller.lower()]
    if not listings:
        st.write('No listings found for', seller)
        return

    for l in listings:
        st.markdown('<div class="listing-card">', unsafe_allow_html=True)
        st.subheader(l.get('title'))
        st.markdown(f"<div class='listing-meta'>{l.get('category')} • {l.get('condition')} • <strong>₹{l.get('price')}</strong></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='listing-meta'>Seller: <strong>{l.get('seller')}</strong> — {l.get('contact')}</div>", unsafe_allow_html=True)
        st.write(l.get('description'))
        cols = st.columns(3)
        if cols[0].button('Edit', key='edit-'+l['id']):
            # simple inline edit flow — opens small inputs
            new_title = st.text_input('Title', value=l.get('title'), key='title-'+l['id'])
            new_price = st.number_input('Price', value=float(l.get('price') or 0), key='price-'+l['id'])
            if st.button('Save', key='save-'+l['id']):
                update_listing(l['id'], {'title':new_title, 'price':new_price})
                st.experimental_rerun()
        if cols[1].button('Mark sold', key='sold-'+l['id']):
            mark_sold(l['id'])
            st.experimental_rerun()
        if cols[2].button('Delete', key='del-'+l['id']):
            delete_listing(l['id'])
            st.experimental_rerun()
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
