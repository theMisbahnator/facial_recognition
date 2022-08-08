import React from 'react'
import User from './User'
import AddUser from './AddUser';
import "../index"

const UserList = ({users, setUsers}) => {
  return (
    <div>
        <div className ="scrollable-div-list scrollable-div card-deck">
            {users.map(userDetails => (
                <User
                    id = {userDetails["id"]}
                    name = {userDetails["name"]}
                    song_title = {userDetails["song_title"]}
                    yt_url = {userDetails["youtube_url"]}
                    file_name = {userDetails["img_fn"]}
                    last_updated = {userDetails["last_updated"]}
                    date_created = {userDetails["date_created"]}
                />
            ))
            }
        </div>
    </div>
  )
}

export default UserList