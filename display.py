import streamlit as st
import time


# st.balloons()
# st.progress(10)

# with st.spinner('Wait for it...'):    
#     time.sleep(10)



st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))