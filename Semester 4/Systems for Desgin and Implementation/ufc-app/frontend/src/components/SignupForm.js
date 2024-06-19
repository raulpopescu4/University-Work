import React, { useState } from 'react';

const SignupForm = ({ onSignup }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const backendurl =  'https://nameless-reaches-91634-e6ccf185c907.herokuapp.com' //'https://nameless-reaches-91634-e6ccf185c907.herokuapp.com';

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch(`${backendurl}/api/auth/signup`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    })
    .then(response => response.json())
    .then(data => {
      if (data.token) {
        onSignup(data.token);
      } else {
        console.error('Signup failed');
      }
    })
    .catch(error => console.error('Error during signup:', error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        required
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
      />
      <button type="submit">Sign up</button>
    </form>
  );
};

export default SignupForm;
