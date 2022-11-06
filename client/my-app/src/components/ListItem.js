import React from 'react';
import { useNavigate } from 'react-router-dom';

const ListItem = ({data, remove}) => {

    const navigate = useNavigate();

  return (
    <div className="result">
      <h3>{data[1]}</h3>
      <h4 className="storeName">{data[8]}</h4>
      <div className="user-wrapper">
        <div>
          <a href={data[4]}>
            <img src={data[6]} className="itemPic"/>
          </a>
        </div>
        <div className="itemInfo">
          <h4>Price: </h4><p>${data[5]}</p>
          <h4>Location Info: </h4>
          <p>{data[7]}</p>
          <p>{data[9]}</p>
        </div>
        <div className="addTo">
          <button className="btn">Remove From List</button>
        </div>
      </div>
    </div>
  )
}

export default ListItem