import React from 'react';
import './FightList.css';

function FightList({ fightsList, handleClick, getFighterNameById }) {
  const fightsTable = fightsList.map(fight => 
    <tr key={fight._id}>
      <td>{fight.card}</td>
      <td>{fight.rounds}</td>
      <td>{fight.outcome}</td>
      <td>{fight.fighters && fight.fighters.map(id => getFighterNameById(id)).join(', ')}</td>
      <td>
        <button onClick={() => handleClick(fight)}>
          Fight Details
        </button>
      </td>
    </tr>
  );

  return (
    <table>
      <thead>
        <tr>
          <th>Card</th>
          <th>Rounds</th>
          <th>Outcome</th>
          <th>Fighters</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        {fightsTable}
      </tbody>
    </table>
  );
}

export default FightList;
    