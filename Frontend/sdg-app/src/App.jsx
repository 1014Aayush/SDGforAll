import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LandingPage from './LandingPage';
import LearnNow from './LearnNow';
import GoalDetail from './GoalDetails';
import Navbar from './Navbar';

function App() {
  return (
    <Router>
            <Navbar/>
      <Routes>
  
        <Route path="/" element={<LandingPage />} />
        <Route path="/learn" element={<LearnNow />} />
        <Route path="/goal/:id" element={<GoalDetail />} />
      </Routes>
    </Router>
  );
}

export default App;


