import React, { useState, useEffect } from 'react';
import getAPIUrl from '../utils/api';

const Users = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const apiUrl = getAPIUrl('users');
        console.log('Fetching users from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Users data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const usersList = data.results ? data.results : Array.isArray(data) ? data : [];
        console.log('Processed users list:', usersList);
        
        setUsers(usersList);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching users:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchUsers();
  }, []);

  if (loading) {
    return (
      <div className="container mt-5">
        <div className="loading-state">
          <div className="spinner-border me-3" role="status"></div>
          <p className="mb-0">Loading users...</p>
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
        <h2>👥 Users</h2>
        <p className="text-muted">Manage and view all user profiles</p>
      </div>
      <div className="table-wrapper">
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Team</th>
            <th>Fitness Level</th>
            <th>Points</th>
          </tr>
        </thead>
        <tbody>
          {users.length > 0 ? (
            users.map((user) => (
              <tr key={user.email}>
                <td><span className="badge badge-primary">{user.id || '—'}</span></td>
                <td>
                  <strong>{user.name || 'N/A'}</strong>
                </td>
                <td><a href={`mailto:${user.email}`}>{user.email}</a></td>
                <td>{user.team || 'N/A'}</td>
                <td><span className="badge bg-info">{user.fitness_level || 'N/A'}</span></td>
                <td>{user.total_points || 0}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="6">
                <div className="empty-state">
                  <div className="empty-state-icon">📋</div>
                  <p>No users found</p>
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

export default Users;
