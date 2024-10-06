// src/components/Card.js
import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Card.css';

function Card({ title, content, image, goalId }) {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`/goal/${goalId}`);
  };

  return (
    <div
      className="card"
      onClick={handleClick}
      style={{ backgroundImage: `url(${image})` }} // Apply background image dynamically
    >
      <div className="card-content">
        <h2>{title}</h2>
        <p>{content}</p>
      </div>
    </div>
  );
}

export default Card;
