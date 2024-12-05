import json
import streamlit as st

st.markdown('''<h3 style='text-align: center; color: #023558;'>Imputation</h3>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Top 5 species by biome (plotly)</h4>''', unsafe_allow_html=True)
with open('example_data/MicW2Graph/top_species_plot_biome.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Multiline plot (altair)</h4>''', unsafe_allow_html=True)
with open('example_data/altair_multilineplot.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)
