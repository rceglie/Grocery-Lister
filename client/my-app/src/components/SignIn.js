import React, {useState} from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const SignIn = () => {

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [er, setEr] = useState("");

  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();

    axios.post('http://127.0.0.1:5000/sign_in',
      {
        username: username,
        password: password
      }
      ).then(function (response) {
        console.log(response.data)
        if (response.data != "error"){
            localStorage.setItem("uid", response.data)
            navigate("/home")
        } else {
            setEr("There was a problem logging in. Make sure your username and password are correct.")
        }
      })
  }

  return (
    <div className="home-wrapper">
        <form onSubmit={handleSubmit}>
            <label htmlFor="a"></label>
            <input type="text" placeholder="username" id="a" name="a" value={username} onChange={(e) => setUsername(e.target.value)}/>
            <label htmlFor="b"></label>
            <input type="password" id="b" placeholder="password" name="b" value={password} onChange={(e) => setPassword(e.target.value)}/>
            <input type="submit"/>
        </form>
        <button onClick={() => navigate("/signup")}>Sign up</button>
        <button onClick={() => navigate("/user")}>Back</button>
        <p>{er}</p>
    </div>
  )
}

export default SignIn