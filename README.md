# 🎯 Resume Analyzer - AI-Powered Recruitment Tool

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.2-green.svg)](https://flask.palletsprojects.com/)
[![spaCy](https://img.shields.io/badge/spaCy-3.6.0-09a3d5.svg)](https://spacy.io/)
[![Deploy on Railway](https://img.shields.io/badge/Deploy-Railway-blueviolet.svg)](https://railway.app/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> AI-powered resume analysis system with NLP, entity extraction, skills assessment, and candidate recommendations using machine learning.

## 🌟 Features

### 📄 Resume Analysis
- **PDF Processing**: Extract and analyze text from PDF resumes
- **Entity Extraction**: Identify names, organizations, locations, and dates using spaCy NLP
- **Skills Assessment**: Detect 25+ technical skills (Python, JavaScript, AWS, Docker, etc.)
- **Soft Skills Analysis**: Evaluate communication, leadership, teamwork, and more

### 📊 Visual Analytics
- **4-Chart Dashboard**: Comprehensive visualization of resume metrics
  - Resume statistics overview
  - Technical skills distribution
  - Soft skills radar chart
  - Resume sections breakdown
- **Interactive Filtering**: Search and filter candidates by skills
- **Entity Display**: Color-coded badges for persons, organizations, dates, and locations

### 🤖 AI-Powered Recommendations
- **Cosine Similarity**: ML-based candidate matching using pre-trained 870-resume dataset
- **Top Profiles**: Intelligent recommendations based on job requirements
- **Similarity Scores**: Percentage-based matching for quick decision making

### 💼 Bulk Processing
- **Multi-Resume Upload**: Process multiple PDFs simultaneously
- **Progress Tracking**: Real-time upload progress with AJAX
- **Batch Analysis**: Analyze entire candidate pools efficiently

### 📱 Modern UI
- **Tailwind CSS**: Clean, responsive design optimized for UAE tech market
- **Mobile Responsive**: Works perfectly on desktop, tablet, and mobile
- **Glassmorphism**: Modern gradient animations and professional aesthetics
- **Toast Notifications**: Real-time feedback for user actions

## 🛠️ Tech Stack

### Backend
- **Flask 2.3.2** - Python web framework
- **spaCy 3.6.0** - Natural Language Processing
- **pandas 2.0.3** - Data manipulation and analysis
- **PyPDF2 3.0.1** - PDF text extraction
- **Gunicorn 21.2.0** - Production WSGI server

### Frontend
- **Tailwind CSS 3.x** - Utility-first CSS framework
- **Alpine.js** - Lightweight JavaScript framework
- **Font Awesome 6** - Icon library
- **Google Fonts (Inter)** - Professional typography

### Machine Learning
- **Pre-trained Models**: 870-resume similarity matrix
- **Cosine Similarity**: Vector-based candidate matching
- **Entity Recognition**: spaCy's en_core_web_sm model
- **Regex Fallbacks**: Robust extraction when NLP unavailable

### Visualization
- **matplotlib 3.7.2** - Statistical charts and graphs
- **Agg Backend** - Non-GUI rendering for server deployment

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/resume-analyzer.git
cd resume-analyzer
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

4. **Run the application**
```bash
python app.py
```

5. **Open browser**
```
http://localhost:5000
```

### Production Deployment

#### Deploy to Railway (FREE - Recommended)

1. **Push to GitHub**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Deploy to Railway**
   - Go to [railway.app](https://railway.app/)
   - Login with GitHub
   - Click "Deploy from GitHub repo"
   - Select your repository
   - Click "Deploy"

3. **Get your URL**
   - Settings → Networking → Generate Domain
   - Your app: `https://your-app.up.railway.app`

📖 **Detailed guide**: See [DEPLOY_RAILWAY.md](DEPLOY_RAILWAY.md)

## 📁 Project Structure

```
resume-analyzer/
├── app.py                      # Main Flask application
├── my_analysis.py              # Resume analysis & visualization
├── pdf_search.py               # PDF text extraction & search
├── wsgi.py                     # Production WSGI entry point
├── requirements.txt            # Python dependencies
├── data_dict.pkl               # Pre-processed resume dataset (870 resumes)
├── similarity.pkl              # Cosine similarity matrix (870x870)
│
├── templates/                  # HTML templates
│   ├── dashboard.html          # Main landing page
│   ├── index.html              # Top profiles view
│   ├── profile_screening.html  # Detailed analysis view
│   ├── skills_assessment.html  # Skills breakdown
│   └── ...
│
├── static/                     # Static assets
│   ├── css/                    # Stylesheets
│   ├── js/                     # JavaScript files
│   ├── images/                 # Image assets
│   └── fonts/                  # Custom fonts
│
├── uploads/                    # Uploaded PDF storage
│
└── deployment/                 # Deployment configurations
    ├── railway.json            # Railway config
    ├── Procfile                # Process file
    ├── nixpacks.toml           # Build configuration
    └── DEPLOY_RAILWAY.md       # Deployment guide
```

## 🎯 Use Cases

### For Recruiters
- Screen hundreds of resumes in minutes
- Identify top candidates using AI matching
- Filter candidates by specific skills
- Export analysis for hiring decisions

### For HR Departments
- Standardize resume evaluation process
- Reduce unconscious bias with data-driven insights
- Track candidate pipelines
- Generate hiring reports

### For Job Seekers
- Analyze your own resume
- Identify missing keywords
- Optimize for ATS systems
- Compare against industry standards

## 📊 Analysis Capabilities

### Extracted Entities
- **PERSON**: Candidate names, references
- **ORG**: Companies, universities, organizations
- **DATE**: Work periods, graduation dates, certifications
- **GPE**: Locations, cities, countries

### Technical Skills Detected
Python, JavaScript, Java, C++, React, Angular, Vue.js, Node.js, Django, Flask, Docker, Kubernetes, AWS, Azure, GCP, SQL, MongoDB, PostgreSQL, Machine Learning, Data Science, DevOps, Git, CI/CD, Agile, Scrum

### Soft Skills Evaluated
Communication, Leadership, Teamwork, Problem Solving, Time Management, Adaptability, Creativity, Critical Thinking, Emotional Intelligence

## 🔧 Configuration

### Environment Variables (Production)
```bash
PORT=8000                    # Server port (Railway sets automatically)
FLASK_ENV=production         # Production mode
```

### Local Development
```bash
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=1
```

## 📈 Performance

- **Processing Speed**: ~2-3 seconds per resume
- **Bulk Upload**: 10+ resumes simultaneously
- **Memory Usage**: ~800MB with ML models loaded
- **Storage**: 50GB+ recommended for large resume databases

## 🛡️ Security

- **File Validation**: Only PDF files allowed
- **Secure Filenames**: Sanitized using werkzeug
- **No SQL Injection**: Uses pandas/pickle for data storage
- **Input Validation**: All user inputs validated
- **HTTPS**: Enabled by default on Railway

## 🐛 Known Issues & Solutions

### Python 3.14 Compatibility
- **Issue**: spaCy 3.6.0 not compatible with Python 3.14
- **Solution**: Use Python 3.11 (configured in `runtime.txt`)

### Chart Rendering
- **Issue**: Matplotlib GUI backend fails on servers
- **Solution**: Uses 'Agg' backend for headless rendering

### Entity Extraction
- **Issue**: spaCy may fail on some systems
- **Solution**: Regex fallback patterns implemented

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- [spaCy](https://spacy.io/) for NLP capabilities
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Tailwind CSS](https://tailwindcss.com/) for the UI design
- [Railway](https://railway.app/) for free hosting

## 📞 Support

For issues and questions:
- 📧 Email: your.email@example.com
- 💬 GitHub Issues: [Create an issue](https://github.com/yourusername/resume-analyzer/issues)
- 📖 Documentation: [Full Docs](DEPLOY_RAILWAY.md)

---

**⭐ Star this repo if you find it helpful!**

**🚀 Deploy your own**: [Get Started](DEPLOY_RAILWAY.md)