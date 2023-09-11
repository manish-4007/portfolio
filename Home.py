import streamlit as st 
st.set_page_config(page_title="Digital CV|Manish Rai Chodhury",page_icon="random",layout='wide')
from streamlit_extras.streaming_write import write
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.colored_header import colored_header
from streamlit_extras.grid import grid
from pages.Projects import show_featured_projects
import webbrowser, time


def write_profession(prof):
    for word in prof:
        yield word + " | "
        time.sleep(0.25)

        # log_container.empty()
def my_intro():
    col1,col2 = st.columns(2)
    with col1:
        cols = st.columns(3)
        with cols[1]:
            # st.image('./resources/images/my_img.jpg', width= 200)
            st.image("./resources/images/profile-pic.png", width= 300)
    with col2:
        st.markdown("""<style>
                .intro{
                    display:flex;
                    flex-direction: column;
                    justify-content:  center;
                    align-items: center;
                    margin: 10px;
                    margin-bottom:  2px;
                }
            </style>""",unsafe_allow_html=True)
        st.markdown(f"""
            <div class="intro">
                <h4>Hi Everyone 👋</h4> <h3> I am Manish Rai Chodhury </h3>
            </div>""",unsafe_allow_html=True)
        write(write_profession(['Data Scientist', 'AI/ML Engineer','NLP Engineer', 'Data Analyst' ,"Freelancer", 'Python Developer', 'Web Developer',"Django Developer", "Problem Solver"]))


def about_myself():
    
    col1,col2 = st.columns(2)
    with col2:
        cols = st.columns(5)
        if cols[1].button('Linkedin',use_container_width=True):
            webbrowser.open_new_tab("https://www.linkedin.com/in/manish-rai-chodhury-170318197/")
        if cols[2].button('GitHub',use_container_width=True):
            webbrowser.open_new_tab("https://github.com/manish-4007")
        if cols[3].button('Kaggle',use_container_width=True):
            webbrowser.open_new_tab("https://www.kaggle.com/manishraichodhury")
        st.image('./resources/business-analysis.gif')# Add a download button
        with open("./resources/Resume.pdf", "rb") as file:
            st.download_button(
                label="Resume",
                data= file,
                key="download_resumev",
                help="Click here to download my resume",
                file_name='Manish_Resume.pdf',
                use_container_width = True
            )

    with col1:
        # st.subheader('About Me')
        about_me = """
        
    - A data scientist who usually play with digital data and with some analyizing , modificaiton  and transformation of these data try to create modern solutions to solve modern problems.
        
    - I possess expertize in Machine Learning, AI models, Data Science, Data Analysis, and Data Visualization.        

    - I always explore new technologies and frameworks. I have worked on projects with these skills and frameworks, which have helped me to hone my problem-solving abilities.
        
        """
        
        skills_log = f""" 
            <h3 >About Me </h3><div>{about_me}</div><br><br>
            <h4 > Data Science and Analytical Skills:</h4>
            <p>
            <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
            <a href="https://www.mongodb.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original-wordmark.svg" alt="mongodb" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://www.sqlite.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> </a>  
            # <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a> <a href="https://numpy.org/" target="_blank" rel="noreferrer"> <img src="https://numpy.org/images/logo.svg" alt="numpy" width="40" height="40"/> </a> <a href="https://scipy.org/" target="_blank" rel="noreferrer"> <img src="https://scipy.org/images/logo.svg" alt="scipy" width="40" height="40"/> </a> <a href="https://matplotlib.org/stable/" target="_blank" rel="noreferrer"> <img src="https://matplotlib.org/stable/_static/images/logo_dark.svg" alt="matplotlib" width="80" height="40"/> </a> <a href="https://seaborn.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt="seaborn" width="40" height="40"/> </a>   <a href="https://plotly.com/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Plotly-logo.png/330px-Plotly-logo.png" alt="plotly" width="80" height="40"/> </a><a href="https://scikit-learn.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/> </a> <a href="https://powerbi.microsoft.com/en-in/" target="_blank" rel="noreferrer"> <img src="https://res.cloudinary.com/hevo/image/upload/f_auto,q_auto/v1685882496/hevo-learn-1/microsoft-power-bi-logo_151265f430f.png?_i=AA" alt="plotly" width="70" height="40"/> </a> 
            <a href="https://spacy.io/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/8/88/SpaCy_logo.svg" alt="opencv" width="60" height="40"/> </a> <a href="https://www.nltk.org/" target="_blank" rel="noreferrer"> <img src="https://static.javatpoint.com/tutorial/ai/images/natural-language-toolkit2.png" alt="opencv" width="80" height="40"/> </a> 
            <a href="https://opencv.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/opencv/opencv-icon.svg" alt="opencv" width="40" height="40"/> </a> <a href="https://www.tensorflow.org" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="tensorflow" width="40" height="40"/> </a> <a href="https://pytorch.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="pytorch" width="40" height="40"/> </a>  <a href="https://keras.io/" target="_blank" rel="noreferrer"> <img src="https://static.javatpoint.com/tutorial/keras/images/keras.png" alt="keras" width="40" height="40"/> </a> 
            <a href="https://huggingface.co/" target="_blank" rel="noreferrer"> <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" alt="huggingface" width="30" height="40"/> </a> 
            <a href="https://www.langchain.com/" target="_blank" rel="noreferrer"> <img src="https://www.freecodecamp.org/news/content/images/size/w1000/2023/05/Screenshot-2023-05-29-at-5.40.38-PM.png" alt="keras" width="120" height="40"/> </a>  <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a> 
    </p>
        """
        st.markdown(skills_log,unsafe_allow_html = True)
        
    # st.button('Resume',use_container_width = True)
    # Add a download button
    # with open("./resources/Resume.pdf", "rb") as file:
    #     st.download_button(
    #         label="Resume",
    #         data= file,
    #         key="download_resume",
    #         help="Click here to download my resume",
    #         file_name='Manish_Resume.pdf',
    #         use_container_width = True
    #     )

