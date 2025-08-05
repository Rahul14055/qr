import streamlit as st
import qrcode
from PIL import Image
import io
import os

st.title("📂 Upload Any File & Generate QR Code for Download")

uploaded_file = st.file_uploader("Upload any file (PDF, video, docx, etc.)")

if uploaded_file is not None:
    # Create temp_dir if it doesn't exist
    if not os.path.exists("temp_dir"):
        os.makedirs("temp_dir")

    # Save uploaded file to a temporary location
    file_path = os.path.join("temp_dir", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write(f"Uploaded file: **{uploaded_file.name}** ({uploaded_file.type})")

    st.download_button(
        label="Download the uploaded file",
        data=uploaded_file,
        file_name=uploaded_file.name,
        mime=uploaded_file.type,
    )

    qr_data = f"File available to download: {uploaded_file.name}"

    qr = qrcode.make(qr_data)
    buf = io.BytesIO()
    qr.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.image(byte_im, caption="QR code for your uploaded file", use_container_width=True)

    st.download_button(
        label="Download QR Code",
        data=byte_im,
        file_name="qr_code.png",
        mime="image/png",
    )
else:
    st.info("Upload a file to generate a QR code for download.")
