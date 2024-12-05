import pandas as pd
import json
import streamlit as st

st.markdown('''<h3 style='text-align: center; color: #023558;'>Cox proportional hazards regression</h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'>Cox proportional hazards regression was run univariately over all the proteins while adjusting for EGFR, Age at baseline, sex, ethnicity (white, black, hispanic, other), education (less than highschool, high school, college and above), BMI (underweight, helathy, overweight, obese), smoking status (current, former, never), and activity levels (little, moderate, a lot). These confounders were chosen based on the risk factors for dementia (see 'Confounder selection' panel). Subsequently, the p-values were adjusted for multiple testeing via false discovery rate (FDR) adjustment with an alpha of 0.05. </p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Kaplan Meier plot of discovery cohort</h4>''', unsafe_allow_html=True)

st.image('DemProt/03_feature_selection/kaplan_meier_plot.png', caption='Kaplan Meier survival plot for the whole discovery cohort over time.', use_column_width=True)

st.markdown('''<figcaption style='text-align: left; color: #000000;'>Kaplan Meier survival plot for the whole discovery cohort over time.</figcaption>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Volcano plot of Cox regression results</h4>''', unsafe_allow_html=True)
with open('DemProt/03_feature_selection/COX_volcano.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<figcaption style='text-align: left; color: #000000;'>Results from Cox regression. Proteins with a p-value < 0.1 are coloured for up-and down regulation. The colored proteins were chosen as biomarker candidates. Their predictive power is tested in the following models.</figcaption>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Cox regression results</h4>''', unsafe_allow_html=True)
df = pd.read_excel('DemProt/03_feature_selection/COX_regression.xlsx')
st.dataframe(df, use_container_width=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Coefficient dependency on alpha penalizer</h4>''', unsafe_allow_html=True)
with open('DemProt/03_feature_selection/COX_paths.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>P-value dependency on alpha penalizer</h4>''', unsafe_allow_html=True)
with open('DemProt/03_feature_selection/COX_paths_pvals.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)
