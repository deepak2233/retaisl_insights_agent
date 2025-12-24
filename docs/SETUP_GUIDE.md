# Setup Guide - Retail Insights Assistant

## 📋 Complete Setup Instructions

### Step 1: System Requirements

**Minimum Requirements:**
- Operating System: Windows 10/11, macOS 10.15+, or Linux (Ubuntu 20.04+)
- Python: 3.9 or higher
- RAM: 4GB minimum (8GB recommended)
- Disk Space: 2GB free space
- Internet: Required for LLM API calls

**Check Python Version:**
```bash
python --version  # Should show 3.9 or higher
```

If Python is not installed:
- **Windows**: Download from [python.org](https://www.python.org/downloads/)
- **macOS**: `brew install python@3.9`
- **Linux**: `sudo apt-get install python3.9`

---

### Step 2: Get API Keys

You need **ONE** of the following:

#### Option A: OpenAI (Recommended)

1. Go to [platform.openai.com](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create new API key
5. Copy the key (starts with `sk-...`)

**Cost Estimate**: ~$5-10 for testing this project

#### Option B: Google Gemini

1. Go to [ai.google.dev](https://ai.google.dev/)
2. Sign up for Gemini API
3. Get your API key
4. Copy the key

**Cost Estimate**: Free tier available with generous limits

---

### Step 3: Clone and Setup Project

```bash
# Clone the repository
git clone <your-repo-url>
cd retail-insights-assistant

# Or if you have the zip file
unzip retail-insights-assistant.zip
cd retail-insights-assistant
```

---

### Step 4: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

---

### Step 5: Install Dependencies

```bash
# Upgrade pip first
pip install --upgrade pip

# Install all requirements
pip install -r requirements.txt
```

**If you encounter errors:**

**Error: "No matching distribution found"**
```bash
# Try updating setuptools
pip install --upgrade setuptools wheel
pip install -r requirements.txt
```

**Error: "Microsoft Visual C++ required" (Windows)**
- Install Microsoft C++ Build Tools: https://visualstudio.microsoft.com/visual-cpp-build-tools/

**Error: "command 'gcc' failed" (Linux)**
```bash
sudo apt-get install python3-dev build-essential
pip install -r requirements.txt
```

---

### Step 6: Configure Environment Variables

```bash
# Copy example environment file
cp .env.example .env

# Edit .env file
# Windows: notepad .env
# macOS: open -e .env
# Linux: nano .env
```

**For OpenAI:**
```env
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-your-actual-key-here
OPENAI_MODEL=gpt-4-turbo-preview
```

**For Google Gemini:**
```env
LLM_PROVIDER=google
GOOGLE_API_KEY=your-actual-key-here
GEMINI_MODEL=gemini-pro
```

**Important**: Never commit your `.env` file to git!

---

### Step 7: Generate Sample Data

```bash
# Generate 50,000 sample sales records
python data/generate_data.py
```

**Expected Output:**
```
Generating 50,000 sales records...
  Generated 10,000 records...
  Generated 20,000 records...
  ...
✅ Successfully generated 50,000 records
📁 Saved to: data/sales_data.csv

Dataset Summary:
  Date Range: 2021-01-01 to 2023-12-31
  Total Revenue: $XXX,XXX,XXX.XX
  Total Profit: $XX,XXX,XXX.XX
  ...
```

**Customize Data Size:**
```python
# Edit generate_data.py and change:
generate_sales_data(num_rows=100000)  # For 100K records
```

---

### Step 8: Run the Application

```bash
streamlit run app.py
```

**Expected Output:**
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

The app will automatically open in your default browser.

**If browser doesn't open automatically:**
- Manually navigate to: http://localhost:8501

---

### Step 9: Test the System

#### 9.1 Initialize System

1. In the sidebar, click **"🔄 Initialize System"**
2. Wait for "✅ System initialized successfully!"
3. Verify metrics appear in sidebar

#### 9.2 Try Example Questions

**In the Q&A tab, try:**
- "What were total sales in 2023?"
- "Which region had the highest growth?"
- "Top 5 products by profit?"

#### 9.3 Generate Summary

1. Click **"📊 Summary Mode"** tab
2. Click **"📈 Generate Summary Report"**
3. Wait for comprehensive report

#### 9.4 Explore Data

1. Click **"🔍 Data Explorer"** tab
2. View charts and statistics

---

## 🔧 Troubleshooting

### Issue: "Module not found" errors

**Solution:**
```bash
# Make sure virtual environment is activated
# You should see (venv) in your prompt

# Reinstall dependencies
pip install -r requirements.txt
```

---

### Issue: "API key not found"

**Solution:**
1. Check `.env` file exists in project root
2. Verify API key is correctly set
3. Restart the Streamlit app

```bash
# Test API key manually
python -c "from config import settings; print(settings.openai_api_key)"
```

---

### Issue: "Database error" or "File not found"

**Solution:**
```bash
# Regenerate data
python data/generate_data.py

# Check file exists
ls -l data/sales_data.csv  # macOS/Linux
dir data\sales_data.csv    # Windows
```

---

### Issue: Port 8501 already in use

**Solution:**
```bash
# Use a different port
streamlit run app.py --server.port 8502
```

---

### Issue: Slow response times

**Possible causes:**
1. **Large dataset**: Reduce sample size in `generate_data.py`
2. **LLM API latency**: Normal, first query is always slower
3. **Internet connection**: Check your connection speed

---

### Issue: LLM API errors

**OpenAI errors:**
- `AuthenticationError`: Check API key
- `RateLimitError`: You've exceeded quota, wait or upgrade plan
- `InvalidRequestError`: Check model name

**Gemini errors:**
- `Invalid API key`: Verify key from Google AI Studio
- `Quota exceeded`: Wait for quota reset

---

## 🧪 Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_agents.py -v

# Run with coverage
pip install pytest-cov
pytest tests/ --cov=agents --cov=utils
```

---

## 📊 Monitoring and Logs

### View Application Logs

**Terminal output shows:**
- Agent workflow execution
- SQL queries being run
- Errors and warnings

### Enable Debug Mode

Edit `config.py`:
```python
enable_logging = True
log_level = "DEBUG"
```

---

## 🚀 Production Deployment

### Docker Deployment

```bash
# Build Docker image
docker build -t retail-insights-assistant .

# Run container
docker run -p 8501:8501 \
  -e OPENAI_API_KEY=your-key \
  retail-insights-assistant
```

### Cloud Deployment

**Streamlit Cloud:**
1. Push code to GitHub
2. Connect at share.streamlit.io
3. Add API keys in Streamlit secrets

**AWS:**
```bash
# Deploy to EC2
# 1. Launch EC2 instance (t3.medium)
# 2. SSH and clone repo
# 3. Install dependencies
# 4. Run with nohup
nohup streamlit run app.py &
```

---

## 📝 Best Practices

### 1. API Key Security
- ✅ Use environment variables
- ✅ Never commit `.env` file
- ✅ Rotate keys regularly
- ❌ Don't hardcode keys in code

### 2. Cost Management
- Set OpenAI usage limits in dashboard
- Monitor API costs daily
- Use caching for repeated queries
- Consider GPT-3.5 for simple queries

### 3. Performance
- Keep dataset < 5GB for local testing
- Use query caching
- Pre-compute common aggregations
- Limit conversation history

---

## 🆘 Getting Help

**Common Resources:**
1. **Project README**: [README.md](../README.md)
2. **Architecture Docs**: [docs/SCALABILITY.md](SCALABILITY.md)
3. **LangChain Docs**: https://python.langchain.com/
4. **Streamlit Docs**: https://docs.streamlit.io/
5. **DuckDB Docs**: https://duckdb.org/docs/

**Support Channels:**
- GitHub Issues: Report bugs and feature requests
- Email: support@yourcompany.com
- Documentation: Check `docs/` folder

---

## ✅ Verification Checklist

Before considering setup complete:

- [ ] Python 3.9+ installed and verified
- [ ] Virtual environment created and activated
- [ ] All dependencies installed successfully
- [ ] API key configured in `.env` file
- [ ] Sample data generated (50K records)
- [ ] Streamlit app launches without errors
- [ ] System initializes successfully
- [ ] Example queries return results
- [ ] Summary generation works
- [ ] Data explorer displays charts
- [ ] Tests pass (`pytest tests/`)

---

## 🎓 Next Steps

Once setup is complete:

1. **Experiment with queries**: Try different questions
2. **Explore the code**: Understand the agent system
3. **Customize**: Modify agents for your use case
4. **Scale up**: Generate larger datasets
5. **Deploy**: Put it in production
6. **Extend**: Add new features and agents

---

**Setup Guide Version**: 1.0  
**Last Updated**: December 2024  
**Estimated Setup Time**: 20-30 minutes
