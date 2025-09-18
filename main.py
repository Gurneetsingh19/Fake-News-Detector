import pandas as pd
import streamlit as st
import joblib

model = joblib.load("News_model")
Tfidf = joblib.load("News_tfidf")

st.markdown("<h1 style='text-align: center; color: white;'>Fake News Detector App 🕵️</h1>", unsafe_allow_html=True)
# st.title("Fake News Detector App")
st.set_page_config(layout='wide', page_title="Fake News Detector App", page_icon="🤖")

col1, col2 = st.columns([2, 1])

with col1:


    import base64

    def get_base64_of_bin_file(bin_file):
        """
        This function converts a binary file (like an image) into a
        base64 encoded string.
        """
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    def set_background_image(png_file):

        bin_str = get_base64_of_bin_file(png_file)
        page_bg_img = f'''
        <style>
        .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)


    set_background_image('ptu_hack/backgroundpic.png')



    st.subheader("Enter a news headline to check its authenticity..")

    input_text= st.text_area("Enter text here", height=50)

    btn= st.button("Predict")

    if btn:
        if input_text.strip() =="":
            st.warning("Please enter a news headline..")
        else:
            with st.spinner("Predicting..."):
                
                import time
                time.sleep(2)
                
                text_tfidf = Tfidf.transform([input_text])
                prediction = model.predict(text_tfidf)[0]
                if prediction == 1:
                    prediction = "Yeahh! It's Real"
                else:
                    prediction = "Ohh! It's Fake"

                if prediction == "Ohh! It's Fake":
                    st.error(f"{prediction}")
                else:
                    st.success(f"{prediction}")
            