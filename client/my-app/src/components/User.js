import React from 'react';
import { useNavigate } from 'react-router-dom';
import "../style/user.css"

const User = () => {

    const navigate = useNavigate();

    const signOut = () => {
        console.log("hi")
    }

    

  return (
    <div className="body">
      <div className="user-wrapper">
        <div className="banner"></div>
        <div className="userInfo">
          <h3>Account settings</h3>
          <div className="buttons">
            <button onClick={() => navigate("/changePassword")}>Change password</button>
            <button onClick={() => navigate("/changeLocation")}>Change location</button>
            <button onClick={signOut}>Sign out</button>
            <p> </p>
            <p> </p>
            <p> </p>
            <p> </p>
            <button onClick={() => navigate("/deleteAccount")}>Delete account</button>
          </div>
        </div>
        <div className="nav">
          <button onClick={() => navigate("/home")}> Back to home </button>
        </div>
      </div>
    </div>
  )
}

export default User