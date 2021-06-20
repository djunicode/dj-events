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
import EventsCard from "../../components/EventCard/EventsCard";
import Carousel from "react-elastic-carousel";
import Grid from "@material-ui/core/Grid";
import CommitteeCard from "../../components/CommitteeCard/CommitteeCard";

const breakPoints = [
  { width: 1, itemsToShow: 1 },
  { width: 550, itemsToShow: 2 },
  { width: 768, itemsToShow: 3 },
  { width: 1200, itemsToShow: 4 },
];

const CommitteePage = () => {
  const [committee, setCommittee] = useState([]);
  const [events, setEvents] = useState([]);
  const [core, setCore] = useState([]);
  const [faculty, setFaculty] = useState([]);
  var committee_id = window.location.pathname.split("/")[2];
  useEffect(() => {
    axios
      .get(
        "http://aryan123456.pythonanywhere.com/api/committee_detail/" +
          committee_id
      )
      .then((response) => {
        console.log(response.data);
        setCommittee(response.data);
        setEvents(response.data.events);
        setFaculty(response.data.facultyMembers);
        setCore(response.data.coreCommitteeMembers);
      })
      // .then(response => console.log(response.data))
      .catch((err) => console.error(err));
  }, []);
  return (
    <div>
      <Navbar />
      <h1 className="com_name">{committee.committeeName}</h1>
      <MDBCard className="center_card" style={{ maxWidth: "700px" }}>
        <MDBRow className="g-0">
          <MDBCol md="4">
            <MDBCardImage
              src="https://wallpapercave.com/wp/wp2587127.jpg"
              alt="..."
              fluid
            />
          </MDBCol>
          <MDBCol md="8">
            <MDBCardBody>
              <MDBCardTitle className="align">About Us</MDBCardTitle>
              <MDBCardText>{committee.committeeDescription}</MDBCardText>
            </MDBCardBody>
          </MDBCol>
        </MDBRow>
      </MDBCard>
      <h3 className="inner_title">Events related to this committee</h3>
      <div>
        <div style={{ marginTop: "80px" }} className="alignhead"></div>
        <div className="d-flex align-items-center mainCard">
          <Carousel breakPoints={breakPoints}>
            {events.map((event) => (
              <EventsCard
                key={event.id}
                id={event.id}
                name={event.eventName}
                committeeId={event.organisingCommittee}
              />
            ))}
          </Carousel>
        </div>
      </div>
      <h3 className="inner_title2">Faculty Members</h3>
      <p className="year">2020-2021</p>
      <div>
        <div className="d-flex align-items-center mainCard">
          <Grid
            container
            spacing={2}
            justify="flex-start"
            alignItems="flex-start"
          >
            {faculty.map((members) => (
              <Grid item xs={12} sm={12} md={4} key={members.id}>
                <CommitteeCard
                  key={members.id}
                  id={members.id}
                  name={members.name}
                />
              </Grid>
            ))}
          </Grid>
        </div>
      </div>
      <h3 className="inner_title2">Core Members</h3>
      <p className="year">2020-2021</p>
      <div>
        <div className="d-flex align-items-center mainCard">
          <Grid
            container
            spacing={2}
            justify="flex-start"
            alignItems="flex-start"
          >
            {core.map((core_members) => (
              <Grid item xs={12} sm={12} md={4} key={core_members.id}>
                <CommitteeCard
                  key={core_members.id}
                  id={core_members.id}
                  name={core_members.student}
                />
              </Grid>
            ))}
          </Grid>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default CommitteePage;
