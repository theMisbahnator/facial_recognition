import React from 'react'

const User = ({id, name, song_title, yt_url, last_updated, date_created}) => {
  return (
    <span>
        <div>Name: {name}</div>
        <div>Song Title: {song_title}</div>
        <div>yt_url: {yt_url}</div>
        <div>last_updated: {last_updated}</div>
        <div>Date Created: {date_created}</div>
    </span>
  )
}

export default User