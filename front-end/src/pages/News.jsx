import React, { useState, useEffect } from 'react';
import axios from 'axios';
import "../index.css";

const News = () => {
    const [newsArticles, setNewsArticles] = useState([]);

    useEffect(() => {
        fetchNewsArticles();
    }, []);

    const fetchNewsArticles = async () => {
        try {
            const response = await axios.get('/api/news'); // Adjust endpoint if needed
            setNewsArticles(response.data);
        } catch (error) {
            console.error('Error fetching news articles:', error);
        }
    };

    return (
        <div className="news-container">
            <h1>Latest News Articles</h1>
            <div className="news-list">
                {newsArticles.map(article => (
                    <div key={article.id} className="news-item">
                        <img src={article.image_url} alt="News" />
                        <div className="news-details">
                            <h2>{article.title}</h2>
                            <p>{article.description}</p>
                            <p>Ticket Price: {article.ticket_price}</p>
                            <p>Date: {article.date}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default News;
