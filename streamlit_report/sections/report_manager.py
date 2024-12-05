import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="DementiaProteomics",
    page_icon="docs/images/vuegen_logo.png",
)
st.logo("docs/images/vuegen_logo.png")
st.markdown(
    """<h1 style='text-align: center; color: #023858;'>DementiaProteomics</h1>""",
    unsafe_allow_html=True,
)

sections_pages = {}
homepage = st.Page("Home/Homepage.py", title="Homepage")
sections_pages["Home"] = [homepage]

Cox_proportional_hazards_regression = st.Page(
    "Discovery/Cox_proportional_hazards_regression.py",
    title="Cox proportional hazards regression",
)
Confounder_selection = st.Page(
    "Discovery/Confounder_selection.py", title="Confounder selection"
)
sections_pages["Discovery"] = [
    Cox_proportional_hazards_regression,
    Confounder_selection,
]

Introduction_to_the_random_forest_classifiers = st.Page(
    "Random_forest_models/Introduction_to_the_random_forest_classifiers.py",
    title="Introduction to the random forest classifiers",
)
Full_model = st.Page("Random_forest_models/Full_model.py", title="Full model")
Minimal_model = st.Page("Random_forest_models/Minimal_model.py", title="Minimal model")
Clinical_model = st.Page(
    "Random_forest_models/Clinical_model.py", title="Clinical model"
)
sections_pages["Random forest models"] = [
    Introduction_to_the_random_forest_classifiers,
    Full_model,
    Minimal_model,
    Clinical_model,
]

Clinical_Knowledge_Graph_for_associations_with_disease = st.Page(
    "Protein_annotation/Clinical_Knowledge_Graph_for_associations_with_disease..py",
    title="Clinical Knowledge Graph for associations with disease.",
)
sections_pages["Protein annotation"] = [
    Clinical_Knowledge_Graph_for_associations_with_disease
]

Imputation = st.Page("Data_preprocessing/Imputation.py", title="Imputation")
Adjustment = st.Page("Data_preprocessing/Adjustment.py", title="Adjustment")
sections_pages["Data preprocessing"] = [Imputation, Adjustment]

Quality_of_the_MS_analysis = st.Page(
    "Data_quality/Quality_of_the_MS_analysis.py", title="Quality of the MS analysis"
)
Quality_of_samples = st.Page(
    "Data_quality/Quality_of_samples.py", title="Quality of samples"
)
Protein_coverage_of_protein_biomarker_candidates_ = st.Page(
    "Data_quality/Protein_coverage_of_protein_biomarker_candidates_.py",
    title="Protein coverage of protein biomarker candidates ",
)
sections_pages["Data quality"] = [
    Quality_of_the_MS_analysis,
    Quality_of_samples,
    Protein_coverage_of_protein_biomarker_candidates_,
]

Combined_results = st.Page(
    "Combined_results/Combined_results.py", title="Combined results"
)
Conclusion = st.Page("Combined_results/Conclusion.py", title="Conclusion")
sections_pages["Combined results"] = [Combined_results, Conclusion]

report_nav = st.navigation(sections_pages)
report_nav.run()
