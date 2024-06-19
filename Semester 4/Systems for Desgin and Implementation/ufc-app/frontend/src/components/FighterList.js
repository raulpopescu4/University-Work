import React from 'react';
import './FighterList.css';

function FighterList({ fightersList, handleClick }) {
  const fightersTable = fightersList.map(fighter => 
    <tr key={fighter.id}>
      <td>{fighter.age}</td>
      <td>{fighter.name}</td>
      <td>{fighter.division}</td>
      <td>{fighter.record}</td>
      <td>
        <button onClick={() => handleClick(fighter)}>
          Fighter Details
        </button>
      </td>
    </tr>
  );

  return (
    <table>
      <thead>
        <tr>
          <th>Age</th>
          <th>Name</th>
          <th>Division</th>
          <th>Record</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        {fightersTable}
      </tbody>
    </table>
  );
}

export default FighterList;
