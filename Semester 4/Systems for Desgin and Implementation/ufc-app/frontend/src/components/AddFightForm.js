import React, { useState, useEffect } from 'react';
import './AddFightForm.css';

function AddFightForm({ onAdd, token }) {
  const [card, setCard] = useState('');
  const [rounds, setRounds] = useState('');
  const [outcome, setOutcome] = useState('');
  const [fighter1, setFighter1] = useState('');
  const [fighter2, setFighter2] = useState('');
  const [fightersList, setFightersList] = useState([]);

  useEffect(() => {
    fetchFighters();
  }, []);

  const fetchFighters = () => {
    console.log('Token:', token); // Log the token
    fetch('https://nameless-reaches-91634-e6ccf185c907.herokuapp.com/api/fighters/allFighters', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
      .then(response => {
        console.log('Response status:', response.status); // Log the response status
        if (response.status === 403) {
          throw new Error('403 Forbidden: You do not have permission to access this resource.');
        }
        return response.json();
      })
      .then(data => setFightersList(data))
      .catch(error => console.error('Error fetching fighters:', error));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onAdd({ card, rounds, outcome, fighters: [fighter1, fighter2] });
    setCard('');
    setRounds('');
    setOutcome('');
    setFighter1('');
    setFighter2('');
  };

  return (
    <form onSubmit={handleSubmit} className="add-fight-form">
      <div className="form-group">
        <input
          type="number"
          placeholder="Card"
          value={card}
          onChange={(e) => setCard(e.target.value)}
          required
        />
        <input
          type="number"
          placeholder="Rounds"
          value={rounds}
          onChange={(e) => setRounds(e.target.value)}
          required
        />
      </div>
      <div className="form-group">
        <input
          type="text"
          placeholder="Outcome"
          value={outcome}
          onChange={(e) => setOutcome(e.target.value)}
          required
        />
      </div>
      <div className="form-group">
        <select value={fighter1} onChange={(e) => setFighter1(e.target.value)} required>
          <option value="">Select Fighter 1</option>
          {fightersList.map(fighter => (
            <option key={fighter._id} value={fighter._id}>
              {fighter.name}
            </option>
          ))}
        </select>
      </div>
      <div className="form-group">
        <select value={fighter2} onChange={(e) => setFighter2(e.target.value)} required>
          <option value="">Select Fighter 2</option>
          {fightersList.map(fighter => (
            <option key={fighter._id} value={fighter._id}>
              {fighter.name}
            </option>
          ))}
        </select>
      </div>
      <button type="submit">Add Fight</button>
    </form>
  );
}

export default AddFightForm;
