import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import './GoalDetails.css';

const GoalDetail = () => {
    const { id } = useParams();
    const [goal, setGoal] = useState(null);
    const [userAnswers, setUserAnswers] = useState([]);
    const [feedback, setFeedback] = useState([]);
    const [lives, setLives] = useState(5);
    const [isGameOver, setIsGameOver] = useState(false);
    const [isFading, setIsFading] = useState(false); // To control fade animation
    const [error, setError] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        axios.get(`http://localhost:5000/api/goals/${id}`)
            .then(response => setGoal(response.data))
            .catch(error => console.error('Error fetching goal:', error));
    }, [id]);

    const handleAnswerSelect = (questionIndex, selectedOption) => {
        if (isGameOver) return;
        const updatedAnswers = [...userAnswers];
        updatedAnswers[questionIndex] = selectedOption;
        setUserAnswers(updatedAnswers);

        const isCorrect = goal.quiz[questionIndex].answer === selectedOption;

        setFeedback(prevFeedback => {
            const updatedFeedback = [...prevFeedback];
            updatedFeedback[questionIndex] = isCorrect ? 'Correct!' : 'Wrong answer. Try again!';
            return updatedFeedback;
        });

        if (!isCorrect) {
            const remainingLives = lives - 1;
            setLives(remainingLives);
            if (remainingLives <= 0) {
                setIsGameOver(true);
            }
        }
    };

    if (!goal) {
        return <div>Loading...</div>;
    }

    const nextGoalId = goal.id === 17 ? 1 : goal.id + 1;

    // Handle the transition animation
    const handleNextGoal = () => {
        setIsFading(true); // Start fade-out animation
        setTimeout(() => {
            navigate(`/goal/${nextGoalId}`); // Wait for fade-out to finish before navigating
            setIsFading(false); // Reset fading state when transitioning to the new goal
        }, 500); // Match the CSS transition duration
    };

    return (
        <div className={`goal-detail-page ${isFading ? 'fade-out' : 'fade-in'}`}>
            <h1>{goal.title}</h1>
            <img src={goal.image} alt={goal.title} />
            <p>{goal.long_description}</p>
            <div className="video-container">
                <iframe
                    src={goal.video_link}
                    title={goal.title}
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowFullScreen
                ></iframe>
            </div>

            <h2>Quiz</h2>
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
                                            className={`option ${isSelected ? (isCorrect ? 'correct' : 'wrong') : ''}`}
                                            onClick={() => handleAnswerSelect(index, option)}
                                        >
                                            {option}
                                        </li>
                                    );
                                })}
                            </ul>
                            {feedback[index] && (
                                <p className={`feedback ${feedback[index] === 'Correct!' ? 'correct' : 'wrong'}`}>
                                    {feedback[index]}
                                </p>
                            )}
                        </li>
                    ))}
                </ul>
            )}

            <button className='class-switch' onClick={handleNextGoal}>
                Go To Next Goal
            </button>
        </div>
    );
};

export default GoalDetail;
