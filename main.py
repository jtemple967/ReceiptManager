import streamlit as st
import database
from streamlit_cookies_controller import CookieController
import time

conn = database.ReceiptsDatabase()
controller = CookieController()
time.sleep(1)

def logout():
    if 'user' in st.session_state:
        controller.remove("ReceiptsUserId")
        del st.session_state['user']
    st.rerun()   

if 'database_init' in st.session_state:
    st.text("The receipts database has been initialized. The default user/password is admin/admin. Please change immediately after logging in.")
    del st.session_state['database_init']
    
if 'user' not in st.session_state:
    user = controller.get("ReceiptsUserId")
    if user:
        st.session_state['user'] = user

if 'user' not in st.session_state:
      
    pg = st.navigation([st.Page("login.py", title="Login")])

else:

    user_pages = []
    if st.session_state.user == "admin":
        user_pages.append(st.Page("listusers.py", title="List users"))
        user_pages.append(st.Page("adduser.py", title="Add user"))
    user_pages.append(st.Page("changepassword.py", title="Change password"))
    user_pages.append(st.Page(logout, title="Logout"))

    pages = {
        "Receipts": [
            st.Page("addreceipt.py", title="Add receipt"),
            st.Page("viewreceipt.py", title="View unrecorded receipts"),
            st.Page("viewallreceipt.py", title="View all receipts")
        ],
        "User": user_pages
    }
    st.sidebar.text(f"Welcome {st.session_state['user']}")

    pg=st.navigation(pages)

pg.run()


