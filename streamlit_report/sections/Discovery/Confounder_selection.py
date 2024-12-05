import json
import streamlit as st

st.markdown('''<h3 style='text-align: center; color: #023558;'>Confounder selection</h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'>Finding confounders.</p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Risk factors of dementia</h4>''', unsafe_allow_html=True)

st.image('DemProt/03_confounder_selection/risk_factors.svg', caption='Risk factors for dementia used as a point of entry of choosing confounders for the Cox regresison model and features for the random forets models.', use_column_width=True)

st.markdown('''<figcaption style='text-align: left; color: #000000;'>Risk factors for dementia used as a point of entry of choosing confounders for the Cox regresison model and features for the random forets models.</figcaption>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Pearson's correlation between continous confounders</h4>''', unsafe_allow_html=True)
with open('DemProt/03_confounder_selection/corrmat_continous.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<figcaption style='text-align: left; color: #000000;'>Pearson's correlation.</figcaption>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Jaccard score between binary (and one-hot categorical) confounders</h4>''', unsafe_allow_html=True)
with open('DemProt/03_confounder_selection/corrmat_jaccard.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<figcaption style='text-align: left; color: #000000;'>Jaccard correlation.</figcaption>''', unsafe_allow_html=True)