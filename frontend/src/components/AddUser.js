import React, { useState } from 'react'
import { FcPlus } from "react-icons/fc";
import { GrClose } from "react-icons/gr";
import axios from "axios"; 

import '../index'
import Modal from 'react-modal';

Modal.setAppElement("#root"); 
const AddUser = ({users, setUsers}) => {
    const [isOpen, setIsOpen] = useState(false);
    const [loading, setLoading] = useState(false); 
    const [nameErr, setNameErr] = useState("");
    const [linkErr, setLinkErr] = useState("");
    const [fileErr, setFileErr] = useState("");
    const [file, setFile] = useState();

    const updateFile = (e) => {
        let files = e.target.files; 
        setFile(files[0]); 
    }

    const handleSumbit = () => {
        resetFields(); 
        let name = document.getElementById('nameForm').value;
        let ytLink = document.getElementById('linkForm').value;

        let inputFail = name === "" || ytLink === "" || typeof file === "undefined"; 
        if (name === "") {
            setNameErr("Required");
        } else if (name.length > 20) {
            setNameErr("Character Limit Exceeded, below 20.");
            inputFail = true; 
        }

        if (ytLink === "") {
            setLinkErr("Required");
        } else if (!linkIsValid(ytLink)) {
            // check if link is valid here
            setLinkErr("Invalid Youtube Link.");
            inputFail = true; 
        } 

        console.log(file);
        if (typeof file === "undefined") {
            setFileErr("Required");
        }

        if (inputFail) {
            return; 
        }

        let reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = (e) => {
            let b64Image = e.target.result.replace('data:image/jpeg;base64,',''); 

            // make request to server to create user
            axios.post('http://127.0.0.1:5000/create-user', {
                imgData: b64Image,
                userName: name,
                url : ytLink
              })
              .then(function (response) {
                handleNewUser(response.data["userID"]); 
                setLoading(false); 
              })
              .catch(function (error) {
                console.log(error);
              });
              
        };

        handleClose(); 
        setLoading(true); 
    }

    const handleNewUser = userID => {
        // make a get request to get this users data
        axios
        .get(`http://127.0.0.1:5000/user/${userID}`)
        .then((response) => {
            let userData = JSON.parse(response.data)[0]; 
            let newUsers = [...users];
            newUsers.unshift(userData); 
            setUsers(newUsers); 
        })
        .catch((err) => {
            console.log(err); 
        });
    }

    const linkIsValid = (url) => {
        if (url != undefined || url != '') {
            let regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=|\?v=)([^#\&\?]*).*/;
            let match = url.match(regExp);
            if (match && match[2].length == 11) {
                return true; 
            }
            else {
                return false; 
            }
        }
    }

    const handleClose = () => {
        setIsOpen(false); 
        resetFields();  
        setFile();
    }

    const resetFields = () => {
        setNameErr(""); 
        setLinkErr(""); 
        setFileErr("");
    }

  return (
    <div>
        <FcPlus className="adduser" size={50} onClick={()=>{setIsOpen(true)}}/>

        <Modal className="add-modal" isOpen={isOpen} onRequestClose={() => {setIsOpen(false)}}>
            <div className='content-form'>
                <div className='close-form'>
                    <button className="close-button" onClick={() => {handleClose()}}><GrClose/></button>
                </div>
                <div className='display-4 title-form text-muted'>
                    Add User
                </div>

                <div className='form-elem'>
                    {/* <label for="nameForm">Name</label> */}
                    <input id ="nameForm" className ="form-control" type="text" placeholder='Enter a name...'></input>
                    <div className='text-danger'>{nameErr}</div>
                </div>
                
                <div className='form-elem'>
                    {/* <label for="linkForm">Link</label> */}
                    <input id ="linkForm" className ="form-control" type="text" placeholder='Paste link from Youtube...'></input>
                    <div className='text-danger'>{linkErr}</div>
                </div>
               
                <div className='form-elem'>
                    <label className = "text-muted" for="fileForm">Face Photo</label>
                    <input id ="fileForm" className ="form-control" type="file" onChange={(e) => {updateFile(e)}} placeholder='Upload a photo of yourself...'></input>
                    <div className='text-danger'>{fileErr}</div>
                </div>
                
                <div className='submit-form'>
                    <button type="button" class="btn btn-success" onClick={()=> {handleSumbit()}}>Create!</button>
                </div>
            </div>
        </Modal>


        <Modal className = "load-modal border border-success" isOpen={loading}>
            <div className='content-form'>
                <div class="spinner-border spinner-border-lg text-success dates" role="status" aria-hidden="true"></div>
                <div className='display-6'>Creating User...</div>
                <p className='text-muted'>Currently adding meta data, images, and mp3 files to AWS and PostgreSQL servers.</p>
                <b>Please do not refresh!</b>
            </div>
            
        </Modal>
        
        
    </div>
  )
}

export default AddUser