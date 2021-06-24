import React from "react";
import EventsReferralCountHeader from "../../components/EventsReferralCountHeader/EventsReferralCountHeader";
import Navbar from "../../components/Navbar/Navbar";
import LoggedHeader from "../../components/LoggedHeader/LoggedHeader";
import axios from "axios";

class EventEdit extends React.Component {
    state = {
        event:[],
    }
    componentDidMount() {
        var token = localStorage.getItem("Token");
        var event_id = window.location.pathname.split("/")[2];
        var data = "";
        var config = {
          method: "get",
          url:
            "http://aryan123456.pythonanywhere.com/api/events/" +
            event_id +
            "/",
          headers: {
            Authorization: "Token " + token,
          },
          data: data,
        };
        axios(config)
          .then((response) => this.setState({ event: response.data }))
          .catch((err) => console.error(err));
      }


  render() {
      console.log(this.state.event)
    return (
      <div style={{ background: "#1C2E4A" }}>
        <Navbar />
        <LoggedHeader />
        <EventsReferralCountHeader />
        <div
          className="container"
          style={{
            color: "white",
            padding: "30px",
            background: "#4E586E",
            display: "flex",
            borderRadius: "28.39px",
            boxShadow: "3px 3px black",
          }}
        >
          <div className="col-sm-4">
            <h3 style={{ textAlign: "left" }}>Name of the event:</h3>
            <input
              className="eventinput"
              style={{ width: "100%", padding: "5px" }}
              type="text"
              placeholder="Enter the name of the event"
              value={""+this.state.event.eventName}
            ></input>
            <br></br>
            <br></br>
            <h3 style={{ textAlign: "left" }}>Short Description:</h3>
            <textarea
              className="eventinput"
              style={{ width: "100%", padding: "5px", height: "100px" }}
              type="text"
              placeholder="Enter a short description of the event"
              value={""+this.state.event.eventDescription}
            ></textarea>
            <br></br>
            <br></br>
            <h3 style={{ textAlign: "left" }}>Date of the event:</h3>
            <input
              className="eventinput"
              style={{ width: "100%", padding: "5px" }}
              type="date"
              placeholder="Choose a Date"
              value={this.state.event.eventDate}
            ></input>
            <br></br>
            <br></br>
            <h3 style={{ textAlign: "left" }}>Venue of the event:</h3>
            <input
              className="eventinput"
              style={{ width: "100%", padding: "5px", fill: "#fff" }}
              type="text"
              placeholder="Enter the venue of the event"
              value={""+this.state.event.eventVenue}
            ></input>
            <br></br>
            <br></br>
          </div>
          <div className="col-sm-4">
            <h3 style={{ textAlign: "left" }}>Link to Register:</h3>
            <input
              className="eventinput"
              style={{ width: "100%", padding: "5px" }}
              type="text"
              placeholder="Paste the link to register"
              value={""+this.state.event.registrationLink}
            ></input>
            <br></br>
            <br></br>
            <h3 style={{ textAlign: "left" }}>Contact Details:</h3>
            <div style={{ width: "100%", display: "flex" }}>
              <input
                className="eventinput"
                style={{ width: "60%", padding: "5px" }}
                type="text"
                placeholder="Person's Name"
                value={this.state.event.contactName1}
              ></input>
              &nbsp;
              <input
                className="eventinput"
                style={{ width: "100%", padding: "5px" }}
                type="text"
                placeholder="Contact Number"
                value={this.state.event.contactNumber1}
              ></input>
            </div>
            <br></br>
            <div style={{ width: "100%", display: "flex" }}>
              <input
                className="eventinput"
                style={{ width: "60%", padding: "5px" }}
                type="text"
                placeholder="Person's Name"
                value={this.state.event.contactName2}
              ></input>
              &nbsp;
              <input
                className="eventinput"
                style={{ width: "100%", padding: "5px" }}
                type="text"
                placeholder="Contact Number"
                value={this.state.event.contactNumber2}
              ></input>
            </div>
            <br></br>
            <h3 style={{ textAlign: "left" }}>Upload Poster:</h3>
            <input
              className="eventinput"
              accept="image/*"
              type="file"
              style={{
                width: "100%",
                padding: "5px",
                border: "1px solid black",
              }}
            />
            <br></br>
            <br></br>
            <div style={{ display: "flex", width: "100%" }}>
              <h3 style={{ textAlign: "left" }}>Add Referral?</h3>
              <input
                className="eventinput"
                style={{ width: "35px", height: "35px", textAlign: "right" }}
                type="checkbox"
              ></input>
            </div>
            <button
              style={{
                width: "100%",
                height: "38px",
                color: "white",
                background:
                  "linear-gradient(62.97deg, #F54B64 29.17%, #F78361 100%)",
                borderRadius: "9.51273px",
              }}
              type="submit"
            >
              Edit the Event
            </button>
            <br></br>
            <br></br>
          </div>
          <div className="col-sm-4">
            <h3 style={{ textAlign: "left" }}>Preview of the poster:</h3>
            <img width="100%" />
            <br></br>
            <br></br>
          </div>
        </div>
        <br></br>
        <br></br>
      </div>
    );
  }
}

export default EventEdit;
