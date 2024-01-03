import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# rand=np.random.normal(1, 4, size=20)
# st.write("normal",rand)

# fig, ax = plt.subplots()
# ax.hist(rand, bins=15) 
# st.pyplot(fig)



# df= pd.DataFrame(np.random.randn(10, 2),    columns=['x', 'y'])
# st.write("randn",np.random.randn(10,2))
# st.line_chart(df)



df = pd.DataFrame(np.random.randn(10, 2),    columns=['x', 'y'])
st.bar_chart(df)


