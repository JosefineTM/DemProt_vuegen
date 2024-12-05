import json
import streamlit as st

st.markdown('''<h3 style='text-align: center; color: #023558;'>Full model</h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'>Model with all confounders and all candidate proteins as features.</p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Heatmap of feature importance rank in the models over time.</h4>''', unsafe_allow_html=True)
with open('DemProt/KNNImp_protein_medianNorm/04_models/heatmap_importances_combined.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<figcaption style='text-align: left; color: #000000;'>Visualization of the rank of importance of each feature in each of the models over the years. </figcaption>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>ROC curves of models over time.</h4>''', unsafe_allow_html=True)
with open('DemProt/KNNImp_protein_medianNorm/04_models/ROC_curve_combined_best.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<figcaption style='text-align: left; color: #000000;'>Description</figcaption>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>AUC over time</h4>''', unsafe_allow_html=True)
with open('DemProt/KNNImp_protein_medianNorm/04_models/dynamic_AUC.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<figcaption style='text-align: left; color: #000000;'>Description</figcaption>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>SHAP</h4>''', unsafe_allow_html=True)

st.image('DemProt/KNNImp_protein_medianNorm/SHAP.svg', caption='SHAP values of the features for every half year.', use_column_width=True)

st.markdown('''<figcaption style='text-align: left; color: #000000;'>SHAP values of the features for every half year.</figcaption>''', unsafe_allow_html=True)