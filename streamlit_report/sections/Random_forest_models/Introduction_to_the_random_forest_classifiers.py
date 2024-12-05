import json
import streamlit as st

st.markdown('''<h3 style='text-align: center; color: #023558;'>Introduction to the random forest classifiers</h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'>To get a deeper understanding of the predictive power of the proteins, multipe random forest models were run as a binary classfifcaiton problems. Here, the proteins alongside the risk factors were used as features. To convert the data into a classification dataset, the cases were recoded depending on their time to event or time to end of follow up as described in the figure below. The predictive value of the proteins were assessed through permutation based feature importance and SHAP values. </p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Recoding of cases to non-cases over time.</h4>''', unsafe_allow_html=True)

st.image('example_data/DemProt/cases_recoding.png', caption='Illustration of the idea behind recoding of the cases and non-cases based on year cut-off. ', use_column_width=True)

st.markdown('''<figcaption style='text-align: left; color: #000000;'>Illustration of the idea behind recoding of the cases and non-cases based on year cut-off. </figcaption>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>N cases and cases over time.</h4>''', unsafe_allow_html=True)
with open('DemProt/KNNImp_protein_medianNorm/04_models/cases_non_cases_time.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<figcaption style='text-align: left; color: #000000;'>Depending on which time cut-off, the classifier is run on, the number of cases and non-cases change. Here, the development over time is presented.</figcaption>''', unsafe_allow_html=True)