import React, {useState} from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const ChangePassword = () => {

  const [oldPassword, setOldPassword] = useState("");
  const [newPassword1, setNewPassword1] = useState("");
  const [newPassword2, setNewPassword2] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    if (newPassword1 !== newPassword2){
      setErrorMessage("Make sure new passwords match");
    }

    axios.post('http://127.0.0.1:5000/change_password',
      {
        uid:1,
        oldpass: oldPassword,
        newpass: newPassword1
      }
      ).then(function (response) {
        console.log(response.data);
        //setErrorMessage(response.data);
      })
  }

  return (
    <div className="home-wrapper">
      <form onSubmit={handleSubmit}>
        <label htmlFor="a">Old Password:</label>
        <input type="text" id="a" name="a" value={oldPassword} onChange={(e) => setOldPassword(e.target.value)}/>
        <label htmlFor="b">New Password:</label>
        <input type="text" id="b" name="b" value={newPassword1} onChange={(e) => setNewPassword1(e.target.value)}/>
        <label htmlFor="c">Repeat New Password:</label>
        <input type="text" id="c" name="c" value={newPassword2} onChange={(e) => setNewPassword2(e.target.value)}/>
        <input type="submit"/>
        <p>{errorMessage}</p>
      </form>
        <button onClick={() => navigate("/user")}>Back</button>
    </div>
  )
}

export default ChangePassword