# TalentInsightAI - User Guide

## 🎯 Quick Start Guide

### Accessing the Application
1. Open your browser
2. Navigate to: `http://127.0.0.1:5000`
3. You'll see the modern dashboard with gradient background

---

## 📚 Feature Guide

### 1. Uploading Resumes

**Step-by-Step:**
1. Scroll to the "Upload Resumes" section (or click "Upload" in navigation)
2. Click the dashed box or drag PDF files onto it
3. Select one or multiple PDF resume files
4. Review the selected files list
5. Click "Upload and Analyze Resumes"
6. Watch the progress bar as files upload
7. See success notification when complete

**Tips:**
- Only PDF files are accepted
- You can upload multiple files at once
- Maximum 50MB per file recommended
- Files are stored securely in the uploads folder

---

### 2. Searching for Skills

**Step-by-Step:**
1. On the homepage, find the "Search by Skills" input box
2. Enter a skill (e.g., "Python", "React", "AWS", "Machine Learning")
3. Click the "Search Candidates" button
4. View the list of matching resumes
5. Click "View Resume" to open the PDF
6. Click "Analyze" to see AI analysis

**Search Tips:**
- Be specific with skill names
- Try variations (e.g., "JavaScript" vs "JS")
- Use programming languages, frameworks, tools
- Case-insensitive search

**Common Skills to Try:**
- Programming: Python, Java, JavaScript, C++, C#
- Web: React, Angular, Vue, Node.js, Django
- Data: SQL, MongoDB, PostgreSQL, Redis
- Cloud: AWS, Azure, Google Cloud, Docker
- Mobile: Android, iOS, React Native, Flutter

---

### 3. Analyzing Resumes

**What You'll See:**
1. **Entity Bar Chart**: Shows distribution of different entity types
2. **Entity Types**:
   - **PERSON**: Candidate names, references
   - **ORG**: Companies, organizations worked at
   - **DATE**: Employment dates, education dates
   - **GPE**: Locations, cities, countries
   - **Other entities**: Skills, technologies, etc.

**How to Analyze:**
1. After searching, click "Analyze" on any resume
2. OR navigate to Profile Screening from the menu
3. View the visual breakdown of resume entities
4. See quick action buttons at the bottom

---

### 4. Getting Top Recommendations

**Step-by-Step:**
1. Click "Top Profiles" in the navigation
2. Select a job category from the dropdown
3. Click "Get Recommendations"
4. View the top 5-6 recommended candidates
5. See match scores for each candidate
6. Click "View Resume" to open PDFs

**Categories Available:**
The categories are auto-populated from your resume database. Common categories include:
- Software Developer
- Data Scientist
- Web Developer
- Full Stack Engineer
- DevOps Engineer
- UI/UX Designer
- Project Manager
- Business Analyst

**Understanding Match Scores:**
- **95-100%**: Excellent match
- **90-94%**: Very good match
- **85-89%**: Good match
- Lower scores indicate less similarity to the category

---

## 🎨 Understanding the Interface

### Homepage Features

**Hero Section:**
- Animated gradient background
- Key statistics (10K+ resumes, 98% accuracy)
- Search functionality front and center

**Upload Section:**
- Clean, professional design
- Drag-and-drop or click to browse
- File preview before upload
- Progress tracking

**Features Section:**
- Six key features explained
- Color-coded cards
- Icons for visual clarity

### Navigation Bar
- **Home**: Return to dashboard
- **Profile Screening**: View analysis results
- **Top Profiles**: Access recommendations
- **Upload**: Quick link to upload section

### Interactive Elements

**Buttons:**
- Primary (gradient): Main actions
- Secondary: Alternative actions
- Hover effects: Visual feedback

**Cards:**
- Lift on hover
- Shadow effects
- Responsive sizing

**Forms:**
- Large, easy-to-use inputs
- Clear labels
- Focus states for accessibility

---

## 🔍 Troubleshooting

### Upload Not Working?
- ✅ Check file is PDF format
- ✅ Ensure file size under 50MB
- ✅ Try refreshing the page
- ✅ Check browser console for errors

