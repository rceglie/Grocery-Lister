import React, {useState, useEffect} from 'react';
import { useNavigate } from 'react-router-dom';
import "../style/home.css"
import ListItem from './ListItem.js'
import axios from 'axios';

function List() {
    
    const [results, setResults] = useState([]);
    const navigate = useNavigate();

    // const remove = (pid) => {
    //     axios.post('http://127.0.0.1:5000/remove_from_list',
    //         {
    //             uid: localStorage.getItem("uid"),
    //             pid: pid
    //         }
    //     ).then(() => {
    //         navigate("/list")
    //     })
    // }
    // const remove = () => {}
    // const updateList = () => {}

    // useEffect(() => {
    //     axios
    //         .post('http://127.0.0.1:5000/get_list', {uid: localStorage.getItem("uid")})
    //         .then((res) => {
    //             setResults(res.data)
    //         })
    // })

    // const updateList = () => {
    //     axios.post('http://127.0.0.1:5000/get_list',
    //         {
    //             uid: localStorage.getItem("uid")
    //         }
    //         ).then(function(response) {
    //             setResults({"list": response.data}, function () {
    //                 console.log(results)
    //             })
    //         })
    // }

    useEffect(() => {
        getData()
    }, [])

    useEffect(() => {
        console.log(results)
    })

    const getData = async() => {
        const response = await axios.post('http://127.0.0.1:5000/get_list', {uid: 4})
        setResults(await response.data)
    }

    return (
        <div>
            <p>{results}</p>
            {results.map((e, index) => {
                return (
                    <p>{index}</p>
                );
              })
            }
        </div>
    )
}

export default List