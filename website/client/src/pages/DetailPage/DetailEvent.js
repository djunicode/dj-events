import React, { useEffect, useState } from "react";
import { MDBContainer, MDBRow, MDBCol } from "mdb-react-ui-kit";
import "../../App.css";
import axios from "axios";
import "./DetailEvent.css";
import Navbar from "../../components/Navbar/Navbar.js";
import Footer from "../../components/Footer/Footer.js";
import ArrowBackIosIcon from "@material-ui/icons/ArrowBackIos";
import { makeStyles } from "@material-ui/core/styles";
import Button from "@material-ui/core/Button";
import PersonIcon from "@material-ui/icons/Person";
import CallIcon from "@material-ui/icons/Call";
import GridList from "@material-ui/core/GridList";
import GridListTile from "@material-ui/core/GridListTile";

const breakPoints = [
  { width: 1, itemsToShow: 1 },
  { width: 550, itemsToShow: 2 },
  { width: 768, itemsToShow: 3 },
  // { width: 1200, itemsToShow: 4 },
];

const useStyles = makeStyles((theme) => ({
  root: {
    display: "flex",
    flexWrap: "wrap",
    justifyContent: "space-around",
    overflow: "hidden",
  },
  gridList: {
    width: 1000,
    height: 450,
  },
}));

const tileData = [
  {
    img:
      "https://images.unsplash.com/photo-1554620158-d8d5c2f3a27b?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTV8fG1haWxtYW58ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
    //  title: 'Image',
    //  author: 'author',
    //  cols: 2,
  },
  {
    img:
      "https://images.unsplash.com/photo-1554620158-d8d5c2f3a27b?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTV8fG1haWxtYW58ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
  },
  {
    img:
      "https://images.unsplash.com/photo-1554620158-d8d5c2f3a27b?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTV8fG1haWxtYW58ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
  },
  {
    img:
      "https://images.unsplash.com/photo-1504616925178-7dce65dfc3ca?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=334&q=80",
  },
  {
    img:
      "https://images.unsplash.com/photo-1554620158-d8d5c2f3a27b?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTV8fG1haWxtYW58ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
  },
  {
    img:
      "https://images.unsplash.com/photo-1554620158-d8d5c2f3a27b?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTV8fG1haWxtYW58ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
  },
  {
    img:
      "https://images.unsplash.com/photo-1554620158-d8d5c2f3a27b?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTV8fG1haWxtYW58ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
  },
  {
    img:
      "https://images.unsplash.com/photo-1554620158-d8d5c2f3a27b?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTV8fG1haWxtYW58ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
  },
  {
    img:
      "https://images.unsplash.com/photo-1554620158-d8d5c2f3a27b?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTV8fG1haWxtYW58ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
  },
  {
    img:
      "https://images.unsplash.com/photo-1554620158-d8d5c2f3a27b?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTV8fG1haWxtYW58ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
  },

  {
    img:
      "https://images.unsplash.com/photo-1554620158-d8d5c2f3a27b?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTV8fG1haWxtYW58ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
  },
  {
    img:
      "https://images.unsplash.com/photo-1554620158-d8d5c2f3a27b?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTV8fG1haWxtYW58ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
  },
];

const DetailEvent = () => {
  var event_id = window.location.pathname.split("/")[2];
  const classes = useStyles();
  const [events, setEvents] = useState([]);

  useEffect(() => {
    axios
      .get("http://aryan123456.pythonanywhere.com/api/events/" + event_id)
      .then((response) => {
        setEvents(response.data);
        console.log(response.data);
      })
      .catch((err) => console.error(err));
  }, []);

  return (
    <div style={{ overflowX: "hidden" }}>
      <Navbar />
      <div className="header" style={{ marginLeft: "670px" }}>
        <Button href="/">
          <ArrowBackIosIcon className="icon" />
        </Button>
        <h1 className="title_name">{events.eventName}</h1>
      </div>
      <MDBRow className="mb-4 imageholder" style={{ marginLeft: "470px" }}>
        <MDBCol md="12">
          <img
            src="https://mdbootstrap.com/img/Others/documentation/1.jpg"
            className="img-fluid"
            alt=""
          />
        </MDBCol>
      </MDBRow>
      <div className="left-orient">
        <h3 className="inner_title">What is the event about?</h3>
        <div className="verticaline">
          <p>{events.eventDescription}</p>
        </div>
      </div>
      <div className={classes.root}>
        <GridList cellHeight={160} className={classes.gridList} cols={3}>
          {tileData.map((tile) => (
            <GridListTile key={tile.img} cols={tile.cols || 1}>
              <img src={tile.img} alt={tile.title} />
            </GridListTile>
          ))}
        </GridList>
      </div>
      <div style={{ marginLeft: "200px", marginTop: "50px" }}>
        <h3 style={{ color: "#F54B64" }}>Interested? Register Now!</h3>
        <p>
          <a className="link" href={events.registrationLink}>
            {events.registrationLink}
          </a>
        </p>
        <h3 style={{ color: "#F54B64" }}>Facing a problem? Get in touch</h3>
        <div className="contact_details">
          <h5 className="contact" style={{ marginRight: "50px" }}>
            {" "}
            <PersonIcon className="contacticon" /> {events.contactName1}
          </h5>
          <h5 className="contact2">
            {" "}
            <CallIcon className="contacticon" /> {events.contactNumber1}
          </h5>
        </div>
        {events.contactName2 ? (
          <div className="contact_details">
            <h5 className="contact" style={{ marginRight: "110px" }}>
              {" "}
              <PersonIcon className="contacticon" /> {events.contactName2}
            </h5>
            <h5 className="contact2">
              {" "}
              <CallIcon className="contacticon" />
              {events.contactNumber2}
            </h5>
          </div>
        ) : (
          ""
        )}
      </div>
      <br />
      <Footer />
    </div>
  );
};

export default DetailEvent;
