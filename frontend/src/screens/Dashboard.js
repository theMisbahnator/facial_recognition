import React, { useEffect, useState } from 'react'
import AddUser from '../components/AddUser';
import UserList from '../components/UserList';
import '../index'
import axios from "axios"; 
import NavBar from '../components/NavBar';



const Dashboard = () => {
    const [users, setUsers] = useState([]); 
    const [message, setMessage] = useState('');

    const handleMessageChange = event => {
        setMessage(event.target.value);
    };

    useEffect(() => {
        axios
        .get('http://127.0.0.1:5000/users')
        .then((response) => {
            console.log(response.data);
            setUsers(JSON.parse(response.data)); 
        })
        .catch((err) => {
            console.log(err); 
        });
    }, []); 


  return (
    <div>
        <NavBar/>
        <div className="form-container">
            <div className="reg-users-title">
                <h2 className="display-5">Registered Users</h2>
                <div className="search-quote">Wanna enter a Room in Style?</div>
                <div className ="flex">
                    <input className="form-control mr-sm-2" type="text" placeholder="Enter a name..." aria-label="Search" onChange={handleMessageChange}></input>
                    <AddUser/>
                </div>
            </div>
        </div>
        <UserList users={users} setUsers = {setUsers} message = {message}/>
    </div>
  )
}

export default Dashboard