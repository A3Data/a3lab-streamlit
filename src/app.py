import streamlit as st
from ml.visualization.streamlit.pages.intro import IntroPage
from ml.visualization.streamlit.pages.exploration import AnalysisPage
from ml.visualization.streamlit.pages.model_page import ModelPage

st.set_page_config("Hermione Titanic", page_icon=":ship:")

PAGES = {
    "Introduction": IntroPage,
    "Dataset Exploration": AnalysisPage,
    'ML Model': ModelPage
}

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))
    page = PAGES[selection]()
    page.write()

if __name__ == "__main__":
    main()