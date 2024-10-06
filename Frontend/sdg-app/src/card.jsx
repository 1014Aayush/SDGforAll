import React from "react";
import { useNavigate } from "react-router-dom"; // Use useNavigate instead of useHistory
import "./Card.css"; // Add your card styling here

function Card({ title, content, image, goalId }) {
  const navigate = useNavigate(); // Get navigate for navigation

  const handleClick = () => {
    navigate(`/goal/${goalId}`); // Navigate to goal detail page
  };

  return (
    <div className='card' onClick={handleClick}>
      <img src={image} className="card_image" />
      <div className='card-content'>
        <h2>{title}</h2>
        <p>{content}</p>
      </div>
    </div>
  );
}

export default Card;
