import React, {useState} from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const SignUp = () => {

  const [nname, setNName] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [password2, setPassword2] = useState("");
  const [er, setEr] = useState("");

  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();

    if (password !== password2){
      setEr("Make sure passwords match");
    } else {
      axios.post('http://127.0.0.1:5000/sign_up',
      {
        username: username,
        name: nname,
        password: password
      }
      ).then(function (response) {
        console.log(response.data);
        if (response.data != "error"){
          navigate("/changeLocation")
        } else {
          setEr("Could not create account.");
        }
      })
    }

    
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
        <input type="submit"/>
        <p>{er}</p>
      </form>
        <button onClick={() => navigate("/home")}>Back</button>
    </div>
  )
}

export default SignUp