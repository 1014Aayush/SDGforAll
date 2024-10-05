import React from 'react';
import { Link as ScrollLink } from 'react-scroll'; // For smooth scroll
import { motion } from 'framer-motion'; // For animations
import './LandingPages.css';

function LandingPage() {
  return (
    <div className="landing-page">
      {/* Section 1: Hero Section */}
      <section className="hero-section">
        <motion.div
          className="hero-content"
          initial={{ opacity: 0, y: -50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1 }}
        >
          <h1>Welcome to Sustainable Development Goals Learning</h1>
          <p>Discover the 17 goals for a better world.</p>
          <ScrollLink to="learn-now" smooth={true} duration={800}>
            <button className="learn-now-btn">Learn Now</button>
          </ScrollLink>
        </motion.div>
      </section>

      {/* Section 2: About SDGs */}
      <section className="sdgs-section" id="sdgs">
        <motion.div
          className="sdgs-content"
          initial={{ opacity: 0, x: -100 }}
          whileInView={{ opacity: 1, x: 0 }}
          transition={{ duration: 1 }}
        >
          <h2>About the SDGs</h2>
          <p>The Sustainable Development Goals are a universal call to action to end poverty, protect the planet, and ensure that by 2030 all people enjoy peace and prosperity.</p>
        </motion.div>
      </section>

      {/* Section 3: Learn Now Button */}
      <section className="learn-now-section" id="learn-now">
        <motion.div
          className="learn-now-content"
          initial={{ opacity: 0, y: 50 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 1 }}
        >
          <h2>Ready to Learn?</h2>
          <p>Jump into our interactive learning platform and master the SDGs with game-based learning.</p>
          <a href="/learn" className="learn-now-btn">Start Learning</a>
        </motion.div>
      </section>
    </div>
  );
}

export default LandingPage;
