import axios from "axios"; 
import React, { useState } from 'react'

const User = ({id, name, song_title, yt_url, file_name, last_updated, date_created}) => {
    const [url, setUrl] = useState("");
    
    const getImgSrc = file_name => {
        axios
        .get(`http://127.0.0.1:5000/img/${file_name}`)
        .then((response) => {
            let url = response.data["imgFileUrl"]; 
            setUrl(url); 
        })
        .catch((err) => {
            console.log(err);
        });
    }

    const getUrl = (file_name) => {
        getImgSrc(file_name); 
        return url; 
    }

  return (
    <span>
        <div>Name: {name}</div>
        <div>Song Title: {song_title}</div>
        <div>yt_url: {yt_url}</div>
        <div>last_updated: {last_updated}</div>
        <div>Date Created: {date_created}</div>
        <img alt='user_img' src={getUrl(file_name)}></img>
    </span>
  )
}

export default User