# 🏐 VNL 2023 – Men's Volleyball Player Statistics App
🔗 **Live App:** https://vnlanalysis.streamlit.app/  
---
This Streamlit application provides interactive analysis and visualizations for the **2023 FIVB Volleyball Nations League (VNL)** men's statistics. It leverages real performance data of international volleyball players and allows filtering, ranking, and graphical exploration of key performance indicators such as attack, block, serve, dig, receive, and more.

## Demo
<img width="1854" height="819" alt="image" src="https://github.com/user-attachments/assets/8fbe6169-c30c-4ac8-bf98-2f5f744078cf" />
<img width="1843" height="825" alt="image" src="https://github.com/user-attachments/assets/c1ce8555-fb85-4399-b1f0-ac17a445e939" />
<img width="1843" height="822" alt="image" src="https://github.com/user-attachments/assets/14e9fd21-3558-4cde-a47e-ef6f106aa17a" />
<img width="1837" height="837" alt="image" src="https://github.com/user-attachments/assets/7d80bc06-d5c7-491e-913e-56cd565a9bcb" />

## 📂 Project Structure

- `Home.py` – Project introduction, dataset explanation, and general information.
- `📊Statics.py` – Statistical highlights including the best players in each skill.
- `📈Graphs.py` – Graphical visualizations like bar charts, boxplots, scatter plots, and pie charts.
- `🔎Filter.py` – Filter the dataset by country, position, or specific player name.
- `VNL2023.csv` – Dataset source containing player statistics.
- `logo.jpg` – Logo used on the home page.

---

## 📊 Dataset Overview

- **Rows**: 131  
- **Columns**: 10  
- **Source**: [Kaggle - VNL Men 2023](https://www.kaggle.com/datasets/yeganehbavafa/vnl-men-2023)

### Columns

| Column     | Description |
|------------|-------------|
| `Player`   | Player name |
| `Country`  | Country represented |
| `Age`      | Age of the player |
| `Attack`   | Average attack score |
| `Block`    | Average block score |
| `Serve`    | Average serve score |
| `Set`      | Average set contribution |
| `Dig`      | Average dig performance |
| `Receive`  | Average receive performance |
| `Position` | Player's position on the court |

### Position Codes:
- **OH** – Outside Hitter  
- **OP** – Opposite  
- **MB** – Middle Blocker  
- **S** – Setter  
- **L** – Libero  

---

## 🚀 Features

### 📊 Statistics Page
- Number of players by position
- Countries represented
- Best individual performance in each skill category

### 📈 Graphs Page
- Top 10 attackers by position
- Attack score distribution by position (boxplot)
- Age vs. Attack score by position (scatterplot)
- Position distribution (pie chart)

### 🔎 Filter Page
- Filter dataset by country and/or position
- View specific player statistics

---

## 🛠️ Tech Stack

- **Python 3**
- **Streamlit**
- **Pandas**
- **Seaborn / Matplotlib / Plotly Express**

---

## 🎯 Use Cases

- Compare players by skills and roles
- Identify top performers in attack, block, serve, etc.
- Analyze team compositions and national differences
- Build dashboards and visual stories for volleyball statistics

---

## 🧑‍💻 How to Run Locally

1. Clone the repository:
   ``` bash
   git clone https://github.com/joaoeferrari/vnl_aplication.git
   cd vnl_aplication
   ```
2. Install dependencies:
   ``` bash
    pip install -r requirements.txt
   ```
3. Run the app:
    ``` bash
      streamlit run Home.py
    ```
