import json
import streamlit as st

st.markdown('''<h3 style='text-align: center; color: #023558;'>Adjustment</h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'>Multiple adjustement methods were tested on the imputed, filtered protein data. The DementiaProteomics GitHub repository includes three of these which are summarized in the figure below. The 'protein median' method was deemed most suitable for the data and thus used in this project. </p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Adjustment methods</h4>''', unsafe_allow_html=True)

st.image('DemProt/adjust_methods.svg', caption='Adjustment methods available in the DementiaProteomics repository. From left to right, the rigiusity of the adjsutment increases.', use_column_width=True)

st.markdown('''<figcaption style='text-align: left; color: #000000;'>Adjustment methods available in the DementiaProteomics repository. From left to right, the rigiusity of the adjsutment increases.</figcaption>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>PCA of unscaled data using KNN imputation, colored for plate</h4>''', unsafe_allow_html=True)
with open('example_data/DemProt/data_clean/KNN_protein_median/PCA_KNN_nonScaled_allProteins_plate.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<figcaption style='text-align: left; color: #000000;'>If you add one plate at a time, we see a clear drift downwards from plates 1 to 10, and then a jump for plate 11, 12, and 13. Hereafter, the </figcaption>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>PCA of unscaled data using KNN imputation, colored for type (pool or sample).</h4>''', unsafe_allow_html=True)
with open('example_data/DemProt/data_clean/KNN_protein_median/PCA_KNN_nonScaled_allProteins_type.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Proteomic drift, unadjusted data</h4>''', unsafe_allow_html=True)
with open('DemProt/01_protein_raw_visualization/drift_raw_all_mean_log2.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Proteomic drift, protein-median adjusted data</h4>''', unsafe_allow_html=True)

st.image('DemProt/02_data_transformation/drift_KNNImputed_protein_medianNorm_median.png', caption='', use_column_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Unscaled data, KNN imputed</h4>''', unsafe_allow_html=True)

st.image('example_data/DemProt/data_clean/Unscaled.svg', caption='', use_column_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Protein median scaled, KNN imputed</h4>''', unsafe_allow_html=True)

st.image('example_data/DemProt/data_clean/KNN_protein_median.svg', caption='', use_column_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Pool scaled, KNN imputed</h4>''', unsafe_allow_html=True)

st.image('example_data/DemProt/data_clean/KNN_pool.svg', caption='', use_column_width=True)
