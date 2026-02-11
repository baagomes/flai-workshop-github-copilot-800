import React, { useState, useEffect } from 'react';
import getAPIUrl from '../utils/api';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTeams = async () => {
      try {
        const apiUrl = getAPIUrl('teams');
        console.log('Fetching teams from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Teams data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const teamsList = data.results ? data.results : Array.isArray(data) ? data : [];
        console.log('Processed teams list:', teamsList);
        
        setTeams(teamsList);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching teams:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchTeams();
  }, []);

  const formatDate = (dateString) => {
    if (!dateString) return 'N/A';
    try {
      const date = new Date(dateString);
      if (isNaN(date.getTime())) {
        return 'Invalid Date';
      }
      return date.toLocaleDateString('en-US', { 
        year: 'numeric', 
        month: 'short', 
        day: 'numeric' 
      });
    } catch (e) {
      return 'Invalid Date';
    }
  };

  if (loading) {
    return (
      <div className="container mt-5">
        <div className="loading-state">
          <div className="spinner-border me-3" role="status"></div>
          <p className="mb-0">Loading teams...</p>
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
        <h2>🏆 Teams</h2>
        <p className="text-muted">Create and manage competitive teams</p>
      </div>
      <div className="table-wrapper">
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Description</th>
            <th>Created At</th>
            <th>Members</th>
          </tr>
        </thead>
        <tbody>
          {teams.length > 0 ? (
            teams.map((team) => (
              <tr key={team.id}>
                <td><span className="badge badge-primary">#{team.id}</span></td>
                <td><strong>{team.name}</strong></td>
                <td>{team.description ? <span>{team.description}</span> : <span className="text-muted">—</span>}</td>
                <td>{formatDate(team.created_at)}</td>
                <td><span className="badge bg-info text-dark">{team.members_count || 0} members</span></td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="5">
                <div className="empty-state">
                  <div className="empty-state-icon">🏆</div>
                  <p>No teams found</p>
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

export default Teams;
