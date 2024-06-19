import React, { useState, useEffect } from 'react';

function UpdateFightForm({ fight, onUpdateFight, token }) {
  const [updatedFight, setUpdatedFight] = useState(fight);
  const [fightersList, setFightersList] = useState([]);

  useEffect(() => {
    setUpdatedFight(fight);
    fetchFighters();
  }, [fight]);

  const fetchFighters = () => {
    fetch('https://nameless-reaches-91634-e6ccf185c907.herokuapp.com/api/fighters/allFighters', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
      .then(response => response.json())
      .then(data => setFightersList(data))
      .catch(error => console.error('Error fetching fighters:', error));
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setUpdatedFight({ ...updatedFight, [name]: value });
  };

  const handleFighter1Change = (e) => {
    const { value } = e.target;
    setUpdatedFight({ ...updatedFight, fighters: [value, updatedFight.fighters[1]] });
  };

  const handleFighter2Change = (e) => {
    const { value } = e.target;
    setUpdatedFight({ ...updatedFight, fighters: [updatedFight.fighters[0], value] });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onUpdateFight(updatedFight);
  };

  return (
    <form onSubmit={handleSubmit} className="update-fight-form">
      <div className="form-group">
        <input
          type="number"
          name="card"
          value={updatedFight.card}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="rounds"
          value={updatedFight.rounds}
          onChange={handleChange}
          required
        />
      </div>
      <div className="form-group">
        <input
          type="text"
          name="outcome"
          value={updatedFight.outcome}
          onChange={handleChange}
          required
        />
      </div>
      <div className="form-group">
        <select value={updatedFight.fighters[0]} onChange={handleFighter1Change} required>
          <option value="">Select Fighter 1</option>
          {fightersList.map(fighter => (
            <option key={fighter._id} value={fighter._id}>
              {fighter.name}
            </option>
          ))}
        </select>
      </div>
      <div className="form-group">
        <select value={updatedFight.fighters[1]} onChange={handleFighter2Change} required>
          <option value="">Select Fighter 2</option>
          {fightersList.map(fighter => (
            <option key={fighter._id} value={fighter._id}>
              {fighter.name}
            </option>
          ))}
        </select>
      </div>
      <button type="submit">Update Fight</button>
    </form>
  );
}

export default UpdateFightForm;