### Search Returns No Results?
- ✅ Try different keywords
- ✅ Check spelling
- ✅ Upload more resumes first
- ✅ Use common skill names

### Analysis Page Blank?
- ✅ Ensure visualization images exist
- ✅ Check uploads folder has PDFs
- ✅ Refresh the page
- ✅ Try analyzing a different resume

### Recommendations Not Showing?
- ✅ Select a valid category
- ✅ Ensure data_dict.pkl exists
- ✅ Check similarity.pkl file
- ✅ Upload resumes for that category

---

## 💡 Best Practices

### For Best Results:

1. **Upload Quality Resumes**
   - Well-formatted PDFs
   - Clear text (not scanned images)
   - Standard resume format

2. **Use Specific Search Terms**
   - Technical skills work best
   - Full technology names (not abbreviations)
   - Try multiple related terms

3. **Regular Updates**
   - Upload new resumes regularly
   - Keep the database fresh
   - Remove outdated resumes

4. **Organize by Category**
   - Group similar roles
   - Use consistent naming
   - Tag appropriately

---

## 📱 Mobile Usage

The application is fully responsive:

- **Mobile Phones**: Vertical layout, touch-friendly
- **Tablets**: Optimized card layouts
- **Desktop**: Full feature display

**Mobile Tips:**
- Use the hamburger menu (≡) for navigation
- Tap and hold to drag files
- Pinch to zoom on visualizations

---

## 🎯 Common Use Cases

### Scenario 1: Finding Python Developers
1. Go to homepage
2. Enter "Python" in skill search
3. Review list of candidates
4. Analyze top candidates
5. View their full resumes

### Scenario 2: Hiring for Specific Role
1. Navigate to "Top Profiles"
2. Select job category (e.g., "Data Scientist")
3. Review top 5 recommendations
4. Check match scores
5. Download/view selected resumes

### Scenario 3: Bulk Resume Processing
1. Collect all resumes in one folder
2. Go to Upload section
3. Select all PDFs at once
4. Wait for upload completion
5. Search and analyze as needed

---

## ⚡ Keyboard Shortcuts

- **Ctrl + F**: Focus on search
- **Esc**: Close modals/dropdowns
- **Enter**: Submit forms
- **Tab**: Navigate between fields

---

## 🔒 Privacy & Security

- All resumes stored locally
- No data sent to external servers
- Secure file handling
- No personal data logging

---

## 📊 Understanding Results

### Entity Types Explained:

- **PERSON**: Names, candidates, references
- **ORG**: Microsoft, Google, IBM (companies)
- **GPE**: Dubai, USA, London (places)
- **DATE**: 2020-2023, Jan 2022 (dates)
- **WORK_OF_ART**: Project names, publications
- **PRODUCT**: Technologies, software
- **EVENT**: Conferences, events attended

### Match Scores:

Based on:
- Skill overlap
- Experience similarity
- Category relevance
- Content analysis

---

## 💬 Tips for Recruiters

1. **Build Your Database First**
   - Upload at least 20-30 resumes
   - Diverse skill sets
   - Various experience levels

2. **Use Multiple Search Terms**
   - Primary skills
   - Alternative terms
   - Related technologies

3. **Review AI Analysis**
   - Check entity distribution
   - Look for key organizations
   - Verify experience dates

4. **Trust the Recommendations**
   - 98% accuracy rate
   - ML-powered matching
   - Similarity-based ranking

---

## 🎓 Learning the System

**Estimated Learning Time:**
- Basic usage: 5 minutes
- Advanced features: 15 minutes
- Mastery: 1 hour of practice

**Practice Exercises:**
1. Upload 5 sample resumes
2. Search for 3 different skills
3. Analyze 2 candidates
4. Get recommendations for 1 category

---

## 📞 Need Help?

**Check:**
1. This user guide
2. Project documentation
3. Code comments
4. Console error messages

**Common Questions:**
- "Why no results?" → Upload more resumes first
- "Upload fails?" → Check file format (PDF only)
- "Slow performance?" → Reduce file sizes
- "Analysis error?" → Refresh and try again

---

**Enjoy using TalentInsightAI! 🚀**

*Your AI-Powered Recruitment Assistant*
