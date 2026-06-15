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

def hero():
        # Premium SaaS-style hero (dark gradient, badge, CTA, hero graphic)
        st.markdown(
                """
                <div class='hero'>
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
                            <!-- simple price-tag SVG with sparkles -->
                            <svg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg' class='sparkle'>
                                <defs>
                                    <linearGradient id='g1' x1='0' x2='1'>
                                        <stop offset='0%' stop-color='#6EE7B7'/>
                                        <stop offset='100%' stop-color='#60A5FA'/>
                                    </linearGradient>
                                </defs>
                                <g fill='none' fill-rule='evenodd'>
                                    <path d='M34 66 L100 22 L166 66 L100 166 Z' fill='url(#g1)' opacity='0.95' stroke='rgba(255,255,255,0.12)' stroke-width='2' />
                                    <circle cx='100' cy='70' r='10' fill='#fff' />
                                    <path d='M100 80 L120 110' stroke='rgba(255,255,255,0.6)' stroke-width='2' stroke-linecap='round' />
                                    <!-- sparkles -->
                                    <g fill='#fff' opacity='0.9'>
                                        <circle cx='160' cy='30' r='2.8'/>
                                        <circle cx='180' cy='60' r='1.8'/>
                                        <circle cx='140' cy='50' r='1.8'/>
                                        <rect x='30' y='20' width='3' height='8' rx='1' transform='rotate(25 31.5 24)' />
                                    </g>
                                </g>
                            </svg>
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
    # Short benefits list
    st.header('Why Campus Marketplace')
    st.markdown(
        """
        <div class='benefit-grid'>
            <div class='benefit-card'>
                <div class='feature-top'><div class='feature-icon' style='background:linear-gradient(135deg,#06b6d4,#3b82f6)'>
                    <svg width='20' height='20' viewBox='0 0 24 24' fill='none' xmlns='http://www.w3.org/2000/svg'><path d='M12 2L2 7l10 5 10-5-10-5z' fill='white'/><path d='M2 17l10 5 10-5' stroke='white' stroke-width='1.2' stroke-linecap='round' stroke-linejoin='round'/></svg>
                </div><div><div class='feature-title'>Save money</div><div class='feature-desc'>Find affordable textbooks and lab essentials.</div></div></div>
            </div>
            <div class='benefit-card'>
                <div class='feature-top'><div class='feature-icon' style='background:linear-gradient(135deg,#f97316,#f59e0b)'>
                    <svg width='20' height='20' viewBox='0 0 24 24' fill='none' xmlns='http://www.w3.org/2000/svg'><path d='M12 2L2 7l10 5 10-5-10-5z' fill='white'/></svg>
                </div><div><div class='feature-title'>Reuse resources</div><div class='feature-desc'>Extend item lifecycles and reduce campus waste.</div></div></div>
            </div>
            <div class='benefit-card'>
                <div class='feature-top'><div class='feature-icon' style='background:linear-gradient(135deg,#8b5cf6,#6366f1)'>
                    <svg width='20' height='20' viewBox='0 0 24 24' fill='none' xmlns='http://www.w3.org/2000/svg'><path d='M12 2L2 7l10 5 10-5-10-5z' fill='white'/></svg>
                </div><div><div class='feature-title'>Build community</div><div class='feature-desc'>Connect with other students in your faculty.</div></div></div>
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
