import React from 'react';
import { useNavigate } from 'react-router-dom';
import "../style/item.css"

const Item = ({data}) => {

    const navigate = useNavigate();

    const signOut = () => {
        console.log("hi")
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
          <button className="btn">Add to List</button>
        </div>
      </div>
    </div>
  )
}

export default Item