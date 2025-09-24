import streamlit as st
import os
from markitdown import MarkItDown, MarkItDownException

st.set_page_config(page_title="MarkItDown Web", layout="wide")

st.title("MarkItDown Web Converter")  # Translated title

# File upload section
uploaded_files = st.file_uploader("Select files to convert", accept_multiple_files=True)  # Translated upload prompt

if uploaded_files:
    for uploaded_file in uploaded_files:
        st.subheader(f"Processing file: {uploaded_file.name}")  # Translated subheader
        
        # Save uploaded file to a temporary directory
        temp_path = f"temp_{uploaded_file.name}"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        try:
            # Convert file
            result = MarkItDown.convert(temp_path)
            
            # Display conversion result
            st.text_area("Conversion result", result.text_content, height=300)  # Translated label
            
            # Provide download button
            st.download_button(
                label="Download Markdown file",  # Translated button label
                data=result.text_content,
                file_name=f"{os.path.splitext(uploaded_file.name)[0]}.md",
                mime="text/markdown"
            )
            
        except Exception as e:
            st.error(f"Conversion failed: {str(e)}")  # Translated error
        finally:
            # Clean up temporary files
            if os.path.exists(temp_path):
                os.remove(temp_path)

st.sidebar.markdown("""
## Instructions
1. Click "Select files to convert" to upload one or more files
2. The system will automatically convert files to Markdown format
3. You can preview the conversion results
4. Click "Download Markdown file" to save the results

## Supported file formats
- PDF
- Word
- PowerPoint
- Excel
- Image files
- Audio files
- HTML
- CSV, JSON, XML
- ZIP files
""")  # Translated sidebar
