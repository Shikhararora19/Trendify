# 🌟 Trendify

![React](https://img.shields.io/badge/Frontend-React-blue?style=for-the-badge&logo=react)
![Flask](https://img.shields.io/badge/Backend-Flask-orange?style=for-the-badge&logo=flask)
![Selenium](https://img.shields.io/badge/Web%20Scraping-Selenium-green?style=for-the-badge&logo=selenium)
![OpenAI](https://img.shields.io/badge/AI-OpenAI-red?style=for-the-badge&logo=openai)
![Python](https://img.shields.io/badge/Language-Python-brightgreen?style=for-the-badge&logo=python)
![NPM](https://img.shields.io/badge/Package%20Manager-NPM-yellow?style=for-the-badge&logo=npm)

**Trendify** is an innovative full-stack web application that keeps you updated with the latest trending topics from platforms like **Google Trends**, **Reddit**, and **YouTube**. Leveraging the power of **ChatGPT**, Trendify categorizes trends into intuitive categories like **Entertainment**, **Sports**, **Technology**, and more, ensuring that you never miss out on what's hot in the world!

---

## 🚀 **Features**

- **Multi-Platform Scraping**: Fetches trending data from Google Trends, Reddit, and YouTube.
- **Intelligent Categorization**: Uses **OpenAI's ChatGPT** to organize trends into meaningful categories.
- **Detailed Insights**: Displays relevant metadata like search volume, upvotes, or views for each trend.
- **Filter & Explore**: Filter trends by categories and explore individual details seamlessly.

---

## 🛠️ **Tech Stack**

### **Frontend**
- ![React](https://img.shields.io/badge/React.js-blue?style=flat-square&logo=react) **React.js**: For building the dynamic user interface.
- **CSS**: For responsive and elegant styling.

### **Backend**
- ![Flask](https://img.shields.io/badge/Flask-orange?style=flat-square&logo=flask) **Flask**: Manages backend logic and API endpoints.
- ![Python](https://img.shields.io/badge/Python-brightgreen?style=flat-square&logo=python) **Python**: For seamless integration with external APIs and data processing.

### **API Integration**
- ![OpenAI](https://img.shields.io/badge/OpenAI-red?style=flat-square&logo=openai) **OpenAI API**: Powers the intelligent categorization of trends.

### **Web Scraping**
- ![Selenium](https://img.shields.io/badge/Selenium-green?style=flat-square&logo=selenium) **Selenium**: Automates browser interactions to scrape dynamic content.

### **Other Tools**
- **Axios**: For API requests.
- **NPM**: Dependency management for the frontend.

---

## 📦 **Installation and Running the Project**

### **Prerequisites**
- **Node.js** and **npm** installed (for the frontend).
- **Python** (preferably version 3.8 or higher).
- **OpenAI API key** for AI-powered features.

### **Steps to Run the Project Locally**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Shikhararora19/Trendify.git
   cd Trendify
   ```

2. **Set Up Environment Variables**
   - Create a `.env` file in the `backend` directory.
   - Add your OpenAI API key:
     ```env
     OPENAI_API_KEY=your_api_key_here
     ```

3. **Install Dependencies**

   **For Backend**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

   **For Frontend**:
   ```bash
   cd ../frontend
   npm install
   ```

4. **Build the Frontend**
   ```bash
   npm run build
   ```

5. **Run the Backend**
   - Navigate to the `backend` directory:
     ```bash
     cd ../backend
     ```
   - Start the backend server:
     ```bash
     python run.py
     ```

6. **Access the Application**
   - Open your browser and navigate to `http://localhost:5001`.

---

## 🌟 **Usage**

1. **Select Location**: Choose the region to scrape trends from.
2. **Filter by Category**: Filter the trends by predefined categories like Entertainment, Technology, etc.
3. **Explore Trends**: Click on individual trends to view detailed metadata and insights.

---

## ✨ **Future Enhancements**

- 🌍 **Global Trend Coverage**: Expand to more platforms and regions.
- 📊 **Advanced Analytics**: Introduce visualizations for trends over time.
- 🚀 **Cloud Deployment**: Host the application on platforms like **AWS**, **Heroku**, or **Vercel**.
- 🔒 **User Authentication**: Add login functionality for saving and customizing user preferences.

---

## 🛡️ **License**

This project is licensed under the **Apache 2.0 License**. See the LICENSE file for details.

---

## 🙌 **Acknowledgments**

- **OpenAI** for their robust AI API.
- **Selenium** for enabling efficient web scraping.
- **React.js** and **Flask** for making full-stack development seamless.

---

## 📬 **Contact**

For questions or feedback, feel free to reach out:
- GitHub: [@Shikhararora19](https://github.com/Shikhararora19)
- Email: [shikhar3@ualberta.ca](mailto:shikhar3@ualberta.ca)
