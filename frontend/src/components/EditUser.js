import React, { useState } from 'react'
import "../index"
import Modal from 'react-modal';
import { GrClose } from "react-icons/gr";
import axios from "axios"; 

const EditUser = ({name, id, editState, setEditState, users, setUsers}) => {
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
        let newName = document.getElementById('nameFormEdit').value;
        let ytLink = document.getElementById('linkFormEdit').value;

        let changeName = newName !== "";
        let changeLink = ytLink !== "";
        let changeFile = typeof file !== "undefined"; 

        let inputFail = !changeName && !changeLink && !changeFile; 
        if (inputFail) {
            setNameErr("Modify at least 1");
            setLinkErr("Modify at least 1");
            setFileErr("Modify at least 1");
            return; 
        }

        if (changeName) {
            if (newName.length > 20) {
                setNameErr("Character Limit Exceeded, below 20.");
                inputFail = true; 
            }
        } 
        if (changeLink) {
            if (!linkIsValid(ytLink)) {
                setLinkErr("Invalid Youtube Link.");
                inputFail = true; 
            }
        } 
        let b64Image = ""
        if (changeFile) {
            let reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onload = (e) => { 
                b64Image = e.target.result.replace('data:image/jpeg;base64,','');  
                if (inputFail) {return; }
                handleClose(); 
                setLoading(true); 
                sendRequest(newName, b64Image, ytLink); 
            } 
        } else {
            if (inputFail) {return; }
            handleClose(); 
            setLoading(true); 
            sendRequest(newName, b64Image, ytLink); 
        }
    }

    async function sendRequest (newName, imgData, url) {
        axios.put('http://127.0.0.1:5000/modify-user', {
            userID: id,
            name: name, 
            newName: newName, 
            imgData: imgData,
            url : url
          })
          .then(function (response) {
            handleNewUser(id); 
            setLoading(false); 
          })
          .catch(function (error) {
            console.log(error);
            setLoading(false); 
          });
    }

    const handleNewUser = userID => {
        // make a get request to get this users data
        axios
        .get(`http://127.0.0.1:5000/user/${userID}`)
        .then((response) => {
            let userData = JSON.parse(response.data)[0]; 
            // the list is updated by filering out this user by id 
            const newUsers = users.filter(parseId);
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

    function parseId(user) {
        return user["id"] !== id;  
    }

    const handleClose = () => {
        setEditState(false); 
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
        <Modal className="edit-modal border border-warning" isOpen={editState} onRequestClose={() => {handleClose()}}>
            <div className='content-form'>
                <div className='display-6 edit-title text-muted'>
                    <div className='close-form'>
                        <button className="close-button" onClick={() => {handleClose()}}><GrClose size={15}/></button>
                    </div>
                    Editing {name}
                </div>

                <div className='form-elem'>
                    {/* <label for="nameForm">Name</label> */}
                    <input id ="nameFormEdit" className ="form-control" type="text" placeholder={`Change name...`}></input>
                    <div className='text-danger'>{nameErr}</div>
                </div>
                
                <div className='form-elem'>
                    {/* <label for="linkForm">Link</label> */}
                    <input id ="linkFormEdit" className ="form-control" type="text" placeholder={`Change song (youtube link)...`}></input>
                    <div className='text-danger'>{linkErr}</div>
                </div>
               
                <div className='form-elem'>
                    <label className = "text-muted" for="fileFormEdit">Edit Face Photo</label>
                    <input id ="fileFormEdit" className ="form-control" type="file" onChange={(e) => {updateFile(e)}} placeholder='Upload a photo of yourself...'></input>
                    <div className='text-danger'>{fileErr}</div>
                </div>
                
                <div className='submit-form'>
                    <button type="button" class="btn btn-success" onClick={()=> {handleSumbit()}}>Sumbit!</button>
                </div>
            </div>
        </Modal>

        <Modal className = "load-modal border border-success" isOpen={loading}>
            <div className='content-form'>
                <div class="spinner-border spinner-border-lg text-success dates" role="status" aria-hidden="true"></div>
                <div className='display-6'>Editing {name}...</div>
                <p className='text-muted'>Currently adding meta data, images, and mp3 files to AWS and PostgreSQL servers.</p>
                <b>Please do not refresh!</b>
            </div>
            
        </Modal>


    </div>
  )
}

export default EditUser