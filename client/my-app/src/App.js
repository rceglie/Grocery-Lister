import './style/App.css';
import React from 'react';
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom';

import User from './components/User';
import Home from './components/Home';
import ChangePassword from './components/ChangePassword';
import DeleteAccount from './components/DeleteAccount';
import ChangeLocation from './components/ChangeLocation';
import List from './components/List';
import SignIn from './components/SignIn';
import SignUp from './components/SignUp';
import Arr from './components/Arr';

const App = () => {
  return (
      <BrowserRouter>
          <Routes>
              <Route path="/" exact element={<Navigate to="/home" />} />
              <Route path="/user" exact element={<User/>} />
              <Route path="/home" exact element={<Home/>} />
              <Route path="/changePassword" exact element={<ChangePassword/>} />
              <Route path="/deleteAccount" exact element={<DeleteAccount/>} />
              <Route path="/changeLocation" exact element={<ChangeLocation/>} />
              <Route path="/list" exact element={<List/>} />
              <Route path="/signin" exact element={<SignIn/>} />
              <Route path="/signup" exact element={<SignUp/>} />
              <Route path="/listreload" exact element={<Arr />} />
          </Routes>
      </BrowserRouter>
  )
}

export default App;