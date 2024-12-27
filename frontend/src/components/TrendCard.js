import React from 'react';

const TrendCard = ({ title, trends }) => {
  return (
    <div className="trend-card">
      <h2>{title}</h2>
      <ul>
        {trends.map((trend, index) => (
          <li key={index}>
            <a href={trend.link} target="_blank" rel="noopener noreferrer">
              {trend.name}
            </a>
            {trend.search_volume && <p>Search Volume: {trend.search_volume}</p>}
            {trend.views && <p>Views: {trend.views}</p>}
            {trend.upvotes && <p>Upvotes: {trend.upvotes}</p>}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TrendCard;
