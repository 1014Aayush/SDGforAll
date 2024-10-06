import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import './GoalDetails.css';

const GoalDetail = () => {
    const { id } = useParams();
    const [goal, setGoal] = useState(null);
    const [userAnswers, setUserAnswers] = useState([]); // Track user's answers
    const [feedback, setFeedback] = useState([]); // Track feedback for each question
    const [lives, setLives] = useState(5); // Initial 5 lives
    const [isGameOver, setIsGameOver] = useState(false); // To track if user is out of lives

    useEffect(() => {
        axios.get(`http://localhost:5000/api/goals/${id}`)
            .then(response => setGoal(response.data))
            .catch(error => console.error('Error fetching goal:', error));
    }, [id]);

    // Handle answer selection for each question
    const handleAnswerSelect = (questionIndex, selectedOption) => {
        if (isGameOver) return; // Disable interaction when the game is over

        const updatedAnswers = [...userAnswers];
        updatedAnswers[questionIndex] = selectedOption;
        setUserAnswers(updatedAnswers);

        // Check if the selected answer is correct
        const isCorrect = goal.quiz[questionIndex].answer === selectedOption;

        setFeedback(prevFeedback => {
            const updatedFeedback = [...prevFeedback];
            updatedFeedback[questionIndex] = isCorrect ? 'Correct!' : 'Wrong answer. Try again!';
            return updatedFeedback;
        });

        // If the answer is incorrect, decrease a life
        if (!isCorrect) {
            const remainingLives = lives - 1;
            setLives(remainingLives);
            if (remainingLives <= 0) {
                setIsGameOver(true); // End the session if lives reach 0
            }
        }
    };

    if (!goal) {
        return <div>Loading...</div>;
    }

    return (
        <div className="goal-detail-page">
            <h1>{goal.title}</h1>
            <img src={goal.image} alt={goal.title} />
            <p>{goal.long_description}</p>
            <div className="video-container">
                <iframe 
                    src={goal.video_link} 
                    title={goal.title} 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowFullScreen>
                </iframe>
            </div>

            <h2>Quiz</h2>

            {/* Display remaining lives as hearts */}
            <div className="life-system">
                {Array.from({ length: lives }).map((_, index) => (
                    <span key={index} className="heart">❤️</span>
                ))}
            </div>

            {isGameOver ? (
                <div className="game-over-message">
                    <h3>Game Over! You've used all your lives.</h3>
                    <p>Take a break and come back refreshed!</p>
                </div>
            ) : (
                <ul>
                    {goal.quiz.map((question, index) => (
                        <li key={index}>
                            <p>{question.question}</p>
                            <ul>
                                {question.options.map((option, optionIndex) => {
                                    const isSelected = userAnswers[index] === option;
                                    const isCorrect = goal.quiz[index].answer === option;

                                    return (
                                        <li 
                                            key={optionIndex} 
                                            className={`option ${isSelected ? (isCorrect ? 'correct' : 'wrong') : ''}`} // Set correct class based on selection
                                            onClick={() => handleAnswerSelect(index, option)}>
                                            {option}
                                        </li>
                                    );
                                })}
                            </ul>
                            {/* Display feedback for the current question */}
                            {feedback[index] && <p className={`feedback ${feedback[index] === 'Correct!' ? 'correct' : 'wrong'}`}>{feedback[index]}</p>}
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default GoalDetail;
