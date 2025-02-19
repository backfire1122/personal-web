###########################
##   pages/Examples.py   ##
###########################

###############################################################
# import python libraries
###############################################################
import streamlit as st
import base64

###############################################################
# page info
###############################################################
st.set_page_config(
    page_title="Econ Releated Stuff",
)

###############################################################
# sidebar
###############################################################
with st.sidebar:
    st.markdown("""
                Include my powerpoint during my study times and my economic thingkings
                """)

###############################################################
# page content
###############################################################
st.title("Econ paper presentation Growing Like China ")


pdf_path = ".devcontainer/Growing_Like_China_Macro_Presenation"  # Path to your PDF file
with open(pdf_path, "rb") as pdf_file:
    st.pdf(pdf_file)


def get_pdf_download_link(pdf_file):
    with open(pdf_file, "rb") as f:
        pdf_data = f.read()
    b64 = base64.b64encode(pdf_data).decode()
    return f'<iframe src="data:application/pdf;base64,{b64}" width="700" height="500" type="application/pdf"></iframe>'

st.title("PDF Viewer")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Save the uploaded PDF to a temporary file
    with open("uploaded_file.pdf", "wb") as f:
        f.write(uploaded_file.read())
    
    # Display the PDF
    st.markdown(get_pdf_download_link("uploaded_file.pdf"), unsafe_allow_html=True)

