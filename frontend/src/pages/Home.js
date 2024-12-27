import React, { useEffect, useState } from 'react';
import { fetchTrends, categorizeTrends } from '../utils/api';
import TrendCard from '../components/TrendCard';

const Home = () => {
  const [trends, setTrends] = useState(null);
  const [categories, setCategories] = useState({});
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [location, setLocation] = useState('US');

  useEffect(() => {
    const getTrends = async () => {
      try {
        setLoading(true);

        // Fetch trends
        const trendsData = await fetchTrends(location);

        // Categorize trends
        const categorizedData = await categorizeTrends(trendsData);

        setTrends(trendsData);
        setCategories(categorizedData);
        setSelectedCategory('All'); // Default to "All"
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

  const handleCategoryChange = (e) => {
    setSelectedCategory(e.target.value);
  };

  const filteredTrends =
    selectedCategory === 'All'
      ? trends
      : Object.fromEntries(
          Object.entries(trends || {}).map(([source, sourceTrends]) => [
            source,
            sourceTrends.filter((trend) =>
              categories[selectedCategory]?.includes(trend.name)
            ),
          ])
        );

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

      <div className="filter-container">
        <label htmlFor="category" className="filter-label">Filter by Category: </label>
        <select id="category" className="filter-select" value={selectedCategory} onChange={handleCategoryChange}>
          <option value="All">All</option>
          {Object.keys(categories).map((category) => (
            <option key={category} value={category}>{category}</option>
          ))}
        </select>
      </div>

      <div className="trends-container">
        {filteredTrends && (
          <>
            <TrendCard title="Google Trends" trends={filteredTrends.google_trends} />
            <TrendCard title="Reddit Trends" trends={filteredTrends.reddit_trends} />
            <TrendCard title="YouTube Trends" trends={filteredTrends.youtube_trends} />
          </>
        )}
      </div>
    </div>
  );
};

export default Home;
