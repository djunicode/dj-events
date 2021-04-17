import React, { useEffect, useState } from "react";
import { MDBContainer, MDBRow, MDBCol } from "mdb-react-ui-kit";
import "../../App.css";
import axios from "axios";
import "./DetailEvent.css";
import Navbar from "../../components/Navbar/Navbar.js";
import Footer from "../../components/Footer/Footer.js";

const breakPoints = [
  { width: 1, itemsToShow: 1 },
  { width: 550, itemsToShow: 2 },
  { width: 768, itemsToShow: 3 },
  // { width: 1200, itemsToShow: 4 },
];

const DetailEvent = () => {
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
      <h1 className="title_name">Digihunt</h1>
      <MDBRow className="mb-4 imageholder">
        <MDBCol md="8">
          <img
            src="https://mdbootstrap.com/img/Others/documentation/1.jpg"
            className="img-fluid"
            alt=""
          />
        </MDBCol>
      </MDBRow>
      <Footer />
    </div>
  );
};

export default DetailEvent;
