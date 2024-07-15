import React from 'react'
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import Navbar from "../components/Navbar.jsx";
import CatalogueVideo from "../components/CatalogueVideo.jsx";
import "../index.css";
function AboutUs() {
  return (
    <div>
      <Navbar />
      <CatalogueVideo/>
    <div className="about-us-container">
      <div className="about-us-content">
        <h2>About Us</h2>
        <p>Welcome to our futuristic car dealership where innovation meets excellence. We are dedicated to providing cutting-edge vehicles and exceptional customer service.</p>
        <p>Our showroom features the latest in automotive technology, from electric vehicles to autonomous driving solutions. Visit us today and experience the future of driving.</p>
        <p>For inquiries or test drives, contact us at <a href="tel:+1234567890">123-456-7890</a> or email <a href="mailto:info@futuristiccars.com">info@futuristiccars.com</a>.</p>
    </div>
    </div>
    </div>
);
};

export default AboutUs