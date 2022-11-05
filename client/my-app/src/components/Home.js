import React from 'react';
import { useNavigate } from 'react-router-dom';
import "../style/home.css"

const Home = () => {

    const navigate = useNavigate();

  return (
    <div className="home-wrapper">
        <button onClick={() => navigate("/user")}>This is home. Go to user</button>
    </div>
  )
}

export default Home