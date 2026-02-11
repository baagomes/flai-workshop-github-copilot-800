import React, { useState, useEffect } from 'react';
import getAPIUrl from '../utils/api';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchActivities = async () => {
      try {
        const apiUrl = getAPIUrl('activities');
        console.log('Fetching activities from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Activities data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const activitiesList = data.results ? data.results : Array.isArray(data) ? data : [];
        console.log('Processed activities list:', activitiesList);
        
        setActivities(activitiesList);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching activities:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchActivities();
  }, []);

  const formatDate = (dateString) => {
    if (!dateString) return 'N/A';
    try {
      const date = new Date(dateString);
      // Check if date is valid
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
          <p className="mb-0">Loading activities...</p>
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
        <h2>🏃 Activities</h2>
        <p className="text-muted">Track your fitness activities and achievements</p>
      </div>
      <div className="table-wrapper">
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>User</th>
            <th>Activity Type</th>
            <th>Duration (minutes)</th>
            <th>Calories Burned</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {activities.length > 0 ? (
            activities.map((activity) => (
              <tr key={activity.id}>
                <td><span className="badge badge-primary">#{activity.id}</span></td>
                <td><strong>{activity.user_name || activity.user}</strong></td>
                <td><span className="badge bg-success">{activity.activity_type}</span></td>
                <td><strong>{activity.duration_minutes}</strong> min</td>
                <td><span className="badge bg-warning text-dark">{activity.calories_burned} cal</span></td>
                <td>{formatDate(activity.date)}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="6">
                <div className="empty-state">
                  <div className="empty-state-icon">📊</div>
                  <p>No activities found</p>
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

export default Activities;
