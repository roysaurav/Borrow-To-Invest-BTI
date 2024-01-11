# conda activate streamlit
import streamlit as st
import pandas as pd
import scipy.sparse as sp
from streamlit.components.v1 import html



st.title("Borrow to Invest Effect on your Net Worth")
age = st.sidebar.number_input("Age", value=35)
home_value = st.sidebar.number_input("House Value", value=1000000)
#tot_return = st.sidebar.number_input("Return Net of borrowing Cost", value = 3)
interest_rate = st.sidebar.number_input("Yearly Interest Rate", value = 8)
Average_Expected_return = st.sidebar.number_input("Average Yearly Expected Return", value = 10)
home_appreciation = st.sidebar.number_input("Annual Home Appreciation Rate", value = 5)
ltv = st.sidebar.number_input("Loan to Value (%)", value = 65)
#tot_return = st.sidebar.number_input("Return Net of borrowing Cost", value = 3)

tot_return = Average_Expected_return - interest_rate
df = pd.DataFrame({ "Age":list(range(age, 100+1)) } )
df["home value"] = (home_value*(ltv/100))*((1 + home_appreciation/100)**df.index)
df["returns"] = ((1 + tot_return/100)**df.index)*df["home value"]
y_axis = "Portfolio Value"
df[y_axis] = df["returns"] - df["home value"]
fig = df.plot(kind="bar",x= "Age", title="Borrow to Invest Portfolio",y =y_axis, backend="plotly")
#fig.update_layout(yaxis_title="Sales")
fig.update_layout(title_text="Borrow to Invest Portfolio", title_x=0.38)


value_70_ = df[df["Age"] == 70][y_axis].iloc[0]

value_70 = round (value_70_/1e6, 2)
fig.add_annotation(
    x=70,
    y=value_70_,
    text=f"~${value_70} Million Extra Value Created by 70",
    arrowhead=1,
    font_color="white",
    bgcolor="orange"
)
explaination = f'''
If you start borrowing from your house and invest it at {age}, assuming you own 100% of the house and expect {Average_Expected_return}% average yearly return
and {home_appreciation}% home appreciation, by age 70 ,<b> you can have ${value_70} million in extra cash </b>
'''

explaination = f'''By borrowing against your house at age {age} and 
investing the money at a {Average_Expected_return}% annual return, you can accumulate an <b> extra ${value_70} million </b> by age 70, assuming your house appreciates by {home_appreciation}% per year.
'''
st.plotly_chart(fig, use_container_width=True, theme="streamlit")

st.markdown(explaination, unsafe_allow_html=True)
#st.write("Add anntation to graph \n Use microsoft forms", unsafe_allow_html=True)

#https://forms.office.com/r/NbWbtQwL7W
st.write('''<p style="font-size: 25px; text-align: center;"><b><a href="https://forms.office.com/r/NbWbtQwL7W"> Contact us for more information</a></b> </p>''',unsafe_allow_html=True)
Discliamer = '''
<p style="font-size: 12px; color: lightgrey;">
This site is for information and entertainment purposes only. The owner of this site is not an investment advisor, financial planner, nor a legal or tax professional. The articles and content on this site are of a general informational nature only and should not be relied upon for individual circumstances. The content and opinions expressed on this site are provided by the authors of this site and are theirs alone. Said content and opinions are not provided by any third party mentioned on this site and have not been reviewed, approved, or otherwise endorsed by any such third parties.
</p>


'''
st.write(Discliamer, unsafe_allow_html=True)