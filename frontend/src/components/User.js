import axios from "axios"; 
import React, { useState } from 'react'
import "../index"
import { FcFullTrash } from "react-icons/fc";

const User = ({id, name, song_title, yt_url, img_url, last_updated, date_created}) => {
    const [url, setUrl] = useState("");

  return (
    <span>
        <div class="card bg-light mb-3 cardSize">
            <div className="container">
                <div class="row">
                    <div class="col-5">
                        <img class=" userImg" src={img_url} alt="user headshot"></img> 
                    </div>
                    <div class="col-7 test">
                        <p class="display-6 name">{name}</p>
                        <a href={yt_url} target="_blank"><p className="display-7">{song_title}</p></a>
                        <p className="container">
                            <div className="row justify-content-around">
                                <button type="button" class="btn btn-warning col-3">Edit 📝</button>
                                <button type="button" class="btn btn-danger col-3">Delete <FcFullTrash/></button>
                            </div>
                        </p>
                        <div class="card creation-details">
                        <p className="container">
                            <div className="row date-holder">
                                <small class="text-muted col dates">Last updated: {last_updated}</small>
                                <small class="text-muted col dates">Date Created: {date_created}</small>
                            </div>
                        </p>
                    </div>
                    </div>
                </div>
            </div>
        </div>
    </span>
  )
}

export default User