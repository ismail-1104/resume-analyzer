import matplotlib.pyplot as plt
import PyPDF2
import re
from collections import Counter
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

# Try to load spaCy, but handle errors gracefully
try:
    import spacy
    from spacy import displacy
    nlp = spacy.load("en_core_web_sm")
    SPACY_AVAILABLE = True
except Exception as e:
    print(f"Warning: spaCy not available: {e}")
    SPACY_AVAILABLE = False
    nlp = None

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def extract_entities_from_resume(resume_text):
    """Extract named entities from resume text using pattern matching and spaCy if available"""
    entities = {
        'PERSON': [],
        'ORG': [],
        'DATE': [],
        'GPE': []
    }
    
    try:
        # Try spaCy first if available
        if SPACY_AVAILABLE and nlp:
            doc = nlp(resume_text[:10000])  # Limit text length for performance
            for ent in doc.ents:
                if ent.label_ in entities:
                    entities[ent.label_].append(ent.text)
        
        # Fallback to regex patterns
        if not entities['DATE'] or len(entities['DATE']) < 3:
            # Extract dates - various formats
            date_patterns = [
                r'\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{4}\b',
                r'\b\d{1,2}/\d{1,2}/\d{2,4}\b',
                r'\b\d{4}\s*-\s*\d{4}\b',
                r'\b\d{4}\s*to\s*\d{4}\b',
                r'\b\d{4}\s*-\s*(?:Present|Current)\b',
                r'\b(19|20)\d{2}\b'
            ]
            for pattern in date_patterns:
                dates = re.findall(pattern, resume_text, re.IGNORECASE)
                entities['DATE'].extend([d if isinstance(d, str) else d[0] for d in dates])
        
        # Extract organizations (common patterns)
        if not entities['ORG'] or len(entities['ORG']) < 2:
            org_keywords = [
                r'\b(?:Inc\.|LLC|Ltd\.|Corporation|Corp\.|Company|Co\.|Group|Associates|Partners|Consulting|Technologies|Systems|Solutions|Services)\b',
                r'\b[A-Z][a-z]+\s+(?:Inc\.|LLC|Ltd\.|Corporation|Corp\.|Company|Co\.|Group|Associates|Partners|Consulting|Technologies|Systems|Solutions|Services)\b',
                r'\b(?:University of [A-Z][a-z]+|[A-Z][a-z]+\s+University|[A-Z][a-z]+\s+College|[A-Z][a-z]+\s+Institute)\b'
            ]
            for pattern in org_keywords:
                orgs = re.findall(pattern, resume_text)
                entities['ORG'].extend(orgs)
        
        # Extract locations (cities, states, countries)
        if not entities['GPE'] or len(entities['GPE']) < 2:
            # Common location indicators
            location_patterns = [
                r'\b(?:New York|Los Angeles|Chicago|Houston|Phoenix|Philadelphia|San Antonio|San Diego|Dallas|San Jose|Austin|Jacksonville|Fort Worth|Columbus|Charlotte|San Francisco|Indianapolis|Seattle|Denver|Washington|Boston|Nashville|Detroit|Portland|Las Vegas|Memphis|Louisville|Baltimore|Milwaukee|Albuquerque|Tucson|Fresno|Sacramento|Kansas City|Atlanta|Miami|Oakland|Tulsa|Cleveland|Wichita|New Orleans|Dubai|Abu Dhabi|London|Paris|Tokyo|Singapore|Mumbai|Bangalore|Delhi|Sydney|Toronto|Vancouver)\b',
                r'\b(?:CA|NY|TX|FL|IL|PA|OH|MI|GA|NC|NJ|VA|WA|MA|AZ|IN|TN|MO|MD|WI|MN|CO|AL|SC|LA|KY|OR|OK|CT|UT|NV|NM|WV|HI|NH|ME|RI|MT|DE|SD|ND|AK|VT|WY|UAE|UK|USA|India|China|Japan|Germany|France|Canada|Australia)\b',
            ]
            for pattern in location_patterns:
                locations = re.findall(pattern, resume_text)
                entities['GPE'].extend(locations)
        
        # Extract person names (simple pattern - capitalized words)
        if not entities['PERSON'] or len(entities['PERSON']) < 1:
            # Look for name patterns at the beginning of resume
            name_pattern = r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})'
            name_match = re.search(name_pattern, resume_text.strip(), re.MULTILINE)
            if name_match:
                entities['PERSON'].append(name_match.group(1))
            
            # Also look for "Name:" or "Candidate:" patterns
            name_label_patterns = [
                r'(?:Name|Candidate|Applicant):\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})',
            ]
            for pattern in name_label_patterns:
                names = re.findall(pattern, resume_text)
                entities['PERSON'].extend(names)
        
        # Deduplicate and limit results
        for key in entities:
            entities[key] = list(set(entities[key]))[:10]  # Keep unique, max 10 per type
            
    except Exception as e:
        print(f"Error extracting entities: {str(e)}")
    
    return entities

