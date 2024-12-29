# Trendify

Trendify is a web application that aggregates trending topics from various platforms, including Google Trends, Reddit, and YouTube, and categorizes them for user convenience. By leveraging the power of ChatGPT, Trendify provides intelligent categorization of fetched trends into relevant categories like Entertainment, Sports, Technology, and more.

## Tech Stack

### Frontend
- **React.js**: For building the user interface.
- **CSS**: For styling components.

### Backend
- **Flask**: For serving the backend and API endpoints.
- **Python**: Core backend logic and integration with external APIs.

### API Integration
- **OpenAI**: Used to categorize fetched data into meaningful categories.

### Other Tools
- **Axios**: For making API requests.
- **NPM**: For managing frontend dependencies and building the frontend.

---

## Features
- Fetches trends from Google, Reddit, and YouTube.
- Categorizes data into predefined categories using ChatGPT.
- Displays trends with relevant metadata like search volume, upvotes, or views.

---

## Installation and Running the Project

### Prerequisites
- Node.js and npm installed (for frontend).
- Python installed (preferably version 3.8 or higher).
- OpenAI API key.

### Steps to Run the Project Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Shikhararora19/Trendify.git
   cd Trendify
   ```

2. **Set Up Environment Variables**
   - Create a `.env` file in the `backend` directory.
   - Add your OpenAI API key:
     ```
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

## Usage
- **Select Location**: Choose the region to fetch trends from.
- **Filter by Category**: Filter the trends by predefined categories.
- **Explore Trends**: Click on individual trends to view more details.

---


## License
This project is licensed under the Apache 2.0 License. See the LICENSE file for details.
