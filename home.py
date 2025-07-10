import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(
    page_title='VNL Analysis',
    page_icon='🏐',
    layout='centered',
)

# st.sidebar.markdown("# VNL 2023 Data Analysis")

st.image('logo.jpg', use_container_width=True)
st.title("🏐 VNL 2023 – Men's Volleyball Player Statistics")
st.divider()

st.markdown('''
    This dataset contains detailed statistics of male volleyball players who participated in the **2023 FIVB Volleyball Nations League (VNL)**. It includes individual performance metrics across core volleyball skills such as attacking, blocking, serving, and more.
''')

st.markdown(
    '''
    ## 📁 Dataset Overview

    - **Lines**: 131   
    - **Columns**: 10  
    - **Source**: [Kaggle - VNL Men 2023](https://www.kaggle.com/datasets/yeganehbavafa/vnl-men-2023)

    ## 📊 Features

    | Column     | Description |
    |------------|-------------|
    | `Player`   | Full name of the volleyball player |
    | `Country`  | Country the player represents |
    | `Age`      | Player's age during the tournament |
    | `Attack`   | Average attack score |
    | `Block`    | Average block score |
    | `Serve`    | Average serve score |
    | `Set`      | Average set contribution |
    | `Dig`      | Average dig performance |
    | `Receive`  | Average receive performance |
    | `Position` | Player's position |

    ### Position Codes:
    - **OH**: Outside Hitter
    - **OP**: Opposite
    - **MB**: Middle Blocker
    - **S**: Setter
    - **L**: Libero

    ## 🎯 Use Cases

    - **Performance Comparison**: Compare players by skill or position.
    - **Team Analysis**: Evaluate which countries had the strongest individual contributions.
    - **Data Visualization**: Build dashboards or charts to highlight trends in performance.
    - **Sports Analytics Projects**: Great for machine learning or data science practice in sports.

    ## 👥 Target Audience

    - Sports analysts and coaches
    - Data science students and professionals
    - Volleyball fans and fantasy league players

    ---

    > 📌 *This dataset provides a great foundation for exploratory data analysis (EDA), predictive modeling, and visual storytelling in the context of international volleyball competitions.*
'''
)






