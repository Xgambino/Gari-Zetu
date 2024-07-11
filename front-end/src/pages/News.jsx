import React, { useState, useEffect } from 'react';

function News() {
  const [news, setNews] = useState([]);

  useEffect(() => {
    async function fetchNews() {
      const response = await fetch('/api/news');
      const data = await response.json();
      setNews(data);
    }
    fetchNews();
  }, []);

  return (
    <div className="App">
      <h1>News</h1>
      <ul>
        {news.map(article => (
          <li key={article.id}>
            <h2>{article.title}</h2>
            <p>{article.content}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default News