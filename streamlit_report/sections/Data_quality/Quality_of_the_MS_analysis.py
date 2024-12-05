import pandas as pd
import json
import streamlit as st

st.markdown('''<h3 style='text-align: center; color: #023558;'>Quality of the MS analysis</h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'>Overall quality of the MS analysis, inlcudig stability, drift, and proteomic coverage.</p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Total quantified peptides</h4>''', unsafe_allow_html=True)

st.image('DemProt/01_QC/tot_quant_peptides_log.svg', caption='Total quantified peptides including events from the lab-log from the Proteomics Research Infrastructure (lab used for MS analysis).', use_column_width=True)

st.markdown('''<figcaption style='text-align: left; color: #000000;'>Total quantified peptides including events from the lab-log from the Proteomics Research Infrastructure (lab used for MS analysis).</figcaption>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>N proteins and peptides</h4>''', unsafe_allow_html=True)
with open('DemProt/01_QC/N_proteins_peptides.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<figcaption style='text-align: left; color: #000000;'>Number of proteins and peptides recorded in the samples as a function of sample order. </figcaption>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Proteomic depth</h4>''', unsafe_allow_html=True)
with open('DemProt/01_QC/protein_rank_plot.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<figcaption style='text-align: left; color: #000000;'>Protemic depth colored for percentage of valid values (percentage of samples in which the protein has been measured). Showing only proteins with a valid value of > 90%.</figcaption>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Inter- and intra-plate variablity</h4>''', unsafe_allow_html=True)
df = pd.read_excel('DemProt/01_QC/inter_intra_batch_variability.xlsx')
st.dataframe(df, use_container_width=True)
st.markdown('''<figcaption style='text-align: left; color: #000000;'>Inter- and intra-plate variablity as a proxy for inter- and intra-plate drift. A value under 5% is considered good. Variability calculated on filtered proteins.</figcaption>''', unsafe_allow_html=True)