import React, { useState } from 'react'
import { FcFullTrash } from "react-icons/fc";
import { GrClose } from "react-icons/gr";
import { FcHighPriority } from "react-icons/fc"
import "../index"
import Modal from 'react-modal';
import axios from "axios"; 

const DeleteUser = ({name, id, deleteState, setDeleteState, users, setUsers}) => {
    
    const handleClose = () => {
        setDeleteState(false); 
    }

    const handleDelete = () => {
        // make a request to delete
        axios
        .delete(`http://127.0.0.1:5000/user/${id}`)
        .then((response) => {
            console.log(response); 
        })
        .catch((err) => {
            console.log(err); 
        });

        // the list is updated by filering out this user by id 
        const newUsers = users.filter(parseId);

        // set the users to the new filtered list
        setUsers(newUsers); 

        handleClose(); 
    }

    function parseId(user) {
        return user["id"] !== id;  
      }

  return (
    <div>
        <Modal className="delete-modal border border-danger" isOpen={deleteState} onRequestClose={() => {setDeleteState(false)}}>
            <div className='content-form'>
                <div>
                    <FcHighPriority className='remove-icon' size={100} />
                </div>
                <div className='display-4 text-muted'>
                    Are you sure?
                </div>
                <p className='text-muted'>Do you really want to delete <b>{name}</b>?</p>
                <br/>

                <p className="container">
                    <div className="row justify-content-around">
                        <button className="btn btn-secondary col-4" onClick={() => {handleClose()}}>Cancel</button>
                        <button className="btn btn-danger col-4" onClick={() => {handleDelete()}}>Delete!</button>
                    </div>
                </p>

            </div>
        </Modal>
    </div>
  )
}

export default DeleteUser