from flask import Flask, jsonify
from flask_cors import CORS  # <-- Import CORS

app = Flask(__name__)
CORS(app)  # <-- Enable CORS for all routes

goals_data=[
    {
        "id": 1,
        "title": "No Poverty",
        "description": "End poverty in all its forms everywhere.",
        "long_description": "Poverty is a fundamental issue that affects the well-being of people worldwide. Achieving this goal is vital to improving access to resources and services and ensuring social protection for the vulnerable.",
        "image": "/images/no-poverty.jpg",
        "video_link": "https://www.youtube.com/embed/7VwK9qRflL0",
        "quiz": [
            {"question": "What is the main target of Goal 1?", "options": ["End hunger", "End poverty", "Promote gender equality"], "answer": "End poverty"},
            {"question": "By which year does the UN aim to end poverty in all forms?", "options": ["2030", "2025", "2050"], "answer": "2030"}
        ]
    },
    {
        "id": 2,
        "title": "Zero Hunger",
        "description": "End hunger, achieve food security and improved nutrition.",
        "long_description": "Zero Hunger focuses on eliminating hunger and ensuring that everyone has enough food to lead a healthy and active life. This goal emphasizes the importance of sustainable agricultural practices.",
        "image": "/images/zero-hunger.jpg",
        "video_link": "https://www.youtube.com/embed/8K9Y5NxV8P4",
        "quiz": [
            {"question": "What is a significant cause of hunger?", "options": ["Climate change", "Overpopulation", "Natural disasters"], "answer": "Natural disasters"},
            {"question": "What can help achieve food security?", "options": ["Sustainable farming", "Deforestation", "Industrial agriculture"], "answer": "Sustainable farming"}
        ]
    },
    {
        "id": 3,
        "title": "Good Health and Well-being",
        "description": "Ensure healthy lives and promote well-being for all.",
        "long_description": "This goal aims to ensure that everyone can live long, healthy lives. It addresses the prevention and treatment of diseases and aims to promote mental health and well-being.",
        "image": "/images/good-health.jpg",
        "video_link": "https://www.youtube.com/embed/8L5DZxGk4V8",
        "quiz": [
            {"question": "What is one of the targets of Goal 3?", "options": ["Reduce maternal mortality", "Increase pollution", "Promote smoking"], "answer": "Reduce maternal mortality"},
            {"question": "What can improve global health?", "options": ["Universal health coverage", "Lack of healthcare access", "High prices for medication"], "answer": "Universal health coverage"}
        ]
    },
    {
        "id": 4,
        "title": "Quality Education",
        "description": "Ensure inclusive and equitable quality education.",
        "long_description": "Quality Education ensures that everyone has access to quality education and opportunities for lifelong learning. It aims to promote equity and inclusion in education.",
        "image": "/images/quality-education.jpg",
        "video_link": "https://www.youtube.com/embed/oT5MZkk-JB0",
        "quiz": [
            {"question": "What is a target of Goal 4?", "options": ["Ensure all youth and adults achieve literacy and numeracy", "Increase dropout rates", "Limit educational access"], "answer": "Ensure all youth and adults achieve literacy and numeracy"},
            {"question": "Which aspect is critical for quality education?", "options": ["Qualified teachers", "Lack of resources", "Overcrowded classrooms"], "answer": "Qualified teachers"}
        ]
    },
    {
        "id": 5,
        "title": "Gender Equality",
        "description": "Achieve gender equality and empower all women and girls.",
        "long_description": "This goal aims to end discrimination, violence, and harmful practices against women and girls, ensuring equal rights and opportunities in all areas.",
        "image": "/images/gender-equality.jpg",
        "video_link": "https://www.youtube.com/embed/y_3W4RxSxgo",
        "quiz": [
            {"question": "What does gender equality mean?", "options": ["Equal rights for all genders", "More rights for men", "None of the above"], "answer": "Equal rights for all genders"},
            {"question": "What is a significant barrier to achieving gender equality?", "options": ["Education", "Cultural norms", "Economic opportunity"], "answer": "Cultural norms"}
        ]
    },
    {
        "id": 6,
        "title": "Clean Water and Sanitation",
        "description": "Ensure availability and sustainable management of water and sanitation.",
        "long_description": "Access to clean water and sanitation is essential for health, survival, and well-being. This goal emphasizes the importance of sustainable water management.",
        "image": "/images/clean-water.jpg",
        "video_link": "https://www.youtube.com/embed/8k2x9GlJtBA",
        "quiz": [
            {"question": "What is a significant issue regarding clean water?", "options": ["Pollution", "Availability", "Cost"], "answer": "Pollution"},
            {"question": "Which practice is essential for sanitation?", "options": ["Littering", "Waste management", "Ignoring waste"], "answer": "Waste management"}
        ]
    },
    {
        "id": 7,
        "title": "Affordable and Clean Energy",
        "description": "Ensure access to affordable, reliable, sustainable, and modern energy.",
        "long_description": "This goal aims to ensure universal access to affordable, reliable, and sustainable energy, highlighting the importance of renewable energy sources.",
        "image": "/images/affordable-clean-energy.jpg",
        "video_link": "https://www.youtube.com/embed/jOe9GV0dfAg",
        "quiz": [
            {"question": "What is a renewable energy source?", "options": ["Fossil fuels", "Solar", "Coal"], "answer": "Solar"},
            {"question": "Why is clean energy important?", "options": ["To reduce pollution", "To increase costs", "To harm health"], "answer": "To reduce pollution"}
        ]
    },
    {
        "id": 8,
        "title": "Decent Work and Economic Growth",
        "description": "Promote sustained, inclusive and sustainable economic growth.",
        "long_description": "This goal focuses on providing decent work opportunities and promoting sustainable economic growth, ensuring that everyone can benefit from economic progress.",
        "image": "/images/decent-work.jpg",
        "video_link": "https://www.youtube.com/embed/XB6e0gXlw7I",
        "quiz": [
            {"question": "What is one goal of decent work?", "options": ["High unemployment", "Job satisfaction", "Exploitation"], "answer": "Job satisfaction"},
            {"question": "What can promote economic growth?", "options": ["Investment in infrastructure", "Lack of education", "Discrimination"], "answer": "Investment in infrastructure"}
        ]
    },
    {
        "id": 9,
        "title": "Industry, Innovation and Infrastructure",
        "description": "Build resilient infrastructure, promote inclusive and sustainable industrialization.",
        "long_description": "This goal aims to develop sustainable infrastructure and promote innovation, enhancing industrial development in a way that is inclusive and environmentally friendly.",
        "image": "/images/industry-innovation.jpg",
        "video_link": "https://www.youtube.com/embed/g3OQ9mF0Hms",
        "quiz": [
            {"question": "What is an example of sustainable infrastructure?", "options": ["Highways", "Wind turbines", "Polluting factories"], "answer": "Wind turbines"},
            {"question": "What drives innovation?", "options": ["Education", "Stagnation", "Resistance to change"], "answer": "Education"}
        ]
    },
    {
        "id": 10,
        "title": "Reduced Inequality",
        "description": "Reduce inequality within and among countries.",
        "long_description": "This goal focuses on reducing inequalities in wealth and opportunity, ensuring that everyone can benefit from economic growth and development.",
        "image": "/images/reduced-inequality.jpg",
        "video_link": "https://www.youtube.com/embed/d_mZcFgHcI4",
        "quiz": [
            {"question": "What is one way to reduce inequality?", "options": ["Fair wages", "Exploitation", "Discrimination"], "answer": "Fair wages"},
            {"question": "Which region faces the highest inequality?", "options": ["Africa", "North America", "Asia"], "answer": "Africa"}
        ]
    },
    {
        "id": 11,
        "title": "Sustainable Cities and Communities",
        "description": "Make cities and human settlements inclusive, safe, resilient and sustainable.",
        "long_description": "This goal aims to create sustainable urban environments that ensure safety, inclusivity, and resilience against challenges such as climate change.",
        "image": "/images/sustainable-cities.jpg",
        "video_link": "https://www.youtube.com/embed/CBR82U-Jb8o",
        "quiz": [
            {"question": "What is a characteristic of a sustainable city?", "options": ["High pollution", "Efficient public transport", "Urban sprawl"], "answer": "Efficient public transport"},
            {"question": "What is urban resilience?", "options": ["Ability to withstand disasters", "Ignoring risks", "Pollution"], "answer": "Ability to withstand disasters"}
        ]
    },
    {
        "id": 12,
        "title": "Responsible Consumption and Production",
        "description": "Ensure sustainable consumption and production patterns.",
        "long_description": "This goal emphasizes the importance of sustainable practices in consumption and production, promoting the responsible use of resources to ensure environmental sustainability.",
        "image": "/images/responsible-consumption.jpg",
        "video_link": "https://www.youtube.com/embed/CnDgZnZWckE",
        "quiz": [
            {"question": "What is responsible consumption?", "options": ["Using resources wisely", "Overconsumption", "Wastefulness"], "answer": "Using resources wisely"},
            {"question": "What is one way to promote responsible production?", "options": ["Using eco-friendly materials", "Ignoring waste management", "Maximizing waste", "None of the above"], "answer": "Using eco-friendly materials"}
        ]
    },
    {
        "id": 13,
        "title": "Climate Action",
        "description": "Take urgent action to combat climate change and its impacts.",
        "long_description": "Climate Action focuses on reducing the effects of climate change through urgent actions and policies that promote sustainability and resilience.",
        "image": "/images/climate-action.jpg",
        "video_link": "https://www.youtube.com/embed/1YzyaE6IRmg",
        "quiz": [
            {"question": "What is a major cause of climate change?", "options": ["Deforestation", "Recycling", "Sustainable farming", "None of the above"], "answer": "Deforestation"},
            {"question": "What is one way to combat climate change?", "options": ["Using fossil fuels", "Investing in renewable energy", "Ignoring environmental policies", "None of the above"], "answer": "Investing in renewable energy"}
        ]
    },
    {
        "id": 14,
        "title": "Life Below Water",
        "description": "Conserve and sustainably use the oceans, seas and marine resources.",
        "long_description": "This goal aims to protect marine environments and promote sustainable practices to ensure the health of oceans and marine life.",
        "image": "/images/life-below-water.jpg",
        "video_link": "https://www.youtube.com/embed/nXGafAFr2gE",
        "quiz": [
            {"question": "What is a major threat to marine life?", "options": ["Plastic pollution", "Sustainable fishing", "Conservation", "None of the above"], "answer": "Plastic pollution"},
            {"question": "Which marine species is often endangered?", "options": ["Sharks", "Dolphins", "Tuna", "All of the above"], "answer": "All of the above"}
        ]
    },
    {
        "id": 15,
        "title": "Life on Land",
        "description": "Protect, restore and promote sustainable use of terrestrial ecosystems.",
        "long_description": "This goal emphasizes the importance of preserving terrestrial ecosystems and promoting sustainable land use practices.",
        "image": "/images/life-on-land.jpg",
        "video_link": "https://www.youtube.com/embed/3eHEH2d0Oas",
        "quiz": [
            {"question": "What is a key threat to forests?", "options": ["Deforestation", "Conservation", "Sustainable logging", "None of the above"], "answer": "Deforestation"},
            {"question": "Which of the following is important for biodiversity?", "options": ["Habitat destruction", "Sustainable practices", "Pollution", "None of the above"], "answer": "Sustainable practices"}
        ]
    },
    {
        "id": 16,
        "title": "Peace, Justice and Strong Institutions",
        "description": "Promote peaceful and inclusive societies.",
        "long_description": "This goal focuses on promoting peaceful societies, ensuring access to justice for all, and building effective institutions.",
        "image": "/images/peace-justice.jpg",
        "video_link": "https://www.youtube.com/embed/KvRfHUnbcE0",
        "quiz": [
            {"question": "What is essential for peace?", "options": ["Dialogue", "War", "Conflict", "None of the above"], "answer": "Dialogue"},
            {"question": "What can promote justice?", "options": ["Fair laws", "Discrimination", "Corruption", "None of the above"], "answer": "Fair laws"}
        ]
    },
    {
        "id": 17,
        "title": "Partnerships for the Goals",
        "description": "Strengthen the means of implementation and revitalize the global partnership.",
        "long_description": "This goal emphasizes the importance of partnerships at global, regional, national, and local levels to achieve the SDGs.",
        "image": "/images/partnerships.jpg",
        "video_link": "https://www.youtube.com/embed/pY2ZJfOfXhU",
        "quiz": [
            {"question": "What is a key to successful partnerships?", "options": ["Collaboration", "Competition", "Isolation", "None of the above"], "answer": "Collaboration"},
            {"question": "Which of the following is essential for partnerships?", "options": ["Trust", "Dishonesty", "Selfishness", "None of the above"], "answer": "Trust"}
        ]
    }
]


@app.route('/api/goals', methods=['GET'])
def get_goals():
    return jsonify(goals_data)

@app.route('/api/goals/<int:goal_id>', methods=['GET'])
def get_goal(goal_id):
    goal = next((goal for goal in goals_data if goal["id"] == goal_id), None)
    if goal is None:
        return jsonify({"error": "Goal not found"}), 404
    return jsonify(goal)
@app.route('/api/goals/<int:goal_id>/submit', methods=['POST'])
def submit_quiz(goal_id):
    goal = next((goal for goal in goals_data if goal["id"] == goal_id), None)
    if goal is None:
        return jsonify({"error": "Goal not found"}), 404

    user_answers = request.json.get('answers')
    if not user_answers:
        return jsonify({"error": "No answers provided"}), 400

    correct_answers = 0
    quiz = goal.get("quiz", [])

    for i, question in enumerate(quiz):
        if user_answers[i] == question["answer"]:
            correct_answers += 1

    total_questions = len(quiz)
    score = (correct_answers / total_questions) * 100

    return jsonify({"score": score, "correct_answers": correct_answers, "total_questions": total_questions})

if __name__ == '__main__':
    app.run(debug=True)
