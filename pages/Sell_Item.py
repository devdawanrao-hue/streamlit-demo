import streamlit as st
from data_manager import add_listing
import os

st.set_page_config(page_title='Sell Item')

def main():
    """Form for creating a new listing. Saves images to assets/uploads and stores record in CSV."""
    st.title('Sell an Item')
    st.write('Create a listing for an item you want to sell to classmates.')

    # Preserve last used seller in session state for convenience
    if 'last_seller' not in st.session_state:
        st.session_state['last_seller'] = ''

    with st.form('sell'):
        title = st.text_input('Title')
        description = st.text_area('Description')
        category = st.selectbox('Category', ['Textbooks','Study Materials','Lab Coats','Scientific Calculators','Academic Tools'])
        price = st.number_input('Price (₹ INR)', min_value=0.0, max_value=100000.0, step=50.0)
        condition = st.selectbox('Condition', ['New','Like New','Good','Fair','Used'])
        seller = st.text_input('Your name', value=st.session_state.get('last_seller',''))
        contact = st.text_input('Contact info (email or phone)')
        image = st.file_uploader('Image (optional)', type=['png','jpg','jpeg'])
        submitted = st.form_submit_button('Create listing')

        if submitted:
            img_path = ''
            if image is not None:
                upload_dir = os.path.join('assets','uploads')
                os.makedirs(upload_dir, exist_ok=True)
                img_path = os.path.join(upload_dir, image.name)
                with open(img_path, 'wb') as f:
                    f.write(image.getbuffer())
            record = add_listing({
                'title': title,
                'description': description,
                'category': category,
                'price': price,
                'condition': condition,
                'seller': seller,
                'contact': contact,
                'image': img_path,
            })
            # remember seller for next time
            st.session_state['last_seller'] = seller
            st.success('Listing created')
            st.write(record)

if __name__ == '__main__':
    main()
