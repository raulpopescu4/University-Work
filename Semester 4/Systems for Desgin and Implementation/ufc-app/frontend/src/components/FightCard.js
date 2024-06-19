import React from 'react';
import './FightCard.css';

function FightCard({ fight, handleUpdate, handleDelete, getFighterNameById }) {
  return (
    <div className="fight-card-container">
      <div className="fight-card">
        <div className="fight-card-number">Card: {fight.card}</div>
        <div className="fight-rounds">Rounds: {fight.rounds}</div>
        <div className="fight-outcome">Outcome: {fight.outcome}</div>
        <div className="fight-fighters">
          Fighters: {fight.fighters && fight.fighters.map(id => getFighterNameById(id)).join(', ')}
        </div>
        <div className="fight-card-actions">
          <button className="btn-update" onClick={() => handleUpdate(fight)}>Update</button>
          <button className="btn-delete" onClick={() => handleDelete(fight._id)}>Delete</button>
        </div>
      </div>
    </div>
  );
}

export default FightCard;
