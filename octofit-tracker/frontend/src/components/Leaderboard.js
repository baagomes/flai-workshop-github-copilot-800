import React, { useState, useEffect } from 'react';
import getAPIUrl from '../utils/api';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      try {
        const apiUrl = getAPIUrl('leaderboard');
        console.log('Fetching leaderboard from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Leaderboard data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const leaderboardList = data.results ? data.results : Array.isArray(data) ? data : [];
        console.log('Processed leaderboard list:', leaderboardList);
        
        setLeaderboard(leaderboardList);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching leaderboard:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchLeaderboard();
  }, []);

  if (loading) {
    return (
      <div className="container mt-5">
        <div className="loading-state">
          <div className="spinner-border me-3" role="status"></div>
          <p className="mb-0">Loading leaderboard...</p>
        </div>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="container mt-5">
        <div className="error-state">
          <span className="error-state-icon">⚠️</span>
          <p className="mb-0"><strong>Error:</strong> {error}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-5">
      <div className="page-header">
        <h2>🏅 Leaderboard</h2>
        <p className="text-muted">Compete and climb the rankings</p>
      </div>
      <div className="table-wrapper">
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Rank</th>
            <th>User</th>
            <th>Team</th>
            <th>Total Calories Burned</th>
            <th>Activities Completed</th>
            <th>Points</th>
          </tr>
        </thead>
        <tbody>
          {leaderboard.length > 0 ? (
            leaderboard.map((entry, index) => (
              <tr key={entry.id}>
                <td>
                  <div style={{ fontSize: '1.5rem', minWidth: '40px' }}>
                    {index === 0 ? '🥇' : index === 1 ? '🥈' : index === 2 ? '🥉' : <span className="badge bg-secondary">{index + 1}</span>}
                  </div>
                </td>
                <td><strong>{entry.user_name || entry.user}</strong></td>
                <td>
                  {entry.team_name || entry.team ? (
                    <span className="badge bg-primary">{entry.team_name || entry.team}</span>
                  ) : (
                    <span className="text-muted">—</span>
                  )}
                </td>
                <td><span className="badge bg-warning text-dark">{entry.total_calories_burned || 0} cal</span></td>
                <td>{entry.activities_count || 0}</td>
                <td><span className="badge bg-success font-weight-bold">{entry.points || 0} pts</span></td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="6">
                <div className="empty-state">
                  <div className="empty-state-icon">🏅</div>
                  <p>No leaderboard entries found</p>
                </div>
              </td>
            </tr>
          )}
        </tbody>
      </table>
      </div>
    </div>
  );
};

export default Leaderboard;
