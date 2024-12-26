import React, { useEffect, useState } from 'react';
import { fetchTrends } from '../utils/api';

const Home = () => {
  const [trends, setTrends] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [location, setLocation] = useState('US');

  useEffect(() => {
    const getTrends = async () => {
      try {
        setLoading(true);
        const data = await fetchTrends(location);
        setTrends(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    getTrends();
  }, [location]);

  const handleLocationChange = (e) => {
    setLocation(e.target.value);
  };

  if (loading) return <div className="loading">Loading trends...</div>;
  if (error) return <div className="error">Error: {error}</div>;

  return (
    <div>
      <div className="filter-container">
        <label htmlFor="location" className="filter-label">Select Location: </label>
        <select id="location" className="filter-select" value={location} onChange={handleLocationChange}>
          <option value="US">United States</option>
          <option value="IN">India</option>
          <option value="CA">Canada</option>
          <option value="GB">United Kingdom</option>
          <option value="AU">Australia</option>
        </select>
      </div>
      <div className="trends-container">
        {trends && (
          <>
            <div className="trend-card">
              <h2>Google Trends</h2>
              <ul>
                {trends.google_trends.map((trend, index) => (
                  <li key={index}>
                    <a
                      href={trend.link}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="trend-link"
                    >
                      {trend.name}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
            <div className="trend-card">
              <h2>Reddit Trends</h2>
              <ul>
                {trends.reddit_trends.map((trend, index) => (
                  <li key={index}>
                    <a
                      href={trend.link}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="trend-link"
                    >
                      {trend.name}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
            <div className="trend-card">
              <h2>YouTube Trends</h2>
              <ul>
                {trends.youtube_trends.map((trend, index) => (
                  <li key={index}>
                    <a
                      href={trend.link}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="trend-link"
                    >
                      {trend.name}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
            <div className="trend-card">
              <h2>BBC Trends</h2>
              <ul>
                {trends.bbc_trends.map((trend, index) => (
                  <li key={index}>
                    <a
                      href={trend.link}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="trend-link"
                    >
                      {trend.name}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export default Home;
