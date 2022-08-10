import React, { useState } from 'react'
import { FcPlus } from "react-icons/fc";
import { GrClose } from "react-icons/gr";

import '../index'
import Modal from 'react-modal';

Modal.setAppElement("#root"); 
const AddUser = () => {
    const [isOpen, setIsOpen] = useState(false);
  return (
    <div>
        <FcPlus className="adduser" size={50} onClick={()=>{setIsOpen(true)}}/>

        <Modal className="add-modal" isOpen={isOpen} onRequestClose={() => {setIsOpen(false)}}>
            <div className='content-form'>
                <div className='close-form'>
                    <button className="close-button" onClick={() => {setIsOpen(false)}}><GrClose/></button>
                </div>
                <div className='display-4 title-form'>
                    Add User
                </div>

                <div className='form-elem'>
                    <input className ="form-control" type="text" placeholder='Enter a name...'></input>
                </div>
                
                <div className='form-elem'>
                    <input className ="form-control" type="text" placeholder='Paste link from Youtube...'></input>
                </div>
               
                <div className='form-elem'>
                    <input className ="form-control" type="file" placeholder='Upload a photo of yourself...'></input>
                </div>
                
                <div className='submit-form'>
                    <button type="button" class="btn btn-success">Create!</button>
                </div>
                

            </div>
        </Modal>
        
        
    </div>
  )
}

export default AddUser