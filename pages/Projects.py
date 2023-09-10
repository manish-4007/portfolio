import streamlit as st 
import pandas as pd 
import numpy as np 
from streamlit_card import card
from streamlit_extras.colored_header import colored_header
import webbrowser

st.set_page_config(layout='wide')

about_projects = """### I have keen interest in Data Science, AI, NLP, Machine Learning and Deep Learning and had done on projects with these skills. 
"""
st.title('Projects')
st.markdown(about_projects)
st.markdown("<p>(I also have some knowledge of Web Development and Cloud Technologies)</p>",unsafe_allow_html=True)
st.header("Some of the my works on these Technologies are listed here.")


def show_featured_projects():
    featured_repo =["YT-video-Transcription","Trip-Planner","Blog-Sentiment-Analysis","PDF-QnA-Expert","IPL-Data-Analysis", "diamond-Price-Prediction"]
    st.markdown('<br>',unsafe_allow_html=True)
    links= ""
    for repo in featured_repo:
        repo_link = f'https://github.com/manish-4007/{repo}'
        repo_card_link =f'https://github-readme-stats.vercel.app/api/pin/?username=manish-4007&repo={repo}&show_icons=true&theme=vue-dark'
        
        links += f"<a href='{repo_link}' style='margin: 10px; padding-bottom:30px;' ><img align='center' src='{repo_card_link}' /></a>"
        
    st.markdown(links,unsafe_allow_html=True)
    st.markdown('<br>',unsafe_allow_html=True)

def project_card(project):
    
    colored_header(
        label=project['title'],
        description=f"published at {project['date']} ",
        color_name="blue-green-70",
    )   
    st.markdown(f"<div style='justify-content: center; width:500px; margin: 5px;'><p>{project['description']}</p>", unsafe_allow_html=True)
    
    col1,col2,col3 = st.columns(3)
    with col1:
        if st.button("Source Code", key= project['title']):
            webbrowser.open_new_tab(project['github'])
    with col2:
        if project['demourl'] !='empty':
            if st.button("View App", key= f"app_{project['title']}"):
                webbrowser.open_new_tab(project['demourl'])
    with col3:
        if project['aboutapp'] !='empty':
            if st.button("Tutorial", key= f"tut_{project['title']}"):
                webbrowser.open_new_tab(project['aboutapp'])

  
colored_header(
            label='Featured Project works',
            description=f" ",
            color_name="orange-70",
        )
show_featured_projects()

projects = pd.read_csv('./resources/portfolio_data.csv')
projects = projects.fillna('empty')
projects['date'] =pd.to_datetime(projects['date']).dt.date
projects = projects.sort_values('date',ascending=False)

project_types = list(projects['tech'].unique())
project_types.insert(0, 'All Projects')

#Added a filter based on Technologies option while showing all projects

filter_col = st.columns(2)
with filter_col[0]:
    colored_header(
                label='All my projects',
                description=f" ",
                color_name="orange-70",
            )
with filter_col[1]:
    tech_cat = st.selectbox('Technologies',options=project_types)
    
if tech_cat =='All Projects':
    tech_projects = projects.reset_index()
else:
    tech_projects = projects[projects['tech']==tech_cat].reset_index()

#Showcasing project in two-column tiles
cols = st.columns(2)
for i,project in tech_projects.iterrows():
    with cols[i%2]:
        if project['image'] =='empty':
            img_path = f"./resources/images/{project['title']}.png"
            # st.write('<div style="width: 300px; margin: 10px;">', unsafe_allow_html=True)
            st.image(img_path,width=500)
        else:
            st.image(project['image'],width=500)
        project_card(project)

        st.write('</div>', unsafe_allow_html=True)
        