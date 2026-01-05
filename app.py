from flask import Flask, render_template, request, redirect, url_for, jsonify, render_template_string, send_file
import os
import pickle
import pandas as pd
from werkzeug.utils import secure_filename
from pdf_search import search_skill_in_pdfs, extract_text_from_pdf  # Import the search function from pdf_search
from my_analysis import visualize_resume_from_pdf, extract_entities_from_resume 

app = Flask(__name__)


# Mock data (replace with actual data handling)
candidates = [
    {'name': 'John Doe', 'qualifications': 'Bachelor\'s in Computer Science', 'experience': '5 years', 'skills': 'Python, Java', 'cultural_fit': 8.5},
    {'name': 'Jane Smith', 'qualifications': 'Master\'s in Business Administration', 'experience': '7 years', 'skills': 'Leadership, Communication', 'cultural_fit': 9.2},
    # Add more candidate data
]


# Set the path where you want to store the uploaded PDFs
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf'}

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/handle_bulk_pdf_upload', methods=['POST'])
def handle_bulk_pdf_upload():
    if request.method == 'POST':
        # Check if the POST request has the file part
        if 'pdfFiles' not in request.files:
            return jsonify({'success': False, 'message': 'No files provided'}), 400

        pdf_files = request.files.getlist('pdfFiles')
        
        if not pdf_files or pdf_files[0].filename == '':
            return jsonify({'success': False, 'message': 'No files selected'}), 400
        
        uploaded_count = 0
        failed_files = []

        for pdf_file in pdf_files:
            # Check if the file is a PDF
            if pdf_file and allowed_file(pdf_file.filename):
                try:
                    # Securely save the file with a unique name
                    filename = secure_filename(pdf_file.filename)
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    pdf_file.save(filepath)
                    uploaded_count += 1
                except Exception as e:
                    failed_files.append(pdf_file.filename)
                    print(f"Error uploading {pdf_file.filename}: {str(e)}")
            else:
                failed_files.append(pdf_file.filename)

        # Return a JSON response indicating results
        if uploaded_count > 0:
            return jsonify({
                'success': True, 
                'message': f'Successfully uploaded {uploaded_count} file(s)',
                'count': uploaded_count,
                'failed': failed_files
            }), 200
        else:
            return jsonify({
                'success': False, 
                'message': 'No files were uploaded',
                'failed': failed_files
            }), 400

@app.route('/search_skill', methods=['POST'])
def search_skill():
    try:
        data = request.get_json()
        skill_to_search = data.get('searchSkill', '')
        
        if not skill_to_search:
            return jsonify({'success': False, 'message': 'Please provide a skill to search'}), 400
        
        # Search for the skill in PDFs
        pdf_names = search_skill_in_pdfs(skill_to_search)

        response = {
            "html": render_template_string("""
                {% if pdf_names %}
                    <div class="space-y-3">
                        {% for pdf_name in pdf_names %}
                            <div class="bg-white bg-opacity-20 backdrop-blur-sm rounded-lg p-3 sm:p-4 flex flex-col sm:flex-row items-start sm:items-center sm:justify-between gap-3 hover:bg-opacity-30 transition">
                                <div class="flex items-center space-x-2 sm:space-x-3 flex-1 w-full sm:w-auto">
                                    <i class="fas fa-file-pdf text-xl sm:text-2xl text-white flex-shrink-0"></i>
                                    <a href="{{ url_for('open_pdf', filename=pdf_name) }}" target="_blank" class="text-white text-sm sm:text-lg font-medium hover:underline truncate">
                                        {{ pdf_name }}
                                    </a>
                                </div>
                                <button onclick="analysePDF('{{ pdf_name }}')" class="w-full sm:w-auto px-4 sm:px-6 py-2 bg-white text-primary-600 rounded-lg font-semibold hover:shadow-lg transition text-sm sm:text-base">
                                    <i class="fas fa-chart-bar mr-2"></i>Analyze
                                </button>
                            </div>
                        {% endfor %}
                    </div>
                {% else %}
                    <div class="text-center text-white py-8">
                        <i class="fas fa-search text-5xl mb-4 opacity-50"></i>
                        <p class="text-xl">No candidates found with the skill "{{ skill }}"</p>
                        <p class="text-sm opacity-75 mt-2">Try searching for a different skill or upload more resumes</p>
                    </div>
                {% endif %}
            """, pdf_names=pdf_names, skill=skill_to_search)
        }

        return jsonify(response), 200
    except Exception as e:
        print(f"Error in search_skill: {str(e)}")
        return jsonify({'success': False, 'message': 'An error occurred during search'}), 500

