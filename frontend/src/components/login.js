import axios from 'axios';
import React, { useEffect, useState } from 'react';

const AdminLoginForm = () => {
  const [phone_number, setPhone_number] = useState('');
  const [password, setPassword] = useState('');
  const [csrfToken, setCsrfToken] = useState('');

  const getCsrfToken = () => {
    const csrfCookie = document.cookie.match(/csrftoken=([^;]*)/);
    return csrfCookie ? csrfCookie[1] : null;
  };

  useEffect(() => {
    setCsrfToken(getCsrfToken());
  }, []);

  const handleUsernameChange = (e) => {
    setPhone_number(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post(
        '/admin/login',
        {
          phone_number,
          password,
        },
        {
          headers: {
            'X-CSRFToken': csrfToken,
          },
        }
      );

      if (response.status === 200) {
        console.log(`Zalogowano admin ${phone_number}`);
        console.log(response.data.email);
        console.log(response.data.phone_number);
        console.log(response.data.driver_license);

        console.log(phone_number);
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleLogin}>
      <div>
        <label>Phone number:</label>
        <input
          type='text'
          value={phone_number}
          onChange={handleUsernameChange}
        />
      </div>
      <div>
        <label>Password:</label>
        <input
          type='password'
          value={password}
          onChange={handlePasswordChange}
        />
      </div>
      <button type='submit'>Zaloguj</button>
    </form>
  );
};

export default AdminLoginForm;
