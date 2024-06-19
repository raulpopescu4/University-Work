import React, { useState, useEffect } from 'react';

function UpdateFighter({ fighter, onUpdateFighter }) {
  const [updatedFighter, setUpdatedFighter] = useState(fighter);

  useEffect(() => {
    setUpdatedFighter(fighter);
  }, [fighter]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setUpdatedFighter({ ...updatedFighter, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onUpdateFighter(updatedFighter);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="name"
        value={updatedFighter.name}
        onChange={handleChange}
        required
      />
      <input
        type="number"
        name="age"
        value={updatedFighter.age}
        onChange={handleChange}
        required
      />
      <input
        type="text"
        name="division"
        value={updatedFighter.division}
        onChange={handleChange}
        required
      />
      <input
        type="text"
        name="record"
        value={updatedFighter.record}
        onChange={handleChange}
        required
      />
      <label>
        Champion
        <input
          type="checkbox"
          name="champion"
          checked={updatedFighter.champion}
          onChange={(e) => setUpdatedFighter({ ...updatedFighter, champion: e.target.checked })}
        />
      </label>
      <button type="submit">Update Fighter</button>
    </form>
  );
}

export default UpdateFighter;
