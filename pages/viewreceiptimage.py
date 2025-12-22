import database
import streamlit as st

conn = database.ReceiptsDatabase()
conn.database_connect()

# Get the image id
image_id = st.query_params.get("image_id", None)
# Get the image passed, if any
image_stream = conn.get_receipt_image(image_id)

with st.form("View image"):
    st.title("View image")
    if image_stream:
        st.image(image_stream)
    submit = st.form_submit_button("Go back", on_click=st.query_params.clear)    
