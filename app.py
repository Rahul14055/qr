import streamlit as st
import qrcode
import io
import os

st.title("📂 Upload Any File & Generate QR Code for Download")

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

uploaded_file = st.file_uploader("Upload any file (PDF, video, docx, etc.)")

if uploaded_file is not None:
    # Save the uploaded file
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write(f"Uploaded file: **{uploaded_file.name}** ({uploaded_file.type})")

    # Provide download button from the local file
    with open(file_path, "rb") as f:
        file_bytes = f.read()

    st.download_button(
        label="Download the uploaded file",
        data=file_bytes,
        file_name=uploaded_file.name,
        mime=uploaded_file.type,
    )

    # Construct public URL for the file
    # CHANGE THIS to your deployed app's URL!
    APP_URL = "https://aaj4oxzggizvfydpfhzuom.streamlit.app/"

    file_url = f"{APP_URL}/{UPLOAD_DIR}/{uploaded_file.name}"

    st.markdown(f"Download link: [**{file_url}**]({file_url})")

    # Generate QR code from public URL
    qr = qrcode.make(file_url)
    buf = io.BytesIO()
    qr.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.image(byte_im, caption="Scan to download the uploaded file", use_container_width=True)

    st.download_button(
        label="Download QR Code",
        data=byte_im,
        file_name="qr_code.png",
        mime="image/png",
    )
else:
    st.info("Upload a file to generate a QR code for download.")
