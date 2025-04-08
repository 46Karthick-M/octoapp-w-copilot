import React from 'react';
import './styles/App.css';

const App = () => {
    return (
        <div className="App">
            <header className="App-header">
                <h1>Welcome to OctoFit Tracker</h1>
                <p>Track your fitness journey and compete with your friends!</p>
            </header>
            <main>
                {/* Future components will be added here */}
            </main>
            <footer>
                <p>&copy; {new Date().getFullYear()} Mergington High School</p>
            </footer>
        </div>
    );
};

export default App;