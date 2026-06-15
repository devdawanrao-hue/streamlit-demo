import streamlit as st

st.set_page_config(page_title='About')

def main():
    """About page summarizing the PDD: problem, root causes, solution, and stakeholders."""
    st.title('About — Campus Marketplace')
    st.header('Problem statement')
    st.write('Students struggle to find affordable academic resources such as textbooks, lab coats, and scientific calculators. Access is fragmented and costly.')

    st.header('Root causes')
    st.write('- High cost of new textbooks and equipment\n- Limited second-hand options on campus\n- Students unaware of available resources')

    st.header('Proposed solution')
    st.write('A lightweight peer-to-peer marketplace specifically for campus that allows students to list, find, and purchase used academic items.')

    st.header('Expected benefits')
    st.write('- Reduced student expenses\n- Increased reuse and sustainability\n- Stronger campus community connections')

    st.header('Stakeholder analysis')
    st.write('- Students (buyers & sellers)\n- University sustainability offices\n- Student organizations')

if __name__ == '__main__':
    main()
