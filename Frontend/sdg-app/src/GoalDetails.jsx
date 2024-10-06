import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import './GoalDetails.css';

function GoalDetail() {
  const { id } = useParams(); // Get the goal id from the route parameters
  const [goal, setGoal] = useState(null);
  const [error, setError] = useState(null);
  const navigate = useNavigate(); // Initialize useNavigate

  useEffect(() => {
    // Fetch goal details from the backend
    axios.get(`http://localhost:5000/api/goals/${id}`)
      .then(response => {
        setGoal(response.data);
      })
      .catch(error => {
        setError('Unable to fetch goal details.');
        console.error('Error fetching goal details:', error);
      });
  }, [id]);

  if (error) {
    return <p>{error}</p>;
  }

  if (!goal) {
    return <p>Loading...</p>;
  }

  // Calculate the next goal ID
  const nextGoalId = goal.id === 17 ? 1 : goal.id + 1;

  return (
    <div className="goal-detail-page">
      <h1>{goal.title}</h1>
      <img src={goal.image} alt={goal.title} />
      <p>{goal.long_description}</p>
      
      {/* Video Section */}
      <div className="video-container">
        <iframe
          width="560"
          height="315"
          src={goal.video_link}
          title={goal.title}
          frameBorder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowFullScreen
        ></iframe>
      </div>

      {/* Quiz Section */}
      <h2>Quiz</h2>
      <ul>
        {goal.quiz.map((quizItem, index) => (
          <li key={index}>
            <p><strong>{quizItem.question}</strong></p>
            <ul>
              {quizItem.options.map((option, optionIndex) => (
                <li key={optionIndex}>{option}</li>
              ))}
            </ul>
          </li>
        ))}
      </ul>

      {/* Button to navigate to the next goal */}
      <button className='class-switch' onClick={() => navigate(`/goal/${nextGoalId}`)}>
        Go To Next Goal
      </button>
    </div>
  );
}

export default GoalDetail;
