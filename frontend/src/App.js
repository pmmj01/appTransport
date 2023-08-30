import React from 'react';
// import { createRoot } from "react-dom/client"
import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';
import AdminLoginForm from './components/login';
import RegistrationForm from './components/registrationDriverForm';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path='/'>
          <Route path='admin/' Component={AdminLoginForm} />
          <Route path='register-driver/' Component={RegistrationForm} />
        </Route>
      </Routes>
    </Router>
  );
};

// const container = document.getElementById("app");
// const root = createRoot(container);
// root.render(<App/>);

export default App;
