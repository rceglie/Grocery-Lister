import React, {useState} from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const ChangeLocation = () => {

  const [street, setStreet] = useState("");
  const [city, setCity] = useState("");
  const [state, setState] = useState("");
  const [zip, setZip] = useState(0);
  const [er, setEr] = useState("");

  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();

    axios.post('http://127.0.0.1:5000/change_address',
    {
      uid: localStorage.getItem("uid"),
      street: street,
      city: city,
      state: state + " " + String(zip)
    }
    ).then(function (response) {
      console.log(response.data);
      if (response.data != "error"){
        navigate("/home")
      } else {
        setEr("Could not set location.");
      }
    })
    

    
  }

  return (
    <div className="home-wrapper">
      <form onSubmit={handleSubmit}>
        <label htmlFor="a">Street Address:</label>
        <input type="text" id="a" name="a" value={street} onChange={(e) => setStreet(e.target.value)}/>
        <label htmlFor="b">City:</label>
        <input type="text" id="b" name="b" value={city} onChange={(e) => setCity(e.target.value)}/>
        <label htmlFor="c">State:</label>
        <input type="text" id="c" name="c" value={state} onChange={(e) => setState(e.target.value)}/>
        <label htmlFor="d">Zip Code:</label>
        <input type="number" id="d" name="d" max="99999" value={zip} onChange={(e) => setZip(e.target.value)}/>
        <input type="submit"/>
        <p>{er}</p>
      </form>
    </div>
  )
}

export default ChangeLocation