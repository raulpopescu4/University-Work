import React, { useState } from 'react';
import './AddFighterForm.css';

function AddFighterForm({ onAdd }) {
  const [name, setName] = useState('');
  const [age, setAge] = useState('');
  const [division, setDivision] = useState('');
  const [record, setRecord] = useState('');
  const [champion, setChampion] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    onAdd({ name, age, division, record, champion });
    setName('');
    setAge('');
    setDivision('');
    setRecord('');
    setChampion(false);
  };

  return (
    <form onSubmit={handleSubmit} className="add-fighter-form">
      <input
        type="text"
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        required
      />
      <input
        type="number"
        placeholder="Age"
        value={age}
        onChange={(e) => setAge(e.target.value)}
        required
      />
      <input
        type="text"
        placeholder="Division"
        value={division}
        onChange={(e) => setDivision(e.target.value)}
        required
      />
      <input
        type="text"
        placeholder="Record"
        value={record}
        onChange={(e) => setRecord(e.target.value)}
        required
      />
      <label>
        Champion
        <input
          type="checkbox"
          checked={champion}
          onChange={(e) => setChampion(e.target.checked)}
        />
      </label>
      <button type="submit">Add Fighter</button>
    </form>
  );
}

export default AddFighterForm;
