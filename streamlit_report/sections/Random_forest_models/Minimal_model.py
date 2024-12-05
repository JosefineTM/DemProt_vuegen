import json
import streamlit as st

st.markdown('''<h3 style='text-align: center; color: #023558;'>Minimal model</h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'>Model with only age and sex and the protein candidates as confounders.</p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Heatmap of feature importance rank in the models over time.</h4>''', unsafe_allow_html=True)
with open('DemProt/KNNImp_protein_medianNorm/04_models/sub_confounders/heatmap_importances_combined.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<figcaption style='text-align: left; color: #000000;'>This plot visualises the rank of importance of each feature in each of the models over the years. </figcaption>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>DemProt/KNNImp_protein_medianNorm/04_models/sub_confounders/ROC_curve_combined_best.json</h4>''', unsafe_allow_html=True)
with open('example_data/DemProt/mini_mod/ROC_curve_combined_best.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<figcaption style='text-align: left; color: #000000;'>Description</figcaption>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>AUC over time</h4>''', unsafe_allow_html=True)
with open('DemProt/KNNImp_protein_medianNorm/04_models/sub_confounders/dynamic_AUC.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<figcaption style='text-align: left; color: #000000;'>Description</figcaption>''', unsafe_allow_html=True)