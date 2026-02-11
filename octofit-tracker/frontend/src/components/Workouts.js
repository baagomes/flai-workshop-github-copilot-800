import React, { useState, useEffect } from 'react';
import getAPIUrl from '../utils/api';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      try {
        const apiUrl = getAPIUrl('workouts');
        console.log('Fetching workouts from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Workouts data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const workoutsList = data.results ? data.results : Array.isArray(data) ? data : [];
        console.log('Processed workouts list:', workoutsList);
        
        setWorkouts(workoutsList);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching workouts:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  if (loading) {
    return (
      <div className="container mt-5">
        <div className="loading-state">
          <div className="spinner-border me-3" role="status"></div>
          <p className="mb-0">Loading workouts...</p>
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
        <h2>💪 Personalized Workouts</h2>
        <p className="text-muted">Custom workout suggestions based on your fitness level</p>
      </div>
      <div className="table-wrapper">
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>User</th>
            <th>Workout Type</th>
            <th>Difficulty</th>
            <th>Duration (minutes)</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          {workouts.length > 0 ? (
            workouts.map((workout) => (
              <tr key={workout.id}>
                <td><span className="badge badge-primary">#{workout.id}</span></td>
                <td><strong>{workout.user_name || workout.user}</strong></td>
                <td><span className="badge bg-info text-dark">{workout.workout_type}</span></td>
                <td>
                  {workout.difficulty === 'easy' && <span className="badge bg-success">🟢 Easy</span>}
                  {workout.difficulty === 'medium' && <span className="badge bg-warning text-dark">🟡 Medium</span>}
                  {workout.difficulty === 'hard' && <span className="badge bg-danger">🔴 Hard</span>}
                  {!['easy', 'medium', 'hard'].includes(workout.difficulty) && <span className="badge bg-secondary">{workout.difficulty}</span>}
                </td>
                <td><strong>{workout.duration_minutes}</strong> min</td>
                <td>{workout.description ? <span>{workout.description}</span> : <span className="text-muted">—</span>}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="6">
                <div className="empty-state">
                  <div className="empty-state-icon">🏋️</div>
                  <p>No workouts found</p>
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

export default Workouts;
