import React, { useState, useEffect } from 'react';
import FighterCard from './components/FighterCard';
import FighterList from './components/FighterList';
import AddFighterForm from './components/AddFighterForm';
import UpdateFighter from './components/UpdateFighter';
import FightCard from './components/FightCard';
import FightList from './components/FightList';
import AddFightForm from './components/AddFightForm';
import UpdateFightForm from './components/UpdateFightForm';
import FighterDoughnutChart from './components/FighterChart';
import LoginForm from './components/LoginForm';
import SignupForm from './components/SignupForm';
import './App.css';

function App() {
  const [fightersList, setFightersList] = useState([]);
  const [fightsList, setFightsList] = useState([]);
  const [selectedFighter, setSelectedFighter] = useState(null);
  const [updateFighter, setUpdateFighter] = useState(null);
  const [selectedFight, setSelectedFight] = useState(null);
  const [updateFight, setUpdateFight] = useState(null);
  const [currentPage, setCurrentPage] = useState(1);
  const [itemsPerPage] = useState(4);
  const [isSorted, setIsSorted] = useState(false);
  const [internetStatus, setInternetStatus] = useState(true);
  const [backendStatus, setBackendStatus] = useState(true);
  const [token, setToken] = useState(localStorage.getItem('token'));
  const [isLoggedIn, setIsLoggedIn] = useState(!!localStorage.getItem('token'));
  const [showLogin, setShowLogin] = useState(true);
  const backendurl = 'https://nameless-reaches-91634-e6ccf185c907.herokuapp.com';

  useEffect(() => {
    if (token) {
      console.log('Initial token:', token);
      fetchData(token);
    }
    checkInternetStatus();
    checkBackendStatus();
    const interval = setInterval(() => {
      checkInternetStatus();
      checkBackendStatus();
    }, 5000);
    return () => clearInterval(interval);
  }, [token]);

  const fetchData = async (token) => {
    console.log('Fetching data with token:', token);
    await fetchFighters(token);
    await fetchFights(token);
  };

  const fetchFighters = async (token) => {
    try {
      console.log('Fetching fighters with token:', token);
      const response = await fetch(`${backendurl}/api/fighters/allFighters`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });
      if (!response.ok) {
        throw new Error(`Network response was not ok: ${response.statusText}`);
      }
      const data = await response.json();
      console.log('Fetched fighters:', data);
      setFightersList(Array.isArray(data) ? data : []);
    } catch (error) {
      console.error('Error fetching fighters:', error);
    }
  };

  const fetchFights = async (token) => {
    try {
      console.log('Fetching fights with token:', token);
      const response = await fetch(`${backendurl}/api/fights/allFights`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });
      if (!response.ok) {
        throw new Error(`Network response was not ok: ${response.statusText}`);
      }
      const data = await response.json();
      console.log('Fetched fights:', data);
      setFightsList(Array.isArray(data) ? data : []);
    } catch (error) {
      console.error('Error fetching fights:', error);
    }
  };

  const checkInternetStatus = () => {
    fetch('https://www.google.com', { mode: 'no-cors' })
      .then(() => setInternetStatus(true))
      .catch(() => setInternetStatus(false));
  };

  const checkBackendStatus = () => {
    if (!token) {
      console.log('No token available for backend status check');
      setBackendStatus(false);
      return;
    }
    console.log('Checking backend status with token:', token);
    fetch(`${backendurl}/api/fighters/allFighters`, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
      .then(response => {
        if (!response.ok) {
          throw new Error(`Backend check failed: ${response.statusText}`);
        }
        setBackendStatus(true);
      })
      .catch(error => {
        console.error('Error checking backend status:', error);
        setBackendStatus(false);
      });
  };

  const handleErrorMessage = (message) => {
    return (
      <div className="error-message">
        {message}
      </div>
    );
  };

  const handleLogin = (token) => {
    console.log('Handling login with token:', token);
    localStorage.setItem('token', token);
    setToken(token);
    setIsLoggedIn(true);
    fetchData(token);
  };

  const handleLogout = () => {
    console.log('Handling logout');
    localStorage.removeItem('token');
    setToken(null);
    setIsLoggedIn(false);
    setFightersList([]);
    setFightsList([]);
  };

  const handleSignup = (token) => {
    console.log('Handling signup with token:', token);
    localStorage.setItem('token', token);
    setToken(token);
    setIsLoggedIn(true);
    fetchData(token);
  };

  const indexOfLastFighter = currentPage * itemsPerPage;
  const indexOfFirstFighter = indexOfLastFighter - itemsPerPage;
  const currentFighters = fightersList.slice(indexOfFirstFighter, indexOfLastFighter);
  const currentFights = fightsList.slice(indexOfFirstFighter, indexOfLastFighter);

  const handleFighterClick = (fighter) => {
    setSelectedFighter(fighter);
    setUpdateFighter(null);
  };

  const handleFightClick = (fight) => {
    setSelectedFight(fight);
    setUpdateFight(null);
  };

  const handleDeleteFighter = (fighterId) => {
    const isConfirmed = window.confirm('Are you sure you want to delete this fighter?');

    if (isConfirmed) {
      fetch(`${backendurl}/api/fighters/deleteFighter/${fighterId}`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
      .then(response => {
        if (!response.ok) {
          return response.json().then(error => {
            throw new Error(error.message || 'Network response was not ok');
          });
        }
        setFightersList(fightersList.filter(fighter => fighter._id !== fighterId));
        if (selectedFighter && selectedFighter._id === fighterId) {
          setSelectedFighter(null);
        }
        if (updateFighter && updateFighter._id === fighterId) {
          setUpdateFighter(null);
        }
      })
      .catch(error => console.error('Error deleting fighter:', error));
    }
  };

  const handleDeleteFight = (fightId) => {
    const isConfirmed = window.confirm('Are you sure you want to delete this fight?');

    if (isConfirmed) {
      fetch(`${backendurl}/api/fights/deleteFight/${fightId}`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
      .then(response => {
        if (!response.ok) {
          return response.json().then(error => {
            throw new Error(error.message || 'Network response was not ok');
          });
        }
        setFightsList(fightsList.filter(fight => fight._id !== fightId));
        if (selectedFight && selectedFight._id === fightId) {
          setSelectedFight(null);
        }
        if (updateFight && updateFight._id === fightId) {
          setUpdateFight(null);
        }
      })
      .catch(error => console.error('Error deleting fight:', error));
    }
  };

  const addFighter = (newFighter) => {
    fetch(`${backendurl}/api/fighters/addFighter`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(newFighter),
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(addedFighter => {
      setFightersList(prevFightersList => [...prevFightersList, addedFighter]);
    })
    .catch(error => console.error('Error adding fighter:', error));
  };

  const addFight = (newFight) => {
    fetch(`${backendurl}/api/fights/addFight`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(newFight),
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(addedFight => {
      setFightsList(prevFightsList => [...prevFightsList, addedFight]);
    })
    .catch(error => console.error('Error adding fight:', error));
  };

  const updateFighterEvent = (updatedFighter) => {
    fetch(`${backendurl}/api/fighters/updateFighter/${updatedFighter._id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(updatedFighter),
    })
    .then(response => {
      if (!response.ok) {
        return response.json().then(error => {
          throw new Error(error.message || 'Network response was not ok');
        });
      }
      return response.json();
    })
    .then(data => {
      const updatedFightersList = fightersList.map(fighter =>
        fighter._id === updatedFighter._id ? data : fighter
      );
      setFightersList(updatedFightersList);
      setSelectedFighter(null);
      setUpdateFighter(null);
    })
    .catch(error => console.error('Error updating fighter:', error));
  };

  const updateFightEvent = (updatedFight) => {
    fetch(`${backendurl}/api/fights/updateFight/${updatedFight._id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(updatedFight),
    })
    .then(response => {
      if (!response.ok) {
        return response.json().then(error => {
          throw new Error(error.message || 'Network response was not ok');
        });
      }
      return response.json();
    })
    .then(data => {
      const updatedFightsList = fightsList.map(fight =>
        fight._id === updatedFight._id ? data : fight
      );
      setFightsList(updatedFightsList);
      setSelectedFight(null);
      setUpdateFight(null);
    })
    .catch(error => console.error('Error updating fight:', error));
  };

  const sortFighters = (fighters) => {
    if (isSorted) {
      return [...fighters].sort((a, b) => a.age - b.age);
    } else {
      return [...fighters].sort((a, b) => b.age - a.age);
    }
  };

  const handleUpdateFighter = (fighter) => {
    setUpdateFighter(fighter);
  };

  const handleUpdateFight = (fight) => {
    setUpdateFight(fight);
  };

  const paginate = (pageNumber) => {
    setCurrentPage(pageNumber);
  };

  const handleSort = () => {
    setIsSorted(!isSorted);
    const sortedFighters = sortFighters(fightersList);
    setFightersList(sortedFighters);
  };

  const getFighterNameById = (id) => {
    console.log('Searching for fighter ID:', id); // Debug log
    const fighter = fightersList.find(f => f._id === id);
    console.log('Found fighter:', fighter); // Debug log
    return fighter ? fighter.name : 'Unknown';
  };

  return (
    <>
      {!internetStatus && handleErrorMessage('Internet connection is down.')}
      {!backendStatus && handleErrorMessage('Backend server is down.')}
      {isLoggedIn ? (
        <>
          <button onClick={handleLogout}>Logout</button>
          <FighterDoughnutChart fightersList={fightersList} />
          <button onClick={handleSort}>{isSorted ? 'Sort by Age' : 'Sort by Age'}</button>
          <div className="content">
            <div className="lists-container">
              <div className="list">
                <FighterList fightersList={currentFighters} handleClick={handleFighterClick} />
              </div>
              <div className="list">
                <FightList fightsList={currentFights} handleClick={handleFightClick} getFighterNameById={getFighterNameById} />
              </div>
            </div>
            <Pagination
              itemsPerPage={itemsPerPage}
              totalItems={fightersList.length}
              paginate={paginate}
            />
            <div className="forms-container">
              <div className="form">
                <AddFighterForm onAdd={addFighter} />
              </div>
              <div className="form">
                <AddFightForm onAdd={addFight} token={token} />
              </div>
            </div>
          </div>
          {selectedFighter && <FighterCard fighter={selectedFighter} handleUpdate={handleUpdateFighter} handleDelete={handleDeleteFighter} />}
          {selectedFight && <FightCard fight={selectedFight} handleUpdate={handleUpdateFight} handleDelete={handleDeleteFight} getFighterNameById={getFighterNameById} />}
          {updateFighter && <UpdateFighter onUpdateFighter={updateFighterEvent} fighter={updateFighter} />}
          {updateFight && <UpdateFightForm onUpdateFight={updateFightEvent} fight={updateFight} token={token} />}
        </>
      ) : (
        <>
          {showLogin ? (
            <>
              <LoginForm onLogin={handleLogin} />
              <p>Don't have an account? <button onClick={() => setShowLogin(false)}>Sign up</button></p>
            </>
          ) : (
            <>
              <SignupForm onSignup={handleSignup} />
              <p>Already have an account? <button onClick={() => setShowLogin(true)}>Login</button></p>
            </>
          )}
        </>
      )}
    </>
  );
}

const Pagination = ({ itemsPerPage, totalItems, paginate }) => {
  const pageNumbers = [];

  for (let i = 1; i <= Math.ceil(totalItems / itemsPerPage); i++) {
    pageNumbers.push(i);
  }

  return (
    <nav>
      <ul className="pagination">
        {pageNumbers.map(number => (
          <li key={number} className="page-item">
            <button onClick={() => paginate(number)} className="page-link">
              {number}
            </button>
          </li>
        ))}
      </ul>
    </nav>
  );
};

export default App;
