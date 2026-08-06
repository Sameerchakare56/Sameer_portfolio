"""
===================================================================
                  PORTFOLIO DATA CONFIGURATION
===================================================================
Welcome Sameer! You can easily modify, add, or remove your portfolio 
information right here in this file. 

To ADD A NEW PROJECT:
  Simply add a new dictionary block inside the 'projects' list below.
  Required keys: 'name', 'category', 'desc', 'tech', 'github', 'live', 'is_live'

To EDIT YOUR PROFILE, SKILLS, EXPERIENCE, OR EDUCATION:
  Just change the corresponding text or list items below!
===================================================================
"""

PORTFOLIO_DATA = {
    # -------------------------------------------------------------
    # PERSONAL INFORMATION
    # -------------------------------------------------------------
    'name': 'Sameer Chakravedi',
    'title': 'AI & ML Developer',
    'email': 'sameerchakravedi75@gmail.com',
    'phone': '+91 9098702377',
    'location': 'Indore, Madhya Pradesh, India',
    'github': 'https://github.com/Sameerchakare56',
    'linkedin': 'https://www.linkedin.com/in/sameerchakravedi/',
    'kaggle': 'https://www.kaggle.com/sameerchakravedi',
    'leetcode': 'https://leetcode.com/u/SameerChakravedi/',
    
    'about': (
        'Aspiring AI professional with hands-on experience in computer vision, machine learning, '
        'natural language processing, and full-stack AI solutions. I specialize in building end-to-end '
        'AI systems — from dataset curation and model training to interactive web dashboards and production deployment.'
    ),
    
    # -------------------------------------------------------------
    # TECHNICAL SKILLS
    # -------------------------------------------------------------
    'skills': [
        {
            'category': 'Languages',
            'icon': '🐍',
            'items': ['Python', 'SQL', 'MySQL', 'C++']
        },
        {
            'category': 'ML & Deep Learning',
            'icon': '🧠',
            'items': ['PyTorch', 'Scikit-learn', 'OpenCV', 'TensorFlow', 'NLP']
        },
        {
            'category': 'Data Analysis & BI',
            'icon': '📊',
            'items': ['Power BI', 'DAX', 'NumPy', 'Pandas', 'Matplotlib', 'Seaborn', 'Plotly']
        },
        {
            'category': 'Web & Frameworks',
            'icon': '⚡',
            'items': ['Django', 'FastAPI', 'Streamlit', 'HTML', 'CSS']
        },
        {
            'category': 'Tools & Platforms',
            'icon': '🛠️',
            'items': ['Git', 'GitHub', 'Render', 'Jupyter', 'VS Code']
        },
    ],

    # -------------------------------------------------------------
    # WORK EXPERIENCE
    # -------------------------------------------------------------
    'experience': [
        {
            'role': 'Python Support Intern',
            'company': 'TDBAI',
            'duration': '15 Sep 2025 –15  Dec 2025',
            'points': [
                'Built computer vision and object detection projects using YOLOv8 models.',
                'Trained custom AI models on datasets created and managed via Roboflow.',
                'Performed data annotation, preprocessing, hyperparameter training, and model evaluation.',
                'Developed and tested FastAPI backends for real-time AI model integration.',
                'Handled end-to-end AI workflows from dataset creation to live inference.',
            ],
            'tech': ['Python', 'OpenCV', 'FastAPI', 'SQL'],
        }
    ],

    # -------------------------------------------------------------
    # PROJECTS (Featured & Live Projects at the top!)
    # -------------------------------------------------------------
    'projects': [
        {
            'id': 'aura-nlp',
            'name': 'AURA-NLP | Multi-Emotion & Toxicity Engine',
            'category': 'NLP & Deep Learning',
            'filter_cat': 'nlp',
            'desc': 'Multi-Emotion & Toxicity Intelligence Engine featuring real-time text analysis, token attribution, neural self-attention heatmaps, and a 6-emotion spectrum radar.',
            'tech': ['Python', 'NLP', 'PyTorch', 'Transformers', 'FastAPI', 'Render'],
            'github': 'https://github.com/Sameerchakare56/aura-nlp',
            'live': 'https://aura-nlp.onrender.com/',
            'is_live': True,
            'featured': True,
        },
        {
            'id': 'south-asia-dashboard',
            'name': 'South Asia Data & Insights Dashboard',
            'category': 'Data Science & Dashboards',
            'filter_cat': 'dashboards',
            'desc': 'Interactive data dashboard analyzing socio-economic, environmental, and demographic metrics across South Asian countries with real-time charts and visualizations.',
            'tech': ['Python', 'Streamlit', 'Pandas', 'Plotly', 'Data Analysis'],
            'github': 'https://github.com/Sameerchakare56/south-asia-dashboard',
            'live': 'https://south-asia-dashboard-ekvi6vcywcgpaykmpkwkr5.streamlit.app/',
            'is_live': True,
            'featured': True,
        },
        {
            'id': 'global-tech-startups-powerbi',
            'name': 'Global Tech Startups Analysis (Power BI)',
            'category': 'Data Analytics · Power BI',
            'filter_cat': 'dashboards',
            'desc': 'Interactive Power BI analytics dashboard analyzing global tech startup funding, valuation trends, tech hubs, and industry growth metrics.',
            'tech': ['Power BI', 'DAX', 'Data Analysis', 'Excel'],
            'github': 'https://github.com/Sameerchakare56/Global-Tech-Startups-2026-Analysis_PowerBI',
            'live': '',
            'is_live': False,
            'featured': True,
        },
        {
            'id': 'sales-analysis-powerbi',
            'name': 'Sales Analysis & BI Dashboard',
            'category': 'Business Intelligence · Power BI',
            'filter_cat': 'dashboards',
            'desc': 'Comprehensive Power BI sales intelligence dashboard featuring KPI tracking, regional revenue breakdowns, product profitability, and customer segmentation.',
            'tech': ['Power BI', 'DAX', 'Sales Analytics', 'SQL'],
            'github': 'https://github.com/Sameerchakare56/Sales-Analysis-PowerBI',
            'live': '',
            'is_live': False,
            'featured': True,
        },
        {
            'id': 'olympic-analytics-powerbi',
            'name': 'Olympic Games Analytics Dashboard',
            'category': 'Data Visualization · Power BI',
            'filter_cat': 'dashboards',
            'desc': 'Historical Olympic Games analytics dashboard visualising medal tallies, athlete performance trends, demographic insights, and country rankings.',
            'tech': ['Power BI', 'Data Analytics', 'Visualization'],
            'github': 'https://github.com/Sameerchakare56/Olympic-Analytics-PowerBI',
            'live': '',
            'is_live': False,
            'featured': False,
        },
        {
            'id': 'movie-rec',
            'name': 'Movie Recommendation Website',
            'category': 'Machine Learning',
            'filter_cat': 'ml',
            'desc': 'A content-based movie recommendation system using cosine similarity that suggests films based on user behavior and preferences.',
            'tech': ['Python', 'Scikit-learn', 'Django', 'Pandas'],
            'github': 'https://github.com/Sameerchakare56/movie_recommendation_website',
            'live': '',
            'is_live': False,
            'featured': False,
        },
        {
            'id': 'portfolio-var',
            'name': 'Portfolio Analysis: Value at Risk',
            'category': 'Financial Analytics',
            'filter_cat': 'ml',
            'desc': 'Financial Risk Management tool that calculates Value at Risk (VaR) to estimate potential investment portfolio loss over specific timeframes with 95% confidence.',
            'tech': ['yfinance', 'Pandas', 'NumPy', 'Matplotlib', 'Seaborn'],
            'github': 'https://github.com/Sameerchakare56/Portfolio_anaylsis_Value_AT_Risk',
            'live': '',
            'is_live': False,
            'featured': False,
        },
        {
            'id': 'car-price',
            'name': 'Car Price Prediction Model',
            'category': 'Machine Learning',
            'filter_cat': 'ml',
            'desc': 'Machine learning model predicting used car prices based on features like brand, year, fuel type, and mileage.',
            'tech': ['Python', 'Scikit-learn', 'Pandas', 'Jupyter'],
            'github': 'https://github.com/Sameerchakare56/Codealpha_carprice_predictio',
            'live': '',
            'is_live': False,
            'featured': False,
        },
        {
            'id': 'iris-classification',
            'name': 'Iris Flower Classification',
            'category': 'Machine Learning',
            'filter_cat': 'ml',
            'desc': 'Classic ML classification project predicting iris flower species using multiple classification algorithms and visualization.',
            'tech': ['Python', 'Scikit-learn', 'Matplotlib'],
            'github': 'https://github.com/Sameerchakare56/Codealpha_Iris_flower_classification',
            'live': '',
            'is_live': False,
            'featured': False,
        },
    ],

    # -------------------------------------------------------------
    # EDUCATION
    # -------------------------------------------------------------
    'education': [
        {
            'degree': 'B.Tech in Artificial Intelligence',
            'school': 'SAGE University, Indore',
            'year': '2023 – 2027',
            'details': 'Specialization in Machine Learning, Deep Learning, Computer Vision, and Data Structures.',
        },
        {
            'degree': 'Higher Secondary (12th) – MP Board',
            'school': 'Govt. Gyanoday Vidyalaya, Indore',
            'year': '2022 – 2023',
            'details': 'Focus on Physics, Chemistry, and Mathematics.',
        },
        {
            'degree': 'Secondary (10th) – MP Board',
            'school': 'Govt. Gyanoday Vidyalaya, Indore',
            'year': '2020 – 2021',
            'details': 'Foundational Science and Mathematics.',
        },
    ],

    # -------------------------------------------------------------
    # CERTIFICATIONS & ACHIEVEMENTS
    # -------------------------------------------------------------
    'certifications': [
        {
            'title': 'Human-Computer Interaction (HCI)',
            'issuer': 'NPTEL (IIT Madras / IIIT Delhi)',
            'year': 'Elite + Gold (94%)',
            'icon': '🥇',
            'details': 'Secured Elite + Gold Certification with 94% score in Human-Computer Interaction offered by IIT Madras & IIIT Delhi.',
            'link': '',
        },
        {
            'title': 'Generative AI, Deep Learning & LLMs',
            'issuer': 'AICTE EduSkills',
            'year': 'Certified',
            'icon': '🧠',
            'details': 'Professional certification in Generative AI architectures, Deep Learning models, and Large Language Models (LLMs).',
            'link': '',
        },
    ],

    # 'achievements': [
    #     {
    #         'title': 'Elite + Gold Standard (94%) in NPTEL HCI',
    #         'desc': 'Awarded Elite + Gold badge by IIT Madras / IIIT Delhi for top performance (94% score) in Human-Computer Interaction.',
    #         'badge': '🥇 Elite + Gold (94%)',
    #     },
    #     {
    #         'title': 'AICTE EduSkills Certified in GenAI & LLMs',
    #         'desc': 'Certified by AICTE EduSkills in Generative AI, Deep Learning architectures, and LLM implementations.',
    #         'badge': '📜 AICTE Certified',
    #     },
    # ],
}
