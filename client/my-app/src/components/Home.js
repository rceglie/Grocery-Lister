import React, {useState, useEffect} from 'react';
import { useNavigate } from 'react-router-dom';
import "../style/home.css"
import Item from './Item.js';
import axios from 'axios';

const Home = () => {
  const navigate = useNavigate();
  const [stores, setStores] = useState({"Walmart":true, "Trader Joe's":true, "Harris Teeter":true, "Wegmans":true, "Aldi":true});
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [range, setRange] = useState(5);
  const [errorMessage, setErrorMessage] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault()

    let exclude = []
    Object.entries(stores).map(([key, value]) => {
      if (!value){
        exclude.push(key)
      }
    })
    if (exclude.length == 0) {
      exclude = [""]
    }

    axios.post('http://127.0.0.1:5000/searchquerylowest',
      {
        query: query.toLowerCase(),
        exclude: exclude,
        range: range,
        uid: JSON.parse(localStorage.getItem("uid"))
      }
      ).then(function (response) {
        setResults(response.data)
        console.log(response.data);
        if (response.data.length == 0) {
          setErrorMessage("No results found. Try another search.")
        }
      })
  }

  useEffect (() => {
    //console.log(stores)
    //<img src="../../../public/images/noresults.png"/>
  })

  return (
    <div className="body">
        <header>
          <div className = "siteName">
            <h1>name</h1>
          </div>
          <div className="shopList">
            <button onClick={() => navigate("/list")}>My Shopping List</button>
          </div>
        </header>

        <div className="flex-container">
          <div className="filter-container">
            <h3>Filter Search Results</h3>
            <h4>Store:</h4>
            <input type="checkbox" id="store0" name="store0" checked={stores["Aldi"]} onChange={(e) => {
              setStores({...stores, "Aldi":!stores["Aldi"]})
            }}/>
            <label htmlFor="store0">Aldi</label><br/>
            <input type="checkbox" id="store1" name="store1" checked={stores["Harris Teeter"]} onChange={(e) => {
              setStores({...stores, "Harris Teeter":!stores["Harris Teeter"]})
            }}/>
            <label htmlFor="store1">Harris Teeter</label><br/>
            <input type="checkbox" id="store2" name="store2" checked={stores["Walmart"]} onChange={(e) => {
              setStores({...stores, "Walmart":!stores["Walmart"]})
            }}/>
            <label htmlFor="store3">Walmart</label><br/>
            <input type="checkbox" id="store2" name="store2" checked={stores["Trader Joe's"]} onChange={(e) => {
              setStores({...stores, "Trader Joe's":!stores["Trader Joe's"]})
            }}/>
            <label htmlFor="store4">Trader Joe's</label><br/>
            <input type="checkbox" id="store4" name="store4" checked={stores["Wegmans"]} onChange={(e) => {
              setStores({...stores, "Wegmans":!stores["Wegmans"]})
            }}/>
            <label htmlFor="store5">Wegmans</label><br/>
            
            <h4>Distance (miles):</h4>
            <div className="slidecontainer">
                <div className="distLabels">
                  <p>5</p>
                  <p>10</p>
                  <p>15</p>
                  <p>20</p>
                </div>
                <input type="range" min="5" max="20" step="5" className="slider" id="myRange" value={range} onChange={(e) => setRange(e.target.value)}/>
            </div>  

            <button onClick={handleSubmit} className="filterBtn">Apply Filters</button>
          </div>

          <div className="container">
            <form className="search-bar" onSubmit={handleSubmit}> 
              <input type="text" id="query" value={query} name="q" placeholder="Search for a product"
                onChange={(e) => setQuery(e.target.value)}/>
              <button type="submit"><img src='../../public/images/search.png'/></button>
            </form>

            <div>
              {results.length > 0 ? results.map((e, index) => {
                return (
                  <Item data={e} key={index}/>
                );
              }) : 
                  <div>
                    <p>{errorMessage}</p>
                  </div>  
                }
            </div>
          </div>
        </div>
      </div>

  )
}

export default Home