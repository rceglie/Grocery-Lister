import axios from 'axios';
import React, {useState} from 'react';
import { useNavigate } from 'react-router-dom';
import "../style/item.css"

const Item = ({data}) => {

    const navigate = useNavigate();
    const [er, setEr] = useState("");

    const signOut = () => {
        console.log("hi")
    }
  
    const addToList = () => {
      axios.post('http://127.0.0.1:5000/add_to_list',
      {
        uid: localStorage.getItem("uid"),
        pid: data[0]
      }
      ).then(function (response) {
        console.log(response.data);
        if (response.data != "error"){
          setEr("")
        } else {
          setEr("Could not add to list.");
        }
      })
    }

  return (
    <div className="result">
      <h3>{data[1]}</h3>
      <h4 className="storeName">{data[8]}</h4>
      <div className="user-wrapper">
        <div>
          <a href={data[4]}>
            <img src={data[3]} className="itemPic"/>
          </a>
        </div>
        <div className="itemInfo">
          <h4>Price: </h4><p>${data[2]}</p>
          <h4>Location Info: </h4>
          <p>{data[7]}</p>
          <p>{data[9]}</p>
        </div>
        <div className="addTo">
          <button className="btn" onClick={() => addToList()}>Add to List</button>
          <p>{er}</p>
        </div>
      </div>
    </div>
  )
}

export default Item