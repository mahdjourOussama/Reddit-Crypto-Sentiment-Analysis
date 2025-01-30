# 🚀 Sentiment Analysis on Crypto Subreddits

## 📌 Project Overview
This project demonstrates how to build a **data pipeline** to fetch, clean, and analyze sentiment from **Reddit posts**. The focus is on integrating a robust **data pipeline** rather than the AI models used for sentiment analysis.

For this proof-of-concept, we analyzed the **cryptocurrency subreddit**, aiming to understand how market sentiment correlates with price fluctuations. By examining discussions, we can gain insights into how the market might react to different coins.

This project was developed as part of the **Octo-Hackathon** for DataScale students.

## 🎯 Objectives
- Build an **end-to-end data pipeline** to extract and process Reddit data.
- Apply **basic sentiment analysis algorithms** to measure sentiment trends.
- **Visualize insights** on how sentiment correlates with cryptocurrency market fluctuations.
- Lay the groundwork for future improvements, such as **more advanced models and deployment with Docker**.

## 🏗️ Project Structure
```
📂 project_root
 ├── 📂 database/                 # Stores cleaned and preprocessed data
 ├── 📂 sentiments/               # Contains CSV files with sentiment analysis results
 ├── 📂 plots/                    # Saves generated visualizations
 ├── 📜 app.py                    # Streamlit-based interactive dashboard
 ├── 📜 data_preprocessing.py      # Module for data cleaning and preprocessing
 ├── 📜 data_visualization.py      # Functions for data visualization
 ├── 📜 sentiments_analysis.py     # Module for performing sentiment analysis
```

## 🛠️ Technologies Used
- **Python** – Core programming language
- **PRAW** – Reddit API for data fetching
- **NLTK / TextBlob** – Sentiment analysis tools
- **Pandas / NumPy** – Data processing
- **Matplotlib / Seaborn** – Data visualization
- **Streamlit** – Interactive UI for sentiment analysis results

## 🚀 Installation & Usage
1. **Clone the repository**
   ```bash
   git clone https://github.com/mahdjourOussama/Reddit-Crypto-Sentiment-Analysis.git
   cd Reddit-Crypto-Sentiment-Analysis
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

## 📊 Future Enhancements
- Expand to **more general topics** beyond cryptocurrency.
- Improve **sentiment analysis models** with more advanced NLP techniques.
- Prepare for **deployment using Docker**.

## 🤝 Contributions
Contributions are welcome! Feel free to fork the repo and submit a PR.

---
📧 **Contact:** If you have any questions, reach out via [LinkedIn](https://www.linkedin.com/in/oussamamahdjour/) or email.

🌟 **Star this repository** if you found it useful!
