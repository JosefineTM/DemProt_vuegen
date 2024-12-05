import json
import streamlit as st

st.markdown('''<h3 style='text-align: center; color: #023558;'>Quality of samples</h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'>Quality of the sample handling. Samples were drawn in 119 different clinics from 20XX through 2015 and stored in freezers. To test the quality of the blood sampling, storage, and handling, the LFQ intensitites of proteins indicative of blood clotting and haemolysis was plotted as the function of sample order to evaluate the stability.</p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Haemolysis-indicating proteins</h4>''', unsafe_allow_html=True)
with open('DemProt/01_QC/hemolysis.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<figcaption style='text-align: left; color: #000000;'>Erythrocyte specific proteins (haemoglobin subunits) indicative of the level of haemolysis. </figcaption>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Blood-clotting factors</h4>''', unsafe_allow_html=True)
with open('DemProt/01_QC/fibrinogens.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<figcaption style='text-align: left; color: #000000;'>Fibrinogens indicative of the level of blood clotting.</figcaption>''', unsafe_allow_html=True)