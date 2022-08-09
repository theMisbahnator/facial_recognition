import React, { useEffect } from 'react'
import User from './User'
import AddUser from './AddUser';
import "../index"

const UserList = ({users, setUsers, message}) => {

    useEffect(() => {
        console.log(message); 
    }, [message]); 

    const meetsSearch = (userName) => {
        if (message === "") {return true; }
        return userName.includes(message);
    }

  return (
    <div>
        <div className ="scrollable-div-list scrollable-div card-deck">
            {users.map(userDetails => (
                meetsSearch(userDetails["name"]) ? (
                <User
                    id = {userDetails["id"]}
                    name = {userDetails["name"]}
                    song_title = {userDetails["song_title"]}
                    yt_url = {userDetails["youtube_url"]}
                    img_url= {userDetails["img_url"]}
                    last_updated = {userDetails["last_updated"]}
                    date_created = {userDetails["date_created"]}
                />
                ) : null
            ))
            }
        </div>
    </div>
  )
}

export default UserList