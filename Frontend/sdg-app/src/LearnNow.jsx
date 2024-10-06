import React from 'react';
import Card from './card';
import './LearnNow.css';

const cardData = [
  { id: 1, title: "No Poverty", content: "End poverty in all its forms everywhere.", image: "/images/no-poverty.jpg" },
  { id: 2, title: "Zero Hunger", content: "End hunger, achieve food security and improved nutrition.", image: "/images/zero-hunger.jpg" },
  { id: 3, title: "Good Health and Well-being", content: "Ensure healthy lives and promote well-being for all.", image: "/images/good-health.jpg" },
  { id: 4, title: "Quality Education", content: "Ensure inclusive and equitable quality education.", image: "/images/quality-education.jpg" },
  { id: 5, title: "Gender Equality", content: "Achieve gender equality and empower all women and girls.", image: "/images/gender-equality.jpg" },
  // Add up to 16 cards
];

function LearnNow() {
  return (
    <div className="learn-now-page">
      <h1>Game-Based Learning</h1>
      <p>Get ready to dive into an interactive and engaging way to learn the SDGs through games!</p>
      {/* This section can later be replaced with an actual game-based learning system */}

      <div className="card-container">
        {cardData.map(card => (
          <Card key={card.id} title={card.title} content={card.content} image={card.image} />
        ))}
      </div>
      {/*<div className="game-placeholder">
        <h2>Game Area</h2>
        <p>This will host your SDG learning games.</p>
      </div>*/}
    </div>
  );
}

export default LearnNow;


