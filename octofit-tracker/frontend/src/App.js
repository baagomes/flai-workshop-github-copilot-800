import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import Users from './components/Users';
import Teams from './components/Teams';
import Activities from './components/Activities';
import Workouts from './components/Workouts';
import Leaderboard from './components/Leaderboard';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark app-navbar">
          <div className="container-fluid">
            <Link className="navbar-brand navbar-brand-logo" to="/">
              <span className="hero-icon">⚡</span>
              <span className="brand-text">HERO SQUAD</span>
            </Link>
            <button 
              className="navbar-toggler" 
              type="button" 
              data-bs-toggle="collapse" 
              data-bs-target="#navbarNav" 
              aria-controls="navbarNav" 
              aria-expanded="false" 
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav ms-auto">
                <li className="nav-item">
                  <Link className="nav-link" to="/users">
                    🦸 Heroes
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">
                    🛡️ Teams
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">
                    ⚡ Power Ups
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">
                    💪 Training
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">
                    🏆 Hall of Fame
                  </Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <main className="main-content">
          <Routes>
            <Route 
              path="/" 
              element={
                <div className="container mt-5">
                  <div className="jumbotron card-effect hero-jumbotron">
                    <h1 className="display-4 font-weight-bold hero-title">ASSEMBLE, HERO! 🦸</h1>
                    <p className="lead hero-subtitle">Power up your fitness journey, unite your super team, and dominate the Hall of Fame!</p>
                    <hr className="hero-divider" />
                    <p className="mb-4 hero-description">Train like a superhero. Compete like a champion. Rise to legendary status.</p>
                    <div className="d-flex gap-2 flex-wrap">
                      <Link to="/users" className="btn btn-primary btn-lg">Meet the Heroes</Link>
                      <Link to="/teams" className="btn btn-danger btn-lg">Form Teams</Link>
                      <Link to="/activities" className="btn btn-warning btn-lg">Log Power Ups</Link>
                      <Link to="/leaderboard" className="btn btn-success btn-lg">Hall of Fame</Link>
                    </div>
                  </div>
                </div>
              } 
            />
            <Route path="/users" element={<Users />} />
            <Route path="/teams" element={<Teams />} />
            <Route path="/activities" element={<Activities />} />
            <Route path="/workouts" element={<Workouts />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
          </Routes>
        </main>

        <footer className="bg-dark text-white text-center mt-5 py-3 hero-footer">
          <p className="mb-0">⚡ 2024 HERO SQUAD - Powers United ⚡</p>
          <p className="mb-0" style={{fontSize: '0.9rem'}}>Train Hard. Fight Harder. Become Legend.</p>
        </footer>
      </div>
    </Router>
  );
}

export default App;
