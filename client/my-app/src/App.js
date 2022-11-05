import './style/App.css';
import React from 'react';
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom';

import User from './components/User';
import Home from './components/Home';
import ChangePassword from './components/ChangePassword';
import DeleteAccount from './components/DeleteAccount';
import ChangeLocation from './components/ChangeLocation';

const App = () => {
  return (
      <BrowserRouter>
          <Routes>
              <Route path="/" exact element={<Navigate to="/user" />} />
              <Route path="/user" exact element={<User/>} />
              <Route path="/home" exact element={<Home/>} />
              <Route path="/changePassword" exact element={<ChangePassword/>} />
              <Route path="/deleteAccount" exact element={<DeleteAccount/>} />
              <Route path="/changeLocation" exact element={<ChangeLocation/>} />
          </Routes>
      </BrowserRouter>
  )
}

export default App;