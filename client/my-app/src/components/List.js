import React, {useState, useEffect} from 'react';
import { useNavigate } from 'react-router-dom';
import "../style/home.css"
import ListItem from './ListItem.js'
import axios from 'axios';

function List() {
    
    const [content, setContent] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        axios.post('http://127.0.0.1:5000/get_list',
            {
                uid: localStorage.getItem("uid")
            }
            ).then((res) => {
                console.log(res)
                setContent(res.data)
            })
    }, [])

    const remove1 = (pid) => {
        console.log(pid)
        let temp = content.slice()
        let index = -1
        temp.forEach((item, i) => {
            if (item[1] == pid){
                index = i
            }
        })
        temp.splice(index, 1)
        setContent(temp)
    }

    const remove = (pid) => {
        console.log("doing something")
        axios.post('http://127.0.0.1:5000/remove_from_list',
            {
                uid: localStorage.getItem("uid"),
                pid: pid
            }
        ).then(() => {
            axios.post('http://127.0.0.1:5000/get_list',
            {
                uid: localStorage.getItem("uid")
            }
            ).then((res) => {
                console.log(res)
                setContent(res.data)
            })
        })
    }

    return (
        <div>
            {content.map((e, index) => {
                return (
                    <ListItem data={e} remove={remove} key={index}/>
                );
              })
            }
        </div>
    )
}

export default List