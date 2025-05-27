This is a GenAI-powered application that lets users interact with both unstructured documents and structured databases using simple natural language. Built using LangChain, Streamlit, FAISS, and Gemini Flash 1.5, the app delivers fast, accurate answers whether you're querying a PDF or an SQL database.

🚀 Features
📄 PDF Ingestion – Upload PDF files and ask questions about them using an LLM-powered interface.

🧠 LLM Q&A – Integrates Gemini Flash 1.5 via LangChain for fast and efficient responses.

📊 SQL Database Querying – Convert natural language questions into SQL queries and run them against your database.

🗂️ FAISS Vector Store – Enables fast semantic search across embedded PDF chunks.

🎛️ Streamlit UI – Clean and intuitive frontend built with Streamlit.

🛠️ Tech Stack
Frontend: Streamlit

LLM: Gemini Flash 1.5 via LangChain

Embeddings: Google's embedding models or OpenAI embeddings

Database Support: SQLite / PostgreSQL / MySQL

Vector Store: FAISS

Python Libraries: LangChain, pandas, SQLAlchemy, dotenv, etc.

📁 Project Structure
bash
Copy code
.
├── app.py                  # Main Streamlit application
├── requirements.txt        # List of dependencies
├── db/                     # SQL database files
├── data/                   # PDF documents or sample input files
├── utils/                  # Helper functions
│   ├── pdf_loader.py
│   ├── sql_handler.py
│   └── llm_query.py
└── README.md
⚙️ Installation
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/text-to-llm-app.git
cd text-to-llm-app
2. Set Up a Virtual Environment
bash
Copy code
python -m venv venv
# Activate it
source venv/bin/activate         # For macOS/Linux
venv\Scripts\activate            # For Windows
3. Install the Dependencies
bash
Copy code
pip install -r requirements.txt
🔧 Configuration
Create a .env file in your project root and add your Gemini API key:

ini
Copy code
GEMINI_API_KEY=your_gemini_flash_key
Optionally, configure your database connection:

ini
Copy code
DATABASE_URL=sqlite:///db/mydata.db
▶️ Running the App
Launch the application using Streamlit:

bash
Copy code
streamlit run app.py
🧠 How It Works
PDF Q&A: The app loads your PDF, splits it into manageable chunks, generates embeddings, and stores them in FAISS for semantic search.

SQL Querying: For structured data, your natural language questions are converted into SQL using Gemini Flash 1.5 and executed on your configured database.

Answers Displayed Instantly: The results—whether from PDFs or databases—are shown in a simple Streamlit interface.

📌 Use Cases
Business analytics and report summarization

Academic research over PDFs

Conversational access to structured company databases

Personal document assistant with SQL log access

🔒 Security Considerations
This project is intended for learning and demo purposes. For production use:

Add authentication and user access control

Secure your API keys and database connections

Implement rate limiting and logging

🤝 Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue if you have suggestions or improvements.

