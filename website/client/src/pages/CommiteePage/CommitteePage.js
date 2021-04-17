import React, { useEffect, useState } from "react";
import "../../App.css";
import axios from "axios";
import {
  MDBCard,
  MDBCardTitle,
  MDBCardText,
  MDBCardBody,
  MDBCardImage,
  MDBRow,
  MDBCol,
} from "mdb-react-ui-kit";
import "./CommitteePage.css";
import EventCom from "./EventCom.js";
import Members from "./Members.js";
import Navbar from "../../components/Navbar/Navbar.js";
import Footer from "../../components/Footer/Footer.js";

const breakPoints = [
  { width: 1, itemsToShow: 1 },
  { width: 550, itemsToShow: 2 },
  { width: 768, itemsToShow: 3 },
  // { width: 1200, itemsToShow: 4 },
];

const CommitteePage = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/events/")
      .then((response) => setEvents(response.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div>
      <Navbar />
      <h1 className="com_name">ACM COMMITTEE</h1>
      <MDBCard className="center_card" style={{ maxWidth: "700px" }}>
        <MDBRow className="g-0">
          <MDBCol md="4">
            <MDBCardImage
              src="https://mdbcdn.b-cdn.net/wp-content/uploads/2020/06/vertical.jpg"
              alt="..."
              fluid
            />
          </MDBCol>
          <MDBCol md="8">
            <MDBCardBody>
              <MDBCardTitle className="align">Card title</MDBCardTitle>
              <MDBCardText>
                This is a wider card with supporting text below as a natural
                lead-in to additional content. This content is a little bit
                longer.
              </MDBCardText>
              <MDBCardText>
                <small className="text-muted">Last updated 3 mins ago</small>
              </MDBCardText>
            </MDBCardBody>
          </MDBCol>
        </MDBRow>
      </MDBCard>
      <h3 className="inner_title">Events related to this committee</h3>
      <EventCom />
      <h3 className="inner_title2">Faculty Members</h3>
      <p className="year">2020-2021</p>
      <Members />
      <h3 className="inner_title2">Core Members</h3>
      <p className="year">2020-2021</p>
      <Members />
      <Footer />
    </div>
  );
};

export default CommitteePage;
