import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.express as px
import base64
import io

def pyplot_chart(data, x, y, **kwargs):
    fig = plt.figure()
    plot = sns.scatterplot(x, y, data = data, **kwargs)
    return fig

def alt_chart(data, x, y, **kwargs):
    plot = alt.Chart(data).mark_point().encode(
                        alt.X(x, scale=alt.Scale(zero=False)),
                        alt.Y(y, scale=alt.Scale(zero=False, padding=1)),
                        **kwargs,
                        tooltip=[x, y, *kwargs.values()],
                    ).interactive()
    return plot

def px_chart(data, x, y, **kwargs):
    plot = px.scatter(data, x, y, **kwargs)
    return plot

def download_link(obj, download_filename):
    """
    Generates a link to download the given object_to_download.

    object_to_download (str, pd.DataFrame):  The object to be downloaded.
    download_filename (str): filename and extension of file. e.g. mydata.csv, some_txt_output.txt
    download_link_text (str): Text to display for download link.

    Examples:
    download_link(YOUR_DF, 'YOUR_DF.csv', 'Click here to download data!')
    download_link(YOUR_STRING, 'YOUR_STRING.txt', 'Click here to download your text!')

    """
    if isinstance(obj, pd.DataFrame):
        csv_obj = obj.to_csv(index=False)
        towrite = io.BytesIO()
        xlsx_obj = obj.to_excel(towrite, encoding="latin-1", index=False, header=True)
        towrite.seek(0)

    # some strings <-> bytes conversions necessary here
    href = {}
    for o, file_type in zip([csv_obj, xlsx_obj], ["csv", "excel"]):
        try:
            b64 = base64.b64encode(o.encode()).decode()

        except AttributeError as e:
            b64 = base64.b64encode(towrite.read()).decode()
        extension = ".csv" if file_type == "csv" else ".xlsx"
        href[
            file_type
        ] = f'<a href="data:file/txt;base64,{b64}" download="{download_filename}{extension}">Download as {file_type}!</a>'
    with st.beta_expander("Download Data"):
        st.markdown(href["csv"], unsafe_allow_html=True)
        st.markdown(href["excel"], unsafe_allow_html=True)
