import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home"; 
import "./index.css"; 
import Catalogue from "./pages/Catalogue";
import News from "./pages/News";
import AboutUs from "./pages/AboutUs";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/contact" element={ContactUs} />
        <Route path="/about" element={<AboutUs />} />
        <Route path="/catalogue" element={<Catalogue />} />
        <Route path="/news" element={<News />} />
      </Routes>
    </Router>
  );
}

export default App;
