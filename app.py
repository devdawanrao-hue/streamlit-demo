import streamlit as st
from datetime import datetime
import os
from data_manager import load_listings

# Configure the top-level page (this file acts as the Home page)
st.set_page_config(page_title='Campus Marketplace', page_icon='🏫', layout='wide')

# Load custom CSS from the assets folder if available
def local_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css('assets/styles.css')

# Stock image URLs (Unsplash & free sources)
STOCK_IMAGES = {
    'hero': 'https://images.unsplash.com/photo-1523875335684-37898b6baf30?w=1200&q=80',  # Campus scene
    'books': 'https://images.unsplash.com/photo-1507842217343-583f20270319?w=400&q=80',  # Stack of books
    'save': 'https://images.unsplash.com/photo-1573497491363-e6169e7f214b?w=400&q=80',  # Piggy bank / savings
    'reuse': 'https://images.unsplash.com/photo-1559015615-cd4628902d4a?w=400&q=80',  # Recycling / sustainability
    'community': 'https://images.unsplash.com/photo-1552664730-d307ca884978?w=400&q=80',  # People / teamwork
}

def hero():
        # Premium SaaS-style hero (dark gradient, badge, CTA, hero graphic + image)
        st.markdown(
                f"""
                <div class='hero' style='background-image:url({STOCK_IMAGES["hero"]}); background-size:cover; background-position:center; background-blend-mode:overlay;'>
                    <div class='hero-left'>
                        <div class='hero-badge'><span style='font-size:16px;'>🎓</span><span>Campus Marketplace</span></div>
                        <h1>Campus Marketplace</h1>
                        <p class='lead'>Affordable textbooks, lab gear and study tools — buy, sell, and reuse on campus.</p>
                        <a class='hero-cta' href='/'>
                            <span>Explore listings</span>
                            <svg width='18' height='18' viewBox='0 0 24 24' fill='none' xmlns='http://www.w3.org/2000/svg' style='display:inline-block; vertical-align:middle'>
                                <path d='M5 12h14' stroke='#fff' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/>
                                <path d='M12 5l7 7-7 7' stroke='#fff' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/>
                            </svg>
                        </a>
                    </div>
                    <div class='hero-right'>
                        <div class='hero-graphic'>
                            <!-- stock image on the right -->
                            <img src='{STOCK_IMAGES["books"]}' style='border-radius:20px; box-shadow:0 15px 50px rgba(0,0,0,0.3); width:100%; height:auto;' alt='Books' />
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
        )

def stats(listings):
    # Show summary metrics for quick glance
    total = len(listings)
    sold = len([r for r in listings if r.get('status')=='sold'])
    active = total - sold
    col1, col2, col3, col4 = st.columns(4)
    col1.metric('Total listings', total)
    col2.metric('Active', active)
    col3.metric('Sold', sold)
    col4.metric('Since', datetime.now().year)

def featured(listings):
    # Show a small grid of featured/active listings
    st.header('Featured Listings')
    cols = st.columns(3)
    featured = [l for l in listings if l.get('status')=='active'][:6]
    for i, l in enumerate(featured):
        with cols[i%3]:
            st.subheader(l.get('title'))
            st.write(f"**{l.get('category')}** — {l.get('condition')} — ₹{l.get('price')}")
            st.write(l.get('description')[:120] + '...')

def benefits():
    # Short benefits list with stock images
    st.header('Why Campus Marketplace')
    st.markdown(
        f"""
        <div class='benefit-grid'>
            <div class='benefit-card' style='background-image:url({STOCK_IMAGES["save"]}); background-size:cover; background-position:center; position:relative;'>
                <div style='position:absolute; inset:0; background:linear-gradient(135deg,rgba(6,182,212,0.85),rgba(59,130,246,0.85)); border-radius:20px;'></div>
                <div class='feature-top' style='position:relative; z-index:2;'><div class='feature-icon' style='background:linear-gradient(135deg,#06b6d4,#3b82f6);'>
                    <svg width='20' height='20' viewBox='0 0 24 24' fill='none' xmlns='http://www.w3.org/2000/svg'><path d='M12 2L2 7l10 5 10-5-10-5z' fill='white'/><path d='M2 17l10 5 10-5' stroke='white' stroke-width='1.2' stroke-linecap='round' stroke-linejoin='round'/></svg>
                </div><div><div class='feature-title' style='color:#fff;'>Save money</div><div class='feature-desc' style='color:#fff;'>Find affordable textbooks and lab essentials.</div></div></div>
            </div>
            <div class='benefit-card' style='background-image:url({STOCK_IMAGES["reuse"]}); background-size:cover; background-position:center; position:relative;'>
                <div style='position:absolute; inset:0; background:linear-gradient(135deg,rgba(249,115,22,0.85),rgba(245,158,11,0.85)); border-radius:20px;'></div>
                <div class='feature-top' style='position:relative; z-index:2;'><div class='feature-icon' style='background:linear-gradient(135deg,#f97316,#f59e0b);'>
                    <svg width='20' height='20' viewBox='0 0 24 24' fill='none' xmlns='http://www.w3.org/2000/svg'><path d='M12 2L2 7l10 5 10-5-10-5z' fill='white'/></svg>
                </div><div><div class='feature-title' style='color:#fff;'>Reuse resources</div><div class='feature-desc' style='color:#fff;'>Extend item lifecycles and reduce campus waste.</div></div></div>
            </div>
            <div class='benefit-card' style='background-image:url({STOCK_IMAGES["community"]}); background-size:cover; background-position:center; position:relative;'>
                <div style='position:absolute; inset:0; background:linear-gradient(135deg,rgba(139,92,246,0.85),rgba(99,102,241,0.85)); border-radius:20px;'></div>
                <div class='feature-top' style='position:relative; z-index:2;'><div class='feature-icon' style='background:linear-gradient(135deg,#8b5cf6,#6366f1);'>
                    <svg width='20' height='20' viewBox='0 0 24 24' fill='none' xmlns='http://www.w3.org/2000/svg'><path d='M12 2L2 7l10 5 10-5-10-5z' fill='white'/></svg>
                </div><div><div class='feature-title' style='color:#fff;'>Build community</div><div class='feature-desc' style='color:#fff;'>Connect with other students in your faculty.</div></div></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def sustainability():
    # Sustainability note
    st.header('Sustainability')
    st.markdown('Reducing waste by extending product lifecycles and keeping items circulating on campus.')

def main():
    # Sidebar menu prompt
    st.sidebar.title('Campus Marketplace')
    st.sidebar.markdown('Use the top-left page menu to navigate.')

    # Load listings from CSV via data_manager
    listings = load_listings()

    # Render sections
    hero()
    st.markdown('---')
    st.markdown('<div class="section-card"><h2>Project overview</h2><p>A lightweight, student-first marketplace for textbooks, lab coats, calculators and other academic tools, designed to reduce costs and keep campus resources circulating.</p></div>', unsafe_allow_html=True)
    stats(listings)
    st.markdown('---')
    featured(listings)
    st.markdown('---')
    benefits()
    st.markdown('---')
    sustainability()

if __name__ == '__main__':
    main()
