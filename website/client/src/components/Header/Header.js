import React from 'react';
import {
  MDBNavbar,
  MDBNavbarNav,
  MDBNavbarItem,
  MDBNavbarLink,
  MDBContainer,
  MDBIcon } from 'mdb-react-ui-kit';
  import './Header.css';

const Header =()=> {
  return (
    <header  classname="mask">
      <div className='p-5 text-center bg-image'>
        <div className='mask'>
        <MDBNavbar style={{ backgroundColor: 'transparent'}} expand='lg' light bgColor=''>
        <MDBContainer  fluid>
          {/* <MDBNavbarToggler
            aria-controls='navbarExample01'
            aria-expanded='false'
            aria-label='Toggle navigation'
          >
            <MDBIcon fas icon='bars' />
          </MDBNavbarToggler> */}
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
            
          <div className='d-flex justify-content-center align-items-center h-100'>
            <div className='text-white'>
              <h1 className='mb-3 display-2'>Welcome to events portal</h1>
              {/* <h4 className='mb-3'>Subheading</h4> */}
              {/* <a className='btn btn-outline-light btn-lg' href='#!' role='button'>
                Call to action
              </a> */}
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}

export default Header;