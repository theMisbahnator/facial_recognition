import React from 'react'
import johnCena from "../johny.webp";

const NavBar = () => {
  return (
    <div>
        <nav className="navbar navbar-dark bg-primary">
            <span className="navbar-brand mb-0 h1 navbar-johncena">
                <span className="display-4">John Cena!</span>
                <span className="container"><img className ="johncena" alt="john cena" src={johnCena}></img></span>
                <div>Created By Misbah Imtiaz</div>
            </span>
        </nav>
    </div>
  )
}

export default NavBar