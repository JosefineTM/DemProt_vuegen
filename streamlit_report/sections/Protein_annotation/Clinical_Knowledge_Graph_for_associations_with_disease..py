import streamlit as st

st.markdown('''<h3 style='text-align: center; color: #023558;'>Clinical Knowledge Graph for associations with disease.</h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'>The Clinical Knowledge Graph is a graph database used for mining knowledge of diease associations and mechinsms of proteomics data. The protein biomarker canidates were quieried and known associations to other neurological diseases. </p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>CKG output</h4>''', unsafe_allow_html=True)
with open('DemProt/05_annotations/ckg_network.html', 'r') as f:
    html_data = f.read()
# Streamlit checkbox for controlling the layout
control_layout = st.checkbox('Add panel to control layout', value=True)
net_html_height = 1200 if control_layout else 630
# Load HTML into HTML component for display on Streamlit
st.components.v1.html(html_data, height=net_html_height)

st.markdown('''<figcaption style='text-align: left; color: #000000;'>Description, CKG</figcaption>''', unsafe_allow_html=True)