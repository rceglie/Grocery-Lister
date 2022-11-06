import React, {useState} from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const SignUp = () => {

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

    axios.post('http://127.0.0.1:5000/signup',
      {
        uid:1,
        oldpass: oldPassword,
        newpass: newPassword1,

      }
      ).then(function (response) {
        console.log(response.data);
        //setErrorMessage(response.data);
      })
  }

  return (
    <div className="home-wrapper">
      <form onSubmit={handleSubmit}>
        <label htmlFor="a">Name:</label>
        <input type="text" id="a" name="a" value={nname} onChange={(e) => setNName(e.target.value)}/>
        <label htmlFor="b">Username:</label>
        <input type="text" id="b" name="b" value={username} onChange={(e) => setUsername(e.target.value)}/>
        <label htmlFor="c">Password:</label>
        <input type="text" id="c" name="c" value={password} onChange={(e) => setPassword(e.target.value)}/>
        <label htmlFor="d">Repeat Password:</label>
        <input type="text" id="d" name="d" value={password2} onChange={(e) => setPassword2(e.target.value)}/>
        <label htmlFor="e">Location:</label>
        <input type="text" id="e" name="e" value={location} onChange={(e) => setLocation(e.target.value)}/>
        <input type="submit"/>
        <p>{errorMessage}</p>
      </form>
        <button onClick={() => navigate("/user")}>Back</button>
    </div>
  )
}

export default SignUp