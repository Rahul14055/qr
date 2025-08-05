import streamlit as st
import qrcode
import io

st.title("🔗 QR Code Generator for URLs")

url = st.text_input("Enter a URL to generate its QR code:")

if url:
    # Generate QR code
    qr = qrcode.make(url)
    buf = io.BytesIO()
    qr.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.image(byte_im, caption="Scan this QR code to open the URL", use_container_width=True)

    st.download_button(
        label="Download QR Code",
        data=byte_im,
        file_name="qr_code.png",
        mime="image/png",
    )
else:
    st.info("Please enter a URL above to generate a QR code.")
