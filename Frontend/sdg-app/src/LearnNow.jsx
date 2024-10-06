import React, { useEffect, useState } from 'react';
import Card from './Card';
import axios from 'axios'; // Import Axios
import './LearnNow.css';

function LearnNow() {
  const [cardData, setCardData] = useState([]); // State to hold goal data
  const [error, setError] = useState(null); // State to hold error messages

  useEffect(() => {
    // Fetch goals data from the backend
    axios.get('http://localhost:5000/api/goals')
      .then(response => {
        setCardData(response.data); // Set state with fetched data
      })
      .catch(error => {
        console.error('Error fetching goals data:', error);
        setError('Unable to fetch goals data.'); // Store error message
      });
  }, []);

  if (error) {
    return <p>{error}</p>; // Display error message if any
  }

  return (
    <div className="learn-now-page">
      <h1>Game-Based Learning</h1>
      <p>Get ready to dive into an interactive and engaging way to learn the SDGs through games!</p>

      <div className="card-container">
        {cardData.map(card => (
          <Card
            key={card.id}
            title={card.title}
            content={card.description} // Updated to show description
            image={card.image}
            goalId={card.id} // Pass the goal ID for routing
          />
        ))}
      </div>
    </div>
  );
}

export default LearnNow;