def job_card(job):
    
        st.markdown(f"<br>",unsafe_allow_html=True)
        my_grid = grid([5,1],[5,1],vertical_align='bottom')
        # cols = my_grid.columns(1)
        # with cols[0]:
        my_grid.subheader(f"{job['role']}")
        colored_header(
            label='',
            description=f"Skills: {job['skills']}",
            color_name="blue-green-70",
        )
        my_grid.write( f"- {job['duration']}")  
        my_grid.write(f"{job['company']}")  
        my_grid.write( f" {job['location']}")      
        st.write(f"{job['description']}")
        st.markdown(f"<br>",unsafe_allow_html=True)

def my_experience():
    
    job ={
            1:{
                'role':'Subject Matter Expert',
                'company': 'Chegg Inc. · Part-time ',
                'location':"remote",
                'duration': 'Apr 2023 - Present',
                'description': """
                - Collaborated with students to complete homework assignments, identify lagging skills, and correct weaknesses.
                - 200+ Questions on Statistics, Linear Algebra, Probability, and Advance Mathematics.""",
                "skills": "Subject Expertise · Communication · problem-solving abilities · Interpersonal Communication · Time Management · Analytical Thinking · Leadership · Teaching and Tutoring"
            },
            2:{
                'role':'Data Science And Machine Learning Internship',
                'company': ' YBI Foundation · Internship',
                'location':"remote",
                'duration': 'Jul 2023 - Aug 2023',
                'description': """
                    - Get knowledge about Data Science ML in-depth and tackle the Large Dataset consisting of outliers and imbalanced data with lots of features.
                    - Apply Machine Learning models and select the best model which fits the problem Statements.
                    - Increases the performance of the model by 12%-15% """,
                "skills": "Data Preprocessing · Exploratory Data Analysis · Feature Engineering · ML Algorithms"
            },
            3:{
                'role':'Data Science Intern',
                'company': 'The Sparks Foundation · Internship',
                'location':"remote",
                'duration': 'Jan 2023 - Mar 2023',
                'description': """
                    - Make a Power BI Dashboard on IPL Dataset and one project on Credit Card Fraud Detection Machine Learning project.
                    - Identified, analyzed, and interpreted trends or patterns in complex data sets by finding correlations and visualizing them with charts.""",
                "skills": "Analytical Skills · Statistical Data Analysis · Microsoft Power BI · Classification · Machine Learning · Data Science · Data Visualization"
            },
            4:{
                'role':'Machine Learning Intern',
                'company': 'Suvidha Foundation (Suvidha Mahila Mandal) · Internship',
                'location':"Nagpur, Maharashtra, India · Hybrid",
                'duration': 'Jan 2023 - Feb 2023 ',
                'description': """
                    - Build an abstractive Text summarizer with NLP and Deep Learning which takes a text as input and then with text transformation and text generation with the help of DL.
                    - This summarizer retained the context of the original text by forming new words. """,
                "skills": "Recurrent Neural Networks (RNN) · Attention Neural Network · Natural Language Processing (NLP) · Text Classification · Text Analytics · TensorFlow · Data Science · Deep Learning"
            },
            5:{
                'role':'Machine Learning Industrial Trainee',
                'company': 'Internshala · Apprenticeship/Internship',
                'location':"Remote",
                'duration': 'Jul 2022 - Sep 2022',
                'description': """
                    - Prototyped machine learning applications and quickly determined application viability. Studied new technologies to support machine learning applications. 
                    - Designed, implemented, and evaluated new models and rapid software prototypes to solve problems in machine learning and systems engineering. 
                    - Leveraged artificial intelligence and machine learning algorithms for standalone products and enhanced existing product offerings. """,
                "skills": "Linear Regression · Logistic Regression · Decision Tree · Ensemble techniques · Clustering · Analytical Skills · Machine Learning · Data Science · Data Analysis"
            },
        }
    
    for i in job:
        job_card(job[i])
    