def visualize_resume_from_pdf(pdf_path, output_path="static/images/visualization.png"):
    try:
        # Extract text from PDF
        resume_text = extract_text_from_pdf(pdf_path)
        
        # Basic text analysis
        words = resume_text.lower().split()
        total_words = len(words)
        
        # Common skills keywords
        technical_skills = ['python', 'java', 'javascript', 'react', 'angular', 'node', 'sql', 'aws', 'azure', 
                          'machine learning', 'data science', 'docker', 'kubernetes', 'git', 'api', 'html', 
                          'css', 'mongodb', 'postgresql', 'django', 'flask', 'tensorflow', 'pytorch']
        
        soft_skills = ['leadership', 'communication', 'teamwork', 'problem solving', 'management', 
                      'collaboration', 'analytical', 'creative', 'organized']
        
        # Find skills in resume
        found_technical = [skill for skill in technical_skills if skill in resume_text.lower()]
        found_soft = [skill for skill in soft_skills if skill in resume_text.lower()]
        
        # Extract common patterns
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', resume_text)
        phones = re.findall(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', resume_text)
        years = re.findall(r'\b(19|20)\d{2}\b', resume_text)
        
        # Create comprehensive visualization
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('Comprehensive Resume Analysis', fontsize=20, fontweight='bold')
        
        # Chart 1: Resume Statistics
        stats_labels = ['Total Words', 'Tech Skills', 'Soft Skills', 'Contact Info']
        stats_values = [min(total_words, 1000), len(found_technical), len(found_soft), len(emails) + len(phones)]
        colors1 = ['#3b82f6', '#8b5cf6', '#10b981', '#f59e0b']
        ax1.bar(stats_labels, stats_values, color=colors1, alpha=0.8, edgecolor='black', linewidth=1.5)
        ax1.set_title('Resume Statistics Overview', fontsize=14, fontweight='bold', pad=15)
        ax1.set_ylabel('Count', fontsize=12)
        ax1.grid(axis='y', alpha=0.3, linestyle='--')
        for i, v in enumerate(stats_values):
            ax1.text(i, v + 20, str(v), ha='center', va='bottom', fontweight='bold', fontsize=11)
        
        # Chart 2: Technical Skills Found
        if found_technical:
            tech_display = found_technical[:8] if len(found_technical) > 8 else found_technical
            ax2.barh(tech_display, [1]*len(tech_display), color='#7c3aed', alpha=0.8, edgecolor='black')
            ax2.set_title(f'Technical Skills Detected ({len(found_technical)} total)', fontsize=14, fontweight='bold', pad=15)
            ax2.set_xlabel('Presence', fontsize=12)
            ax2.set_xlim(0, 1.2)
            ax2.grid(axis='x', alpha=0.3, linestyle='--')
        else:
            ax2.text(0.5, 0.5, 'No common technical skills detected', 
                    ha='center', va='center', fontsize=12, transform=ax2.transAxes)
            ax2.set_title('Technical Skills', fontsize=14, fontweight='bold')
        ax2.set_xticks([])
        
        # Chart 3: Soft Skills
        if found_soft:
            ax3.bar(range(len(found_soft)), [1]*len(found_soft), color='#10b981', alpha=0.8, edgecolor='black')
            ax3.set_xticks(range(len(found_soft)))
            ax3.set_xticklabels(found_soft, rotation=45, ha='right', fontsize=10)
            ax3.set_title(f'Soft Skills Detected ({len(found_soft)} total)', fontsize=14, fontweight='bold', pad=15)
            ax3.set_ylabel('Presence', fontsize=12)
            ax3.grid(axis='y', alpha=0.3, linestyle='--')
        else:
            ax3.text(0.5, 0.5, 'No common soft skills detected', 
                    ha='center', va='center', fontsize=12, transform=ax3.transAxes)
            ax3.set_title('Soft Skills', fontsize=14, fontweight='bold')
        ax3.set_yticks([])
        
        # Chart 4: Resume Sections Analysis
        sections = {
            'Experience': len(re.findall(r'\bexperience\b|\bwork\b|\bemployment\b', resume_text, re.I)),
            'Education': len(re.findall(r'\beducation\b|\bdegree\b|\buniversity\b|\bcollege\b', resume_text, re.I)),
            'Skills': len(re.findall(r'\bskills\b|\btechnical\b|\bproficient\b', resume_text, re.I)),
            'Projects': len(re.findall(r'\bproject\b|\bdeveloped\b|\bbuilt\b', resume_text, re.I)),
            'Certifications': len(re.findall(r'\bcertificat\b|\bcertified\b|\bcourse\b', resume_text, re.I))
        }
        
        section_names = list(sections.keys())
        section_counts = list(sections.values())
        colors4 = ['#3b82f6', '#8b5cf6', '#10b981', '#f59e0b', '#ef4444']
        
        wedges, texts, autotexts = ax4.pie(section_counts, labels=section_names, autopct='%1.1f%%',
                                           colors=colors4, startangle=90, textprops={'fontsize': 11})
        ax4.set_title('Resume Sections Coverage', fontsize=14, fontweight='bold', pad=15)
        
        # Make percentage text bold
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(10)
        
        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
        plt.close()
        
        return output_path
        
    except Exception as e:
        print(f"Error creating visualization: {str(e)}")
        # Create error visualization
        plt.figure(figsize=(10, 6))
        plt.text(0.5, 0.5, f'Error analyzing resume\n{str(e)}', 
                ha='center', va='center', fontsize=14, wrap=True)
        plt.axis('off')
        plt.title("Resume Analysis")
        plt.savefig(output_path)
        plt.close()
        return output_path

