import React from 'react';
import './FighterCard.css';

function FighterCard({ fighter, handleUpdate, handleDelete }) {
  return (
    <div className="fighter-card-container">
      <div className="fighter-card">
        <div className="fighter-name">{fighter.name}</div>
        <div className="fighter-age">Age: {fighter.age}</div>
        <div className="fighter-division">Division: {fighter.division}</div>
        <div className="fighter-record">Record: {fighter.record}</div>
        <div className="fighter-card-actions">
          <button className="btn-update" onClick={() => handleUpdate(fighter)}>Update</button>
          <button className="btn-delete" onClick={() => handleDelete(fighter._id)}>Delete</button>
        </div>
      </div>
    </div>
  );
}

export default FighterCard;
