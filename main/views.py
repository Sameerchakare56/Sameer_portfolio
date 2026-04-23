from django.shortcuts import render

def index(request):
    context = {
        'name': 'Sameer Chakravedi',
        'title': 'AI & ML Developer',
        'email': 'sameerchakravedi75@gmail.com',
        'phone': '9098702377',
        'location': 'Indore, Madhya Pradesh',
        'github': 'https://github.com/Sameerchakare56',
        'linkedin': 'https://www.linkedin.com/in/sameerchakravedi/',
        'about': 'Aspiring AI professional with hands-on experience in computer vision, machine learning, and full-stack AI solutions. I build real-world AI systems — from dataset creation to model deployment.',
        'skills': [
            {'category': 'Languages', 'items': ['Python', 'SQL', 'MySQL']},
            {'category': 'ML & AI', 'items': ['Scikit-learn', 'YOLOv8', 'OpenCV', 'Roboflow']},
            {'category': 'Data Analysis', 'items': ['NumPy', 'Pandas', 'Matplotlib', 'Seaborn']},
            {'category': 'Web & APIs', 'items': ['Django', 'FastAPI', 'HTML5', 'CSS3']},
            {'category': 'Tools', 'items': ['Git', 'GitHub', 'Jupyter', 'VS Code', 'PyCharm']},
        ],
        'experience': [
            {
                'role': 'Python Support Intern',
                'company': 'TDBAI',
                'duration': 'Sep 2025 – Dec 2025',
                'points': [
                    'Built computer vision and object detection projects using YOLOv8',
                    'Trained custom models on datasets managed via Roboflow',
                    'Performed data annotation, preprocessing, training, and evaluation',
                    'Developed and tested FastAPI backends for AI model integration',
                    'Handled end-to-end AI workflows from dataset creation to inference',
                ],
                'tech': ['Python', 'OpenCV', 'YOLOv8', 'Roboflow', 'FastAPI'],
            }
        ],
        'projects': [
            {
                'name': 'Movie Recommendation Website',
                'desc': 'A content-based movie recommendation system using cosine similarity that suggests films based on user behavior and preferences.',
                'tech': ['Python', 'Scikit-learn', 'Django', 'Pandas'],
                'github': 'https://github.com/Sameerchakare56/movie_recommendation_website',
            },
            {
                'name': 'Voice Command System',
                'desc': 'A voice-controlled command system that interprets spoken commands and executes corresponding actions.',
                'tech': ['Python', 'Speech Recognition'],
                'github': 'https://github.com/Sameerchakare56/voice-command-system',
            },
            {
                'name': 'Car Price Prediction',
                'desc': 'ML model that predicts used car prices based on features like brand, year, fuel type, and mileage.',
                'tech': ['Python', 'Scikit-learn', 'Pandas', 'Jupyter'],
                'github': 'https://github.com/Sameerchakare56/Codealpha_carprice_predictio',
            },
            {
                'name': 'Iris Flower Classification',
                'desc': 'Classic ML classification project that predicts iris species using multiple algorithms.',
                'tech': ['Python', 'Scikit-learn', 'Matplotlib'],
                'github': 'https://github.com/Sameerchakare56/Codealpha_Iris_flower_classification',
            },
        ],
        'education': [
            {
                'degree': 'B.Tech in Artificial Intelligence',
                'school': 'SAGE University, Indore',
                'year': '2023 – 2027',
            },
            {
                'degree': 'Higher Secondary (12th) – MP Board',
                'school': 'Govt. Gyanoday Vidyalaya, Indore',
                'year': '2022 – 2023',
            },
        ],
    }
    return render(request, 'index.html', context)
