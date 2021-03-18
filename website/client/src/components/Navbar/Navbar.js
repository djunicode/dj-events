import React from 'react';
import {
  MDBNavbar,
  MDBNavbarNav,
  MDBNavbarItem,
  MDBNavbarLink,
  MDBContainer,
  MDBIcon } from 'mdb-react-ui-kit';
  import '../Header/Header.css';

const Navbar =()=> {
  return (
    <header  classname="mask">
        <MDBNavbar  expand='lg' light bgColor='#1c2e4a'>
        <MDBContainer  fluid>
          <div  className='collapse navbar-collapse' id='navbarExample01'>
            <MDBNavbarNav right className='mb-2 mb-lg-0 justify-content-end ml-auto '>
              <MDBNavbarItem active>
                <MDBNavbarLink className=" spacingnav" aria-current='page'href='#'>
                  <h3>Events</h3>
                </MDBNavbarLink>
              </MDBNavbarItem>
              <MDBNavbarItem>
                <MDBNavbarLink  className=" spacingnav"href='#'><h3>Commitee</h3></MDBNavbarLink>
              </MDBNavbarItem>
              <MDBNavbarItem>
                <MDBNavbarLink className=" spacingnav" href='#'><h3>Login</h3></MDBNavbarLink>
              </MDBNavbarItem>
              {/* <MDBNavbarItem>
                <MDBNavbarLink href='#'>About</MDBNavbarLink>
              </MDBNavbarItem> */}
            </MDBNavbarNav>
          </div>
        </MDBContainer>
      </MDBNavbar>
            
       
    </header>
  );
}

export default Navbar;