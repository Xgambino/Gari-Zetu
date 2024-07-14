import React, { useEffect, useState } from "react";
import Background from "../components/Background.jsx";
import Navbar from "../components/Navbar.jsx";
import { BASE_URL } from "../components/data/data.jsx";
import "../index.css";

function Catalogue() {
  const [catalogue, setCatalogue] = useState([]);

  useEffect(() => {
    fetch(`${BASE_URL}/catalogues`)
      .then((response) => response.json())
      .then((data) => setCatalogue(data));
  }, []);

  return (
    <div>
      <Navbar />
      <Background />
    <div className="catalogue-container">
      <h1 className="catalogue-title">Catalogue</h1>
      <button className="catalogue-futuristic-button">Add to Catalogue</button>
      <ul className="catalogue-list">
        {catalogue.map((item) => (
          <li key={item.id} className="catalogue-item">
            <div className="catalogue-image-container">
              <img
                src={item.image_url}
                alt={item.brand}
                className="catalogue-image"
              />
            </div>
            <div className="catalogue-details">
              <h2 className="catalogue-brand-model">
                {item.brand} - {item.model}
              </h2>
              <p className="catalogue-category">Category: {item.category}</p>
              <p className="catalogue-price">Price: {item.price}</p>
              <p className="catalogue-rating">Rating: {item.rating}</p>
              <p className="catalogue-release-date">
                Release Date: {item.release_date}
              </p>
              <button className="catalogue-futuristic-button">Buy</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
    </div>
  );
}

export default Catalogue;
