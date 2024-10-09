#load the libraries - هنفعل المكتبات

import plotly.express as px
import streamlit as st
import pandas as pd
import numpy as np

#read the data

data = pd.read_csv('Top_1000_wealthiest_people.csv')

#display info about the data like data types null values and coluomns

print(data.info())

#display 15 rows

print(data.head(15))

#display the number of wealth people in each country
#عرفنا من خلاله ان امريكا هي الدولة المسيطرة في عدد المليارديرات

country_counts = data["Country"].value_counts()
print("Number of people in country")
print(country_counts)


#display the number of wealth people in each industry
#عرفنا من خلاله ان القطاع الاكبر في الثروة هو قطاع التكنولوجيا

industry_counts = data["Industry"].value_counts()
print("Number of people in industry")
print(industry_counts)


#display the important statistcs about data like the max of net worth is 199 billion (the wealthiest man in the world )
#عرفنا منه اهم الاحصائيات عن الداتا زي ان اغنى حد ثروته 199 مليار دولار


print(data.describe())



#######################################################################################################

# after making a simple exploratory data analysis thats time for visualizing using stremlit
#بعد التحليل البسيط و التعرف على البيانات الي عندي نبدء في عمل داش بورد


#page configurtion - تعديل اسم التاب و تغيير الايقونة


st.set_page_config(
    page_title="Wealthiest 1000 People Dashboard",
    page_icon="💸",
    )



#page title -عنوان الصفحة

st.title('welcome , this is Top 1000 wealthiest people dashboard 💸 ')





#group the data by the the country and make a new dataframe with this data - تجميع البيانات على اساس الدولة علشان نستخدمها في العرض

wealth_counts = data.groupby("Country").size().reset_index(name='wealth people count')




#visualize the data using the world map - عرض البيانات المجمعة في السطر الي قبله على هيئة هيتماب

fig = px.choropleth(
        data_frame=wealth_counts,
        locations="Country",
        locationmode="country names",
        color="wealth people count",
        hover_name="Country",
        color_continuous_scale="Bluered",
        title="The number of wealthy people in each country"
 )




st.plotly_chart(fig)


#calculate the precentage - حساب النسبة المؤية لكل دولة وعمل عمود جديد فيه النسبة

wealth_counts['percentage'] = (wealth_counts['wealth people count'] / wealth_counts['wealth people count'].sum()) * 100

wealth_counts['pie_chart_label'] = wealth_counts['Country'] + ": " + wealth_counts['percentage'].round(2).astype(str) + "%"


#display a piechart _ عرض الباي شارت


fig = px.pie(
        wealth_counts,
        names='pie_chart_label',
        values='wealth people count',
        title='The Percentage of Rich People in Each Country',
        hole=0.3
    )


st.title("The Percentage of Rich People in Each Country")
st.plotly_chart(fig)


#بنجمع البيانات على اساس العمل في كل قطاع - group data by industry

industry_counts = data.groupby("Industry").size().reset_index(name='industry_people_count')


fig = px.bar(
        industry_counts,
        x='Industry',
        y='industry_people_count',
        title="people working in each industry",
        labels={'industry_people_count': 'people number :', 'industry': 'industry'},
        color='industry_people_count',
        height=600
    )

st.title("number of people working in each industry")
st.plotly_chart(fig)



#make a side bar and display top ranked by net worth - عملت شريط في الجنب وظهرنا فيه اغنى عشر اشخاص
st.sidebar.title("top ranked by net worth 💸")
sorted_data = data.groupby('Name')['Net Worth (in billions)'].sum().sort_values(ascending = False).reset_index()
top_10_names = sorted_data['Name'].head(10)
st.sidebar.write(top_10_names)

