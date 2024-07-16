import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home"; 
import "./index.css"; 
import Catalogue from "./pages/Catalogue";
import News from "./pages/News";
import AboutUs from "./pages/AboutUs";
import ContactUs from "./pages/ContactUs"; 

function App() {
  return (
    <Router>
      <div>
        <Navbar /> 
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/contact" element={<ContactUs />} /> 
          <Route path="/about" element={<AboutUs />} />
          <Route path="/catalogue" element={<Catalogue />} />
          <Route path="/news" element={<News />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
