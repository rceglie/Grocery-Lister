import React from 'react';
import { useNavigate } from 'react-router-dom';

const DeleteAccount = () => {

    const navigate = useNavigate();

  return (
    <div className="home-wrapper">
        <button onClick={() => navigate("/user")}>This is home. Go to user</button>
    </div>
  )
}

export default DeleteAccount