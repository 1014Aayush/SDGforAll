from flask import Flask, jsonify
from flask_cors import CORS  # <-- Import CORS

app = Flask(__name__)
CORS(app)  # <-- Enable CORS for all routes

goals_data = [
    {
        "id": 1,
        "title": "No Poverty",
        "description": "End poverty in all its forms everywhere.",
        "long_description": "Poverty is a fundamental issue that affects the well-being of people worldwide. Achieving this goal is vital to improving access to resources and services and ensuring social protection for the vulnerable.",
        "image": "/images/no-poverty.jpg",
        "video_link": "https://www.youtube.com/embed/WYGIpP2Nal0?si=iMzu9eWb6pGonQKq",
        "quiz": [
            {"question": "What is one way we can help reduce poverty?", 
             "options": ["Buying a lot of clothes", "Donating to charities", "Throwing food away", "Using more electricity"], 
             "answer": "Donating to charities"},
            {"question": "Which group of people is most affected by poverty?", 
             "options": ["Only rich people", "People with a lot of money", "People without enough money for basic needs", "People who own a lot of businesses"], 
             "answer": "People without enough money for basic needs"},
            {"question": "What does 'poverty' mean?", 
             "options": ["Having too much food", "Having very little money or resources", "Having many toys", "Going on vacation often"], 
             "answer": "Having very little money or resources"},
            {"question": "How can education help end poverty?", 
             "options": ["By making people smarter so they can get better jobs", "By making people lazy", "By making people poor", "By making people fight"], 
             "answer": "By making people smarter so they can get better jobs"},
            {"question": "Why is it important to end poverty?", 
             "options": ["So everyone can have equal opportunities", "So only rich people can be happy", "To make sure everyone has toys", "To take away people’s money"], 
             "answer": "So everyone can have equal opportunities"}
        ]
    },
    {
        "id": 2,
        "title": "Zero Hunger",
        "description": "End hunger, achieve food security and improved nutrition.",
        "long_description": "Zero Hunger focuses on eliminating hunger and ensuring that everyone has enough food to lead a healthy and active life. This goal emphasizes the importance of sustainable agricultural practices.",
        "image": "/images/zero-hunger.jpg",
        "video_link": "https://www.youtube.com/embed/DNCL-1ASmNc?si=wEIalw0AFJHB1Yd2",
        "quiz": [
            {"question": "What does 'Zero Hunger' aim to achieve?", 
             "options": ["To let people eat as much as they want", "To ensure no one goes hungry", "To make sure everyone eats ice cream", "To stop people from eating"], 
             "answer": "To ensure no one goes hungry"},
            {"question": "What is one way we can help reduce hunger?", 
             "options": ["Wasting food", "Sharing food with those in need", "Eating a lot and not sharing", "Only eating junk food"], 
             "answer": "Sharing food with those in need"},
            {"question": "Which of these is a healthy food that can help fight hunger?", 
             "options": ["Vegetables", "Candy", "Cookies", "Soda"], 
             "answer": "Vegetables"},
            {"question": "What is 'malnutrition'?", 
             "options": ["When people eat too much fast food", "When people do not get enough healthy food", "When people drink too much soda", "When people skip breakfast"], 
             "answer": "When people do not get enough healthy food"},
            {"question": "How can we help farmers grow more food?", 
             "options": ["By teaching them better farming techniques", "By telling them to stop farming", "By throwing food away", "By eating all their crops"], 
             "answer": "By teaching them better farming techniques"}
        ]
    },
    {
        "id": 3,
        "title": "Good Health and Well-being",
        "description": "Ensure healthy lives and promote well-being for all.",
        "long_description": "This goal aims to ensure that everyone can live long, healthy lives. It addresses the prevention and treatment of diseases and aims to promote mental health and well-being.",
        "image": "/images/good-health.jpg",
        "video_link": "https://www.youtube.com/embed/ZVqSC_hN2lk?si=-4Pgew3zDCOP7EWB",
        "quiz": [
            {"question": "What is one way to stay healthy?", 
             "options": ["Eating junk food all the time", "Exercising and eating healthy food", "Sleeping all day", "Never drinking water"], 
             "answer": "Exercising and eating healthy food"},
            {"question": "Why is it important to wash your hands often?", 
             "options": ["To make your hands shiny", "To keep germs away and stay healthy", "To make your hands cold", "To waste water"], 
             "answer": "To keep germs away and stay healthy"},
            {"question": "What should you do if you feel sick?", 
             "options": ["Ignore it", "Tell an adult or go to a doctor", "Go play outside", "Eat candy"], 
             "answer": "Tell an adult or go to a doctor"},
            {"question": "Which of these is part of staying healthy?", 
             "options": ["Smoking", "Drinking soda all day", "Getting enough sleep", "Watching TV all night"], 
             "answer": "Getting enough sleep"},
            {"question": "How can we help others stay healthy?", 
             "options": ["By sharing information about healthy habits", "By making them eat junk food", "By telling them not to sleep", "By telling them to stop exercising"], 
             "answer": "By sharing information about healthy habits"}
        ]
    },
    {
        "id": 4,
        "title": "Quality Education",
        "description": "Ensure inclusive and equitable quality education.",
        "long_description": "Quality Education ensures that everyone has access to quality education and opportunities for lifelong learning. It aims to promote equity and inclusion in education.",
        "image": "/images/quality-education.jpg",
        "video_link": "https://www.youtube.com/embed/tlhp3K1veoQ?si=YALe2MU-LDBSqq-A",
        "quiz": [
            {"question": "What does SDG 4 aim to provide?", 
             "options": ["Quality education for all children", "Free ice cream", "No homework for anyone", "More video games"], 
             "answer": "Quality education for all children"},
            {"question": "Why is education important?", 
             "options": ["It helps us learn skills for the future", "It’s only for fun", "It helps us become professional gamers", "It helps us avoid going to school"], 
             "answer": "It helps us learn skills for the future"},
            {"question": "What should every child have a chance to do?", 
             "options": ["Go to school and learn", "Stay at home all day", "Only play video games", "Never read a book"], 
             "answer": "Go to school and learn"},
            {"question": "What can we do to support education?", 
             "options": ["Donate books and supplies", "Destroy schools", "Stop kids from learning", "Waste school materials"], 
             "answer": "Donate books and supplies"},
            {"question": "Why do some children not get a good education?", 
             "options": ["They don’t want to", "They don’t have enough teachers, books, or schools", "They only want to play", "They are too rich"], 
             "answer": "They don’t have enough teachers, books, or schools"}
        ]
    },
    {
        "id": 5,
        "title": "Gender Equality",
        "description": "Achieve gender equality and empower all women and girls.",
        "long_description": "This goal aims to end discrimination, violence, and harmful practices against women and girls, ensuring equal rights and opportunities in all areas.",
        "image": "/images/gender-equality.jpg",
        "video_link": "https://www.youtube.com/embed/vNv4WAGZAak?si=otHUiW4frTaTWLEX",
        "quiz": [
            {"question": "What is gender equality?", 
             "options": ["Treating boys and girls equally", "Only letting boys go to school", "Only letting girls play sports", "Making boys do all the chores"], 
             "answer": "Treating boys and girls equally"},
            {"question": "What is one way to promote gender equality?", 
             "options": ["Giving equal opportunities to boys and girls", "Letting only boys play games", "Making girls stay at home", "Letting boys do all the work"], 
             "answer": "Giving equal opportunities to boys and girls"},
            {"question": "Should girls have the same chance to go to school as boys?", 
             "options": ["Yes, they should", "No, only boys need school", "No, only girls need school", "No one needs school"], 
             "answer": "Yes, they should"},
            {"question": "Which of these is an example of gender equality?", 
             "options": ["Letting boys and girls choose their future jobs", "Making boys do everything", "Only letting girls cook", "Giving boys more school supplies"], 
             "answer": "Letting boys and girls choose their future jobs"},
            {"question": "Why is gender equality important?", 
             "options": ["So everyone has a fair chance in life", "So boys can do everything", "So girls can stay home", "So no one gets educated"], 
             "answer": "So everyone has a fair chance in life"}
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
            {"question": "Why is clean water important for everyone?", 
             "options": ["To keep plants healthy", "To stay clean and healthy", "To waste in water fights", "To fill swimming pools"], 
             "answer": "To stay clean and healthy"},
            {"question": "How can we save water at home?", 
             "options": ["By leaving the tap on while brushing teeth", "By fixing leaky taps", "By using water to wash the car every day", "By throwing away water bottles"], 
             "answer": "By fixing leaky taps"},
            {"question": "What can happen if people drink dirty water?", 
             "options": ["They get stronger", "They can get sick", "They feel full", "They grow faster"], 
             "answer": "They can get sick"},
            {"question": "What is one way to keep water clean?", 
             "options": ["Dumping trash into rivers", "Keeping rivers and lakes free of pollution", "Pouring oil into the sea", "Using dirty water for cooking"], 
             "answer": "Keeping rivers and lakes free of pollution"},
            {"question": "How can we help people without access to clean water?", 
             "options": ["Building wells and water filters", "Ignoring the problem", "Using all the water ourselves", "Playing in the water"], 
             "answer": "Building wells and water filters"}
        ]
    },
    {
        "id": 7,
        "title": "Affordable and Clean Energy",
        "description": "Ensure access to affordable, reliable, sustainable, and modern energy.",
        "long_description": "This goal aims to ensure universal access to affordable, reliable, and sustainable energy, highlighting the importance of renewable energy sources.",
        "image": "/images/affordable-clean-energy.jpg",
        "video_link": "https://www.youtube.com/embed/HyjNKnjpRvU?si=GSG7lxBVJBPbH8Ez",
        "quiz": [
            {"question": "What is 'clean energy'?", 
             "options": ["Energy that comes from wind, sun, or water", "Energy made by burning coal", "Energy from cooking", "Energy from candy"], 
             "answer": "Energy that comes from wind, sun, or water"},
            {"question": "Why is clean energy important?", 
             "options": ["It helps pollute the air", "It’s good for the environment", "It makes us hungry", "It breaks our machines"], 
             "answer": "It’s good for the environment"},
            {"question": "Which of these is an example of clean energy?", 
             "options": ["Solar power", "Coal power", "Gasoline power", "Burning wood"], 
             "answer": "Solar power"},
            {"question": "How can we save energy at home?", 
             "options": ["By leaving all the lights on", "By turning off lights when we leave a room", "By using more electricity", "By buying more electronics"], 
             "answer": "By turning off lights when we leave a room"},
            {"question": "What is one way to use clean energy at home?", 
             "options": ["Installing solar panels", "Using a lot of gasoline", "Burning lots of wood", "Using coal"], 
             "answer": "Installing solar panels"}
        ]
    },
    {
        "id": 8,
        "title": "Decent Work and Economic Growth",
        "description": "Promote sustained, inclusive and sustainable economic growth.",
        "long_description": "This goal focuses on providing decent work opportunities and promoting sustainable economic growth, ensuring that everyone can benefit from economic progress.",
        "image": "/images/decent-work.jpg",
        "video_link": "https://www.youtube.com/embed/dylOM3GY9PY?si=Y3MdSTufm-K9Ti2o",
        "quiz": [
            {"question": "What does 'decent work' mean?", 
             "options": ["Having a fair and safe job", "Playing video games all day", "Making people work without rest", "Working only when you feel like it"], 
             "answer": "Having a fair and safe job"},
            {"question": "Why is economic growth important?", 
             "options": ["It helps countries become wealthier and provide better jobs", "It makes everyone lazy", "It stops people from working", "It makes people fight"], 
             "answer": "It helps countries become wealthier and provide better jobs"},
            {"question": "What is one way to promote decent work for everyone?", 
             "options": ["Paying fair wages", "Making people work for free", "Giving people no time to rest", "Letting only a few people work"], 
             "answer": "Paying fair wages"},
            {"question": "What is child labor?", 
             "options": ["When children go to school", "When children are forced to work instead of studying", "When children play with toys", "When children help with homework"], 
             "answer": "When children are forced to work instead of studying"},
            {"question": "How can we help people get better jobs?", 
             "options": ["Providing education and training", "Stopping education", "Taking away books", "Making everyone stay at home"], 
             "answer": "Providing education and training"}
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
            {"question": "What is 'infrastructure'?", 
             "options": ["Roads, bridges, and buildings that help a city run", "A type of animal", "A new video game", "A kind of tree"], 
             "answer": "Roads, bridges, and buildings that help a city run"},
            {"question": "What is one way to make industries better for the environment?", 
             "options": ["Using clean energy in factories", "Burning lots of fuel", "Polluting rivers", "Throwing away waste"], 
             "answer": "Using clean energy in factories"},
            {"question": "How does innovation help people?", 
             "options": ["It makes new ideas that solve problems", "It makes people angry", "It makes everyone lazy", "It stops people from working"], 
             "answer": "It makes new ideas that solve problems"},
            {"question": "Why is good infrastructure important?", 
             "options": ["It helps cities run smoothly", "It makes people sleepy", "It makes everyone leave the city", "It stops transportation"], 
             "answer": "It helps cities run smoothly"},
            {"question": "How can we support innovation?", 
             "options": ["Encouraging creativity and new ideas", "Stopping new inventions", "Ignoring smart people", "Breaking machines"], 
             "answer": "Encouraging creativity and new ideas"}
        ]
    },
    {
        "id": 10,
        "title": "Reduced Inequality",
        "description": "Reduce inequality within and among countries.",
        "long_description": "This goal focuses on reducing inequalities in wealth and opportunity, ensuring that everyone can benefit from economic growth and development.",
        "image": "/images/reduced-inequality.jpg",
        "video_link": "https://www.youtube.com/embed/UXZcLINRGw0?si=q9F2h72RZjkZNW3t",
        "quiz": [
            {"question": "What does 'inequality' mean?", 
             "options": ["When people are treated unfairly because of differences", "When everyone has the same things", "When everyone has the same job", "When people are treated equally"], 
             "answer": "When people are treated unfairly because of differences"},
            {"question": "How can we reduce inequality?", 
             "options": ["By treating everyone fairly and giving them equal opportunities", "By only helping rich people", "By ignoring people in need", "By giving some people more rights than others"], 
             "answer": "By treating everyone fairly and giving them equal opportunities"},
            {"question": "What is one example of inequality?", 
             "options": ["Some people being paid less for the same work", "Everyone going to school", "Everyone getting the same pay", "Everyone having clean water"], 
             "answer": "Some people being paid less for the same work"},
            {"question": "Who should have equal rights and opportunities?", 
             "options": ["Only men", "Everyone, regardless of their gender, race, or background", "Only adults", "Only rich people"], 
             "answer": "Everyone, regardless of their gender, race, or background"},
            {"question": "Why is it important to reduce inequality?", 
             "options": ["So everyone has a fair chance in life", "So only rich people succeed", "So only some people can be happy", "So everyone stays the same"], 
             "answer": "So everyone has a fair chance in life"}
        ]
    },
    {
        "id": 11,
        "title": "Sustainable Cities and Communities",
        "description": "Make cities and human settlements inclusive, safe, resilient and sustainable.",
        "long_description": "This goal aims to create sustainable urban environments that ensure safety, inclusivity, and resilience against challenges such as climate change.",
        "image": "/images/sustainable-cities.jpg",
        "video_link": "https://www.youtube.com/embed/UXZcLINRGw0?si=uIKpqLDECAsAmu6n",
        "quiz": [
            {"question": "What does a 'sustainable city' mean?", 
             "options": ["A city with lots of cars", "A city that takes care of the environment and people", "A city with no rules", "A city with only tall buildings"], 
             "answer": "A city that takes care of the environment and people"},
            {"question": "What is one way to make cities cleaner?", 
             "options": ["Throwing trash in the streets", "Using public transport or bikes instead of cars", "Using more gasoline", "Cutting down all the trees"], 
             "answer": "Using public transport or bikes instead of cars"},
            {"question": "Why is it important to have parks and green spaces in cities?", 
             "options": ["For people to relax and breathe clean air", "So animals can take over the city", "To get rid of buildings", "To have more places to park cars"], 
             "answer": "For people to relax and breathe clean air"},
            {"question": "What is one way to reduce pollution in cities?", 
             "options": ["Planting more trees", "Building more factories", "Burning more coal", "Letting cars run all day"], 
             "answer": "Planting more trees"},
            {"question": "How can we make cities safer for everyone?", 
             "options": ["Building strong and safe houses", "Closing all the roads", "Letting people litter", "Making everything too expensive"], 
             "answer": "Building strong and safe houses"}
        ]
    },
    {
        "id": 12,
        "title": "Responsible Consumption and Production",
        "description": "Ensure sustainable consumption and production patterns.",
        "long_description": "This goal emphasizes the importance of sustainable practices in consumption and production, promoting the responsible use of resources to ensure environmental sustainability.",
        "image": "/images/responsible-consumption.jpg",
        "video_link": "https://www.youtube.com/embed/RX2elsVjY-c?si=INd8ml47Bl8Ople7",
        "quiz": [
            {"question": "What does 'responsible consumption' mean?", 
             "options": ["Using resources carefully and not wasting them", "Buying as much as possible", "Throwing away all food", "Leaving lights on all the time"], 
             "answer": "Using resources carefully and not wasting them"},
            {"question": "How can we reduce waste at home?", 
             "options": ["By throwing everything away", "By recycling and reusing things", "By buying more than we need", "By wasting water and energy"], 
             "answer": "By recycling and reusing things"},
            {"question": "What is 'recycling'?", 
             "options": ["Throwing things in the trash", "Turning old materials into new products", "Buying new things every day", "Breaking things on purpose"], 
             "answer": "Turning old materials into new products"},
            {"question": "What is one way we can help the planet when we shop?", 
             "options": ["Buying only what we need", "Buying things we’ll never use", "Throwing away food after buying it", "Using plastic bags for everything"], 
             "answer": "Buying only what we need"},
            {"question": "How can companies produce products more responsibly?", 
             "options": ["By using eco-friendly materials", "By polluting more", "By wasting resources", "By making products that break easily"], 
             "answer": "By using eco-friendly materials"}
        ]
    },
    {
        "id": 13,
        "title": "Climate Action",
        "description": "Take urgent action to combat climate change and its impacts.",
        "long_description": "Climate Action focuses on reducing the effects of climate change through urgent actions and policies that promote sustainability and resilience.",
        "image": "/images/climate-action.jpg",
        "video_link": "https://www.youtube.com/embed/xznlCuhqfOI?si=IEy2g6q01SFncNY0",
        "quiz": [
            {"question": "What is climate change?", 
             "options": ["A change in the weather patterns caused by human activity", "A new type of clothing", "A different kind of plant", "A game people play"], 
             "answer": "A change in the weather patterns caused by human activity"},
            {"question": "What is one way we can fight climate change?", 
             "options": ["Planting more trees", "Driving more cars", "Using more plastic", "Cutting down all the trees"], 
             "answer": "Planting more trees"},
            {"question": "Why is reducing pollution important for the climate?", 
             "options": ["It helps keep the air and water clean", "It makes the world hotter", "It stops people from breathing", "It creates more waste"], 
             "answer": "It helps keep the air and water clean"},
            {"question": "What are greenhouse gases?", 
             "options": ["Gases that trap heat in the atmosphere", "Air from the garden", "Fresh air from the forest", "Smoke from campfires"], 
             "answer": "Gases that trap heat in the atmosphere"},
            {"question": "How can using less energy help the planet?", 
             "options": ["It reduces pollution and saves resources", "It makes the air dirty", "It causes more climate change", "It wastes water"], 
             "answer": "It reduces pollution and saves resources"}
        ]
    },
    {
        "id": 14,
        "title": "Life Below Water",
        "description": "Conserve and sustainably use the oceans, seas and marine resources.",
        "long_description": "This goal aims to protect marine environments and promote sustainable practices to ensure the health of oceans and marine life.",
        "image": "/images/life-below-water.jpg",
        "video_link": "https://www.youtube.com/embed/u75w751uzoQ?si=3qUQ5Jq6W0-Xmz_3",
        "quiz": [
            {"question": "Why are oceans important for life on Earth?", 
             "options": ["They provide homes for many animals and help produce oxygen", "They are good places to throw trash", "They make the Earth hotter", "They are only for swimming"], 
             "answer": "They provide homes for many animals and help produce oxygen"},
            {"question": "How can we protect the oceans?", 
             "options": ["By throwing waste into the water", "By keeping beaches clean and reducing plastic waste", "By using more plastic bags", "By catching all the fish"], 
             "answer": "By keeping beaches clean and reducing plastic waste"},
            {"question": "What can happen if too much plastic goes into the ocean?", 
             "options": ["Marine animals can get hurt or die", "It makes the ocean cleaner", "It makes fish grow faster", "It helps animals swim better"], 
             "answer": "Marine animals can get hurt or die"},
            {"question": "What is one way to reduce plastic waste?", 
             "options": ["Using reusable bags instead of plastic ones", "Buying more plastic", "Throwing plastic into the sea", "Using plastic for everything"], 
             "answer": "Using reusable bags instead of plastic ones"},
            {"question": "Why is it important to protect coral reefs?", 
             "options": ["They are homes for many sea creatures", "They are great places for throwing trash", "They make the ocean warmer", "They are just rocks"], 
             "answer": "They are homes for many sea creatures"}
        ]
    },
    {
        "id": 15,
        "title": "Life on Land",
        "description": "Protect, restore and promote sustainable use of terrestrial ecosystems.",
        "long_description": "This goal emphasizes the importance of preserving terrestrial ecosystems and promoting sustainable land use practices.",
        "image": "/images/life-on-land.jpg",
        "video_link": "https://www.youtube.com/embed/N5YR2GMhYcI?si=43JTNavEDikj-dhM",
        "quiz": [
            {"question": "What is one way to protect forests and animals?", 
             "options": ["Planting trees and stopping deforestation", "Cutting down all the trees", "Hunting all the animals", "Building more cities in forests"], 
             "answer": "Planting trees and stopping deforestation"},
            {"question": "Why are trees important for life on Earth?", 
             "options": ["They provide oxygen and habitats for animals", "They make the ground hard", "They stop animals from living", "They take away air"], 
             "answer": "They provide oxygen and habitats for animals"},
            {"question": "How can we help protect endangered animals?", 
             "options": ["By not destroying their homes and stopping illegal hunting", "By hunting them", "By building cities in their homes", "By throwing trash in the forest"], 
             "answer": "By not destroying their homes and stopping illegal hunting"},
            {"question": "What is one way to protect the environment on land?", 
             "options": ["Reducing pollution and planting more trees", "Cutting down forests", "Throwing trash in rivers", "Destroying animal habitats"], 
             "answer": "Reducing pollution and planting more trees"},
            {"question": "Why is biodiversity important?", 
             "options": ["It keeps ecosystems balanced and healthy", "It makes the planet dirtier", "It causes animals to disappear", "It stops trees from growing"], 
             "answer": "It keeps ecosystems balanced and healthy"}
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
            {"question": "What is 'peace'?", 
             "options": ["Living in harmony without fighting", "Having lots of arguments", "Breaking the law", "Ignoring others"], 
             "answer": "Living in harmony without fighting"},
            {"question": "What is one way to promote peace in your community?", 
             "options": ["Solving problems by talking instead of fighting", "Starting fights with others", "Ignoring people", "Breaking things"], 
             "answer": "Solving problems by talking instead of fighting"},
            {"question": "Why is justice important?", 
             "options": ["It ensures that everyone is treated fairly", "It helps only some people", "It makes people angry", "It ignores the law"], 
             "answer": "It ensures that everyone is treated fairly"},
            {"question": "What does it mean to have strong institutions?", 
             "options": ["Having governments and organizations that follow laws and protect people's rights", "Having no rules", "Ignoring people's needs", "Making unfair laws"], 
             "answer": "Having governments and organizations that follow laws and protect people's rights"},
            {"question": "How can you contribute to peace and justice?", 
             "options": ["By respecting others and following the rules", "By breaking the law", "By ignoring people's rights", "By causing trouble"], 
             "answer": "By respecting others and following the rules"}
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
            {"question": "What is a 'partnership'?", 
             "options": ["When people or organizations work together to achieve something", "When everyone works alone", "When people fight against each other", "When people ignore each other"], 
             "answer": "When people or organizations work together to achieve something"},
            {"question": "Why are partnerships important for the SDGs?", 
             "options": ["They help people work together to solve global problems", "They make people argue", "They stop progress", "They divide people"], 
             "answer": "They help people work together to solve global problems"},
            {"question": "What is one example of a partnership for the SDGs?", 
             "options": ["Countries working together to reduce poverty", "Everyone working separately", "Fighting over resources", "Ignoring each other's problems"], 
             "answer": "Countries working together to reduce poverty"},
            {"question": "How can individuals help with the SDGs?", 
             "options": ["By working with others and taking action", "By staying silent", "By ignoring global issues", "By working alone"], 
             "answer": "By working with others and taking action"},
            {"question": "What is one way to encourage partnerships for the SDGs?", 
             "options": ["Sharing ideas and resources", "Keeping everything to ourselves", "Stopping communication", "Working alone"], 
             "answer": "Sharing ideas and resources"}
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
