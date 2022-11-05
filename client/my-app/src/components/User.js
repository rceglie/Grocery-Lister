import React from 'react';
import { useNavigate } from 'react-router-dom';
import "../style/user.css"

const User = () => {

    const navigate = useNavigate();

    const signOut = () => {
        console.log("hi")
    }

  return (
    <div className="user-wrapper">
        <button onClick={() => navigate("/changePassword")}>Change password</button>
        <button onClick={() => navigate("/changeLocation")}>Change location</button>
        <button onClick={signOut}>Sign out</button>
        <button onClick={() => navigate("/deleteAccount")}>Delete account</button>
    </div>
  )
}

export default User