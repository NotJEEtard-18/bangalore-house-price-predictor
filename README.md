# 🏠 Bangalore House Price Predictor

A powerful and interactive Streamlit web app that predicts housing prices in Bangalore using a Machine Learning model.  
It’s clean, beautiful, and gives instant estimates based on area, BHK, bathrooms, and location — with visualizations included.

> 🔗 **Live Demo:** [Click here to try the app](https://bangalore-house-price-predictor-notjeetard18.streamlit.app/)

---

## 📌 Features

- 📏 **Input:** Area (sqft), BHK, Bathrooms, Location
- 🤖 **Model:** Trained Linear Regression on real Bengaluru housing data
- 📈 **Visualization:** Interactive pie chart showing BHK distribution
- ⚡ **Real-time Prediction:** Instant estimated price output
- ✅ Easy-to-use interface for any user — no technical knowledge required!

---

## 🧠 How It Works

- The app uses a **pre-trained Linear Regression model**
- Locations are one-hot encoded
- User input is converted into model input format
- Prediction is shown in real-time along with an animation

---

## 📊 Dataset

- **Source:** Kaggle – [Bengaluru House Data](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)
- **Features used:**
  - Total Square Feet
  - Number of Bathrooms
  - BHK (Bedrooms)
  - Location
- **Target:** Price (in Lakhs)

---

## 🚀 Tech Stack

| Tool        | Description                    |
|-------------|--------------------------------|
| Python      | Programming language           |
| Streamlit   | Web app frontend               |
| scikit-learn| Model training (Linear Regression) |
| pandas, numpy | Data preprocessing           |
| Plotly      | Beautiful BHK distribution chart |

---

### 📂 Folder Structure

```
├── app.py                              # Streamlit application
├── Data/
│   └── Bengaluru_House_Data.csv        # Original housing dataset
├── bangalore_home_prices_model.pickle  # Trained ML model
├── columns.json                        # Stores all features for model input
├── requirements.txt                    # For deployment
```

---

## 👨‍💻 Author

Made by **Shubham Kumar Jha**  
📧 [shubham.kr.jha.2005@gmail.com]  
🔗 [LinkedIn](https://www.linkedin.com/in/shubham-kumar-jha-3b0a13366/)  
🐱 [GitHub](https://github.com/notjeetard18)

---

## 📦 Setup Locally (Optional)

```bash
git clone https://github.com/notjeetard18/bangalore-price-predictor.git
cd bangalore-price-predictor
pip install -r requirements.txt
streamlit run app.py


