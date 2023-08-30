import axios from 'axios';
import React, { useEffect, useState } from 'react';

function RegistrationForm() {
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    phone_number: '',
    driver_license: '',
    email: '',
    password: '',
  });
  const [csrfToken, setCsrfToken] = useState('');

  const getCsrfToken = () => {
    const csrfCookie = document.cookie.match(/csrftoken=([^;]*)/);
    return csrfCookie ? csrfCookie[1] : null;
  };
  useEffect(() => {
    setCsrfToken(getCsrfToken());
  }, []);

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/register-driver/', {
        headers: {
          'X-CSRFToken': csrfToken,
        },
      });
      if (response.status === 200) {
        console.log(
          `Konto utworzone ${formData.first_name + formData.last_name}`
        );
      }
    } catch (error) {
      console.error(error);
      console.log(error);
      console.log(formData);
      console.log(
        `nie udało się ;( ${formData.first_name + formData.last_name}`
      );
    }
  };

  return (
    <div>
      <h2>Rejestracja kierowcy</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor='first_name'>Imię:</label>
        <input
          type='text'
          name='first_name'
          value={formData.first_name}
          onChange={handleInputChange}
          required
        />
        <br />

        <label htmlFor='last_name'>Nazwisko:</label>
        <input
          type='text'
          name='last_name'
          value={formData.last_name}
          onChange={handleInputChange}
          required
        />
        <br />

        <label htmlFor='phone_number'>Numer telefonu:</label>
        <input
          type='tel'
          name='phone_number'
          value={formData.phone_number}
          onChange={handleInputChange}
          required
        />
        <br />

        <label htmlFor='driver_license'>Prawo jazdy:</label>
        <select
          name='driver_license'
          value={formData.driver_license}
          onChange={handleInputChange}
        >
          <option value=''>Wybierz rodzaj prawa jazdy</option>
          <option value='C'>C</option>
          <option value='C+E'>C+E</option>
          {/* Dodaj więcej opcji tutaj */}
        </select>
        <br />

        <label htmlFor='email'>Email:</label>
        <input
          type='text'
          name='email'
          value={formData.email}
          onChange={handleInputChange}
          required
        />
        <br />

        <label htmlFor='password'>Hasło:</label>
        <input
          type='password'
          name='password'
          value={formData.password}
          onChange={handleInputChange}
          required
        />
        <br />

        <input type='submit' value='Zarejestruj' />
      </form>
    </div>
  );
}

export default RegistrationForm;
