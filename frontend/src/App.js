// frontend/src/App.js

import React from 'react';
import Navbar from './Navbar';
import AgentSection from './AgentSection';
import ServicesSection from './ServicesSection';
// Import other sections as needed

function App() {
  return (
    <div>
      <Navbar />
      <AgentSection />
      {/* <ServicesSection /> */}
      {/* Include other sections here */}
    </div>
  );
}

export default App;