@app.route('/analyse_pdf/<pdf_name>')
def analyse_pdf(pdf_name):
    try:
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_name)

        # Check if the file exists
        if not os.path.exists(pdf_path):
            return render_template('profile_screening.html', image_path=None, error="File not found", entities=None), 404

        # Ensure images directory exists
        os.makedirs('static/images', exist_ok=True)
        
        # Extract text and entities from resume
        resume_text = extract_text_from_pdf(pdf_path)
        entities = extract_entities_from_resume(resume_text)
        
        # Save visualization as image
        image_path = visualize_resume_from_pdf(pdf_path, "static/images/visualization.png")

        # Render the HTML with the image path and entities
        return render_template('profile_screening.html', 
                             image_path=image_path, 
                             pdf_name=pdf_name,
                             entities=entities)
    except Exception as e:
        print(f"Error in analyse_pdf: {str(e)}")
        import traceback
        traceback.print_exc()
        return render_template('profile_screening.html', image_path=None, error=str(e), entities=None)

@app.route('/open_pdf/<filename>')
def open_pdf(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(filepath, mimetype='application/pdf', as_attachment=False)


@app.route('/profile_screening', methods=['GET'])
def profile_screening():
    pdf_name = request.args.get('pdf')  # Get the PDF name from the URL parameter
    # You may want to include additional logic here to process the PDF name if needed

    # Render the profile_screening.html template and pass the PDF name
    return render_template('profile_screening.html', pdf_name=pdf_name, image_path=None)

@app.route('/qualifications-experience-analysis')
def qualifications_experience_analysis():
    return render_template('qualifications_experience_analysis.html', candidates=candidates)

@app.route('/skills-assessment')
def skills_assessment():
    return render_template('skills_assessment.html', candidates=candidates)

@app.route('/cultural-fit-evaluation')
def cultural_fit_evaluation():
    return render_template('cultural_fit_evaluation.html', candidates=candidates)

@app.route('/detailed-dashboard')
def detailed_dashboard():
    return render_template('detailed_dashboard.html', candidates=candidates)


def recommend(category, data, similarity):
    """Get top recommended resumes based on category using cosine similarity"""
    try:
        # Find all resumes in this category
        matching_resumes = data[data['Category'] == category]
        
        if matching_resumes.empty:
            return []
        
        # Get the first resume in this category as reference
        index = matching_resumes.index[0]
        
        # Get similarity scores for this resume
        distances = similarity[index]
        
        # Sort by similarity (highest first), exclude the first one (self)
        resume_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]
        
        # Extract resume IDs with their similarity scores
        recommended_resumes = []
        for i in resume_list:
            resume_idx = i[0]
            similarity_score = i[1]
            resume_id = data.iloc[resume_idx]['resume_id']
            resume_category = data.iloc[resume_idx]['Category']
            
            recommended_resumes.append({
                'resume_id': resume_id,
                'similarity_score': round(similarity_score * 100, 2),  # Convert to percentage
                'category': resume_category
            })
        
        return recommended_resumes
    except Exception as e:
        print(f"Error in recommend function: {str(e)}")
        import traceback
        traceback.print_exc()
        return []

@app.route('/index', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            selected_category = request.form.get('selected_category', '')
            
            if selected_category:
                # Use cosine similarity to get recommended resumes for the category
                recommended_resumes = recommend(selected_category, data, similarity)
                
                if recommended_resumes:
                    return render_template('index.html', 
                                         selected_category=selected_category, 
                                         resume_data=recommended_resumes,
                                         categories=sorted(data['Category'].unique()),
                                         no_matches=False)
                else:
                    # No matching resumes found
                    return render_template('index.html', 
                                         selected_category=selected_category, 
                                         resume_data=None,
                                         categories=sorted(data['Category'].unique()),
                                         no_matches=True)
            else:
                return render_template('index.html', 
                                     selected_category='', 
                                     resume_data=None, 
                                     categories=sorted(data['Category'].unique()),
                                     no_matches=False)

        return render_template('index.html', 
                             selected_category='', 
                             resume_data=None, 
                             categories=sorted(data['Category'].unique()),
                             no_matches=False)
    except Exception as e:
        print(f"Error in index route: {str(e)}")
        import traceback
        traceback.print_exc()
        return render_template('index.html', 
                             selected_category='', 
                             resume_data=None, 
                             categories=[],
                             error=str(e))


if __name__ == '__main__':
        app.config['UPLOAD_FOLDER'] = 'uploads'
        data_dict = pickle.load(open('data_dict.pkl', 'rb'))
        data = pd.DataFrame(data_dict)
        similarity = pickle.load(open('similarity.pkl', 'rb'))
        
        app.run(debug=True)

