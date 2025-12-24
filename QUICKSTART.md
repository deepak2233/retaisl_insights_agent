# 🚀 Quick Start Guide

## Get Started in 5 Minutes

### Step 1: Install Dependencies (2 min)
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### Step 2: Configure API Key (1 min)
```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your API key
# For OpenAI: OPENAI_API_KEY=sk-your-key-here
# For Gemini: GOOGLE_API_KEY=your-key-here
```

### Step 3: Generate Data (1 min)
```bash
python data/generate_data.py
```

### Step 4: Run Application (1 min)
```bash
streamlit run app.py
```

**Done! 🎉** Open http://localhost:8501

---

## 🎯 First Steps

1. **Click "Initialize System"** in sidebar
2. **Try example questions**:
   - "What were total sales in 2023?"
   - "Which region performed best?"
3. **Generate summary** in Summary Mode tab
4. **Explore data** in Data Explorer tab

---

## 🐳 Docker Quick Start

```bash
# Build and run with Docker
docker-compose up -d

# Access at http://localhost:8501
```

---

## 📚 Documentation

- **README.md**: Complete documentation
- **docs/SETUP_GUIDE.md**: Detailed setup instructions
- **docs/SCALABILITY.md**: Architecture for 100GB+ data
- **docs/PRESENTATION_OUTLINE.md**: Technical presentation
- **docs/TEST_RESULTS.md**: Testing documentation

---

## 🆘 Common Issues

**"Module not found"**
```bash
pip install -r requirements.txt
```

**"API key not found"**
- Check `.env` file exists and has your key
- Restart Streamlit app

**"File not found"**
```bash
python data/generate_data.py
```

---

## 💡 Example Questions

- "What were total sales in Q3 2023?"
- "Which category saw highest YoY growth?"
- "Top 5 products by profit?"
- "Compare Online vs In-Store channels"
- "Show monthly trend for Electronics"
- "Which region underperformed in 2022?"

---

## 🎓 What's Included

✅ **4 Specialized Agents** (Query, Extraction, Validation, Response)  
✅ **Multi-Agent Orchestration** (LangGraph)  
✅ **LLM Integration** (OpenAI GPT-4 / Google Gemini)  
✅ **Efficient Database** (DuckDB for OLAP)  
✅ **Interactive UI** (Streamlit)  
✅ **Sample Data** (50K transactions)  
✅ **Complete Documentation**  
✅ **Scalability Design** (100GB+ architecture)  

---

**Ready to deploy?** See docs/SETUP_GUIDE.md for production deployment.
