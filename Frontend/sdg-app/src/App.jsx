import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [sdgs, setSdgs] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/sdgs')
      .then(response => setSdgs(response.data))
      .catch(error => console.error('Error fetching SDG data:', error));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Sustainable Development Goals</h1>
        <div className="sdg-container">
          {sdgs.map(sdg => (
            <div key={sdg.id} className="sdg-card">
              <h2>{sdg.title}</h2>
              <p>{sdg.description}</p>
            </div>
          ))}
        </div>
      </header>
    </div>
  );
}

export default App;