def my_skills():
    languages = """<br>
        <h4 align="left"> Programming Languages</h4>
        <p align="left"> <a href="https://www.cprogramming.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/c/c-original.svg" alt="c" width="40" height="40"/> </a> <a href="https://www.w3schools.com/cpp/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg" alt="cplusplus" width="40" height="40"/> </a>
        <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.java.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg" alt="java" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> 
    """
    databases="""<br>
        <h4 align="left"> Databases</h4>
        <a href="https://www.mongodb.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original-wordmark.svg" alt="mongodb" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://www.oracle.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/oracle/oracle-original.svg" alt="oracle" width="40" height="40"/> </a> <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> <a href="https://www.sqlite.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> </a>  """
        
    Visualiztion="""<br>
        <h4 align="left">Data Analysis & Visualization </h4><a href="https://matplotlib.org/stable/" target="_blank" rel="noreferrer"> <img src="https://matplotlib.org/stable/_static/images/logo_dark.svg" alt="matplotlib" width="100" height="40"/> </a> <a href="https://seaborn.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt="seaborn" width="40" height="40"/> </a><a href="https://plotly.com/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Plotly-logo.png/330px-Plotly-logo.png" alt="plotly" width="40" height="40"/><a href="https://powerbi.microsoft.com/en-in/" target="_blank" rel="noreferrer"> <img src="https://res.cloudinary.com/hevo/image/upload/f_auto,q_auto/v1685882496/hevo-learn-1/microsoft-power-bi-logo_151265f430f.png?_i=AA" alt="plotly" width="70" height="40"/> </a> """
    ML_libraies="""<br>
        <h4 align="left"> AI/ML tools </h4>
        <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a> <a href="https://numpy.org/" target="_blank" rel="noreferrer"> <img src="https://numpy.org/images/logo.svg" alt="numpy" width="40" height="40"/> </a> <a href="https://scipy.org/" target="_blank" rel="noreferrer"> <img src="https://scipy.org/images/logo.svg" alt="scipy" width="40" height="40"/> </a>  </a> <a href="https://scikit-learn.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/> </a> 
        <a href="https://spacy.io/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/8/88/SpaCy_logo.svg" alt="opencv" width="60" height="40"/> </a> <a href="https://www.nltk.org/" target="_blank" rel="noreferrer"> <img src="https://static.javatpoint.com/tutorial/ai/images/natural-language-toolkit2.png" alt="opencv" width="100" height="40"/> </a> 
        <a href="https://opencv.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/opencv/opencv-icon.svg" alt="opencv" width="40" height="40"/> </a> <a href="https://www.tensorflow.org" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="tensorflow" width="40" height="40"/> </a> <a href="https://pytorch.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="pytorch" width="40" height="40"/> </a>  <a href="https://keras.io/" target="_blank" rel="noreferrer"> <img src="https://static.javatpoint.com/tutorial/keras/images/keras.png" alt="keras" width="40" height="40"/> </a> 
        <a href="https://huggingface.co/" target="_blank" rel="noreferrer"> <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" alt="huggingface" width="40" height="40"/> </a> 
        <a href="https://www.langchain.com/" target="_blank" rel="noreferrer"> <img src="https://www.freecodecamp.org/news/content/images/size/w1000/2023/05/Screenshot-2023-05-29-at-5.40.38-PM.png" alt="keras" width="140" height="40"/> </a> """

    web_Dev="""<br>
    <h4 align="left"> Web Development</h4>
    <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> """

    frameworks= """<br>
    <h4 align="left"> Frameworks</h4><a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a>
        </a> <a href="https://reactjs.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" width="40" height="40"/> </a> <a href="https://tailwindcss.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/tailwindcss/tailwindcss-icon.svg" alt="tailwind" width="40" height="40"/> </a> 
        <a href="https://expressjs.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/express/express-original-wordmark.svg" alt="express" width="40" height="40"/> </a> <a href="https://nodejs.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original-wordmark.svg" alt="nodejs" width="40" height="40"/> </a>  """
        
    Devops ="""<br>
    <h4 align="left"> DevOps/ MLOps</h4>
    <a href="https://aws.amazon.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="aws" width="40" height="40"/> </a> <a href="https://azure.microsoft.com/en-in/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" alt="azure" width="40" height="40"/> </a> <a href="https://www.gnu.org/software/bash/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/gnu_bash/gnu_bash-icon.svg" alt="bash" width="40" height="40"/> </a> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> <a href="https://cloud.google.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/google_cloud/google_cloud-icon.svg" alt="gcp" width="40" height="40"/> </a> <a href="https://kubernetes.io" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/kubernetes/kubernetes-icon.svg" alt="kubernetes" width="40" height="40"/> </a> </p>"""

    Other_Utilities = """<br>
    <h4 align="left"> Other Utilities & tools</h4><a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> </a> <a href="https://www.selenium.dev" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/selenium-logo.svg" alt="selenium" width="40" height="40"/> </a> </p>

        """
        
    my_grid = grid([2,5],[2,1.7,1.7,1.7],[2,5],vertical_align='bottom')
    my_grid.markdown(Visualiztion,unsafe_allow_html=True)
    my_grid.markdown(ML_libraies,unsafe_allow_html=True)
    my_grid.markdown(languages,unsafe_allow_html=True)
    my_grid.markdown(databases,unsafe_allow_html=True)
    my_grid.markdown(web_Dev,unsafe_allow_html=True)
    my_grid.markdown(frameworks,unsafe_allow_html=True)
    my_grid.markdown(Devops,unsafe_allow_html=True)
    my_grid.markdown(Other_Utilities,unsafe_allow_html=True)


#! Showing Introduction
my_intro()

#! Tell me about yourself
about_myself()
st.write('---')
#Featured projects list
colored_header(
            label='Featured Projects',
            description=f" ",
            color_name="orange-70",
        )
show_featured_projects()

if st.button('more projects . . . . . '):
    switch_page('Projects')

st.write('---')
colored_header(
            label='Work Experience',
            description=f" ",
            color_name="orange-70",
        )
my_experience()

st.write('---')
colored_header(
            label='Skills',
            description=f" ",
            color_name="orange-70",
        )
my_skills()

st.write('---')
colored_header(
            label='Education',
            description=f" ",
            color_name="orange-70",
        )
mygrid= grid([4,1],vertical_align='bottom')
mygrid.write('- B.Tech in Computer Science and Engineering (CSE)  ')
mygrid.write('Aug 2019- Jun 2023')
mygrid.write(' ( From Heritage Institute of Technology )')
mygrid.write('Kolkata')
