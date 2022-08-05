import React, { useEffect } from 'react'
import AddUser from '../components/AddUser';
import UserList from '../components/UserList';
import '../index'
import johnCena from "../johny.webp";
import axios from "axios"; 

const Dashboard = () => {
    useEffect(() => {
        axios
        .get('http://127.0.0.1:5000/users')
        .then((response) => {
            console.log(response.data);
        })
        .catch((err) => {
            console.log(err); 
        });
    }, []); 

  return (
    <div>
        <nav className="navbar navbar-dark bg-primary">
            <span className="navbar-brand mb-0 h1 navbar-johncena">
                <span className="display-4">John Cena!</span>
                <span className="container"><img className ="johncena" alt="john cena" src={johnCena}></img></span>
                <div>Created By Misbah Imtiaz</div>
            </span>
        </nav>
        <div className="form-container">
            <div className="reg-users-title">
                <h2 className="display-5">Registered Users</h2>
                <div className="search-quote">Wanna enter a Room in Style?</div>
                <div className ="flex">
                    <input className="form-control mr-sm-2" type="text" placeholder="Enter a name..." aria-label="Search"></input>
                    <AddUser/>
                </div>
            </div>
        </div>
        <UserList/>
    </div>
  )
}

export default Dashboard