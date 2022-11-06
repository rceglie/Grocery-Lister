import React, {useState, useEffect} from 'react';
import { useNavigate } from 'react-router-dom';
import "../style/user.css"
import ListItem from './ListItem.js'
import axios from 'axios';

const List = (props) => {
    
    const [results, setResults] = useState([])
    const navigate = useNavigate();
    
    let uid = localStorage.getItem('uid')
    
    useEffect(() => {
        axios.post('http://127.0.0.1:5000/getlist',
            {
                uid: uid
            }
        ).then(function (response) {
            setResults(response.data)
        })
    }, [])

    return (
        <div>
            {results.length > 0 ? results.map((e, index) => {
                return (
                    <ListItem data={e} key={index}/>
                );
              }) : 
                <div>
                    <p>Your list is empty.</p>
                </div>  
            }
        </div>
    )
}

export default List