import React from "react";
import {
  MDBNavbar,
  MDBNavbarNav,
  MDBNavbarItem,
  MDBNavbarLink,
  MDBContainer,
  MDBIcon,
} from "mdb-react-ui-kit";
import "./Navbar.css";

const Navbar = () => {
  return (
    <header classname="mask">
      <MDBNavbar
        style={{ backgroundColor: "transparent" }}
        expand="lg"
        light
        bgColor=""
      >
        <MDBContainer fluid>
          {/* <MDBNavbarToggler
            aria-controls='navbarExample01'
            aria-expanded='false'
            aria-label='Toggle navigation'
          >
            <MDBIcon fas icon='bars' />
          </MDBNavbarToggler> */}
          <div className="collapse navbar-collapse" id="navbarExample01">
            <MDBNavbarNav
              right
              className="mb-2 mb-lg-0 justify-content-end ml-auto "
            >
              <MDBNavbarItem active>
                <MDBNavbarLink
                  className=" spacingnav"
                  aria-current="page"
                  href="#"
                >
                  <h3>Events</h3>
                </MDBNavbarLink>
              </MDBNavbarItem>
              <MDBNavbarItem>
                <MDBNavbarLink className=" spacingnav" href="#">
                  <h3>Commitee</h3>
                </MDBNavbarLink>
              </MDBNavbarItem>
              <MDBNavbarItem>
                <MDBNavbarLink className=" spacingnav" href="#">
                  <h3>Login</h3>
                </MDBNavbarLink>
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
};

export default Navbar;
