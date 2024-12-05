import pandas as pd
import streamlit as st

st.markdown('''<h3 style='text-align: center; color: #023558;'>Protein coverage of protein biomarker candidates </h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'>Protein sequence coverage is the degree to which the full protein has been covered by the precursors measured in the MS. The precursors may align with sequences in multiple proteins, and the final protein group call is a 'based guess' based on the precursors measured. Conversely, the coverage serve as a proxy for certainty that the protein is indeed the protein.</p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Coverage</h4>''', unsafe_allow_html=True)
df = pd.read_excel('DemProt/06_protein_coverage/coverage_df.xlsx')
st.dataframe(df, use_container_width=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>AFM</h4>''', unsafe_allow_html=True)

st.image('DemProt/06_protein_coverage/sequence_coverage_AFM.png', caption='', use_column_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>ALCAM</h4>''', unsafe_allow_html=True)

st.image('DemProt/06_protein_coverage/sequence_coverage_ALCAM.png', caption='', use_column_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>CNDP1</h4>''', unsafe_allow_html=True)

st.image('DemProt/06_protein_coverage/sequence_coverage_CNDP1.png', caption='', use_column_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>F13A1</h4>''', unsafe_allow_html=True)

st.image('DemProt/06_protein_coverage/sequence_coverage_F13A1.png', caption='', use_column_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>F13B</h4>''', unsafe_allow_html=True)

st.image('DemProt/06_protein_coverage/sequence_coverage_F13B.png', caption='', use_column_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>IGFBP2</h4>''', unsafe_allow_html=True)

st.image('DemProt/06_protein_coverage/sequence_coverage_IGFBP2.png', caption='', use_column_width=True)
