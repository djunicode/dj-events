import React from "react";
import EventsReferralCountHeader from "../../components/EventsReferralCountHeader/EventsReferralCountHeader";
import Navbar from "../../components/Navbar/Navbar";
import LoggedHeader from "../../components/LoggedHeader/LoggedHeader";
import axios from "axios";
import { withRouter} from 'react-router-dom';

class EventEdit extends React.Component {
    state = {
        event:[],
        eventDescription:"",
        eventSummary:"blah meh meh",
        eventName:"",
        eventDate:"",
        eventTime:"13:55:55",
        eventSeatingCapacity:0,
        eventVenue:"",
        registrationLink:"",
        is_referral:false,
        contactName1:null,
        contactName2:null,
        contactNumber1:null,
        contactNumber2:null,
    }
    onChange=(e)=>{
      this.setState({
        [e.target.name]:e.target.value
      })
    }
    EventPost=(e)=>{
      e.preventDefault();
      var token = localStorage.getItem("Token");
      var committee_id = parseInt(localStorage.getItem("id"))
      var event_id = window.location.pathname.split("/")[2];
      var myHeaders = new Headers();
      myHeaders.append("Authorization", "Token "+token);
      myHeaders.append("Content-Type", "application/json");
  
      var raw = JSON.stringify({"eventDescription":this.state.eventDescription?this.state.eventDescription:this.state.event.eventDescription,
      "eventSummary":this.state.eventSummary?this.state.eventSummary:this.state.event.eventSummary,
      "eventName":this.state.eventName?this.state.eventName:this.state.event.eventName,
      "eventDate":this.state.eventDate?this.state.eventDate:this.state.event.eventDate,
      "eventTime":this.state.eventTime?this.state.eventTime:this.state.event.eventTime,
      "eventSeatingCapacity":this.state.eventSeatingCapacity,
      "eventVenue":this.state.eventVenue?this.state.eventVenue:this.state.event.eventVenue,
      "registrationLink":this.state.registrationLink?this.state.registrationLink:this.state.event.registrationLink,
      "is_referral":this.state.is_referral?this.state.is_referral:this.state.event.is_referral,
      "organisingCommittee":committee_id,
      "contactName1":this.state.contactName1?this.state.contactName1:this.state.event.contactName1,
      "contactName2":this.state.contactName2?this.state.contactName2:this.state.event.contactName2,
      "contactNumber1":this.state.contactNumber1?this.state.contactNumber1:this.state.event.contactNumber1,
      "contactNumber2":this.state.contactNumber2?this.state.contactNumber2:this.state.event.contactNumber2});
  
      var requestOptions = {
        method: 'PUT',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
      };
  
      fetch("http://aryan123456.pythonanywhere.com/api/eventscrud/"+event_id+"/", requestOptions)
      .then(response => response.text())
      .then(result => console.log(result))
      .catch(error => console.log('error', error));
  
      this.props.history.push('/events');
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
    return (
      <div style={{ background: "#1C2E4A" }}>
        <Navbar />
        <LoggedHeader />
        <EventsReferralCountHeader />
        <form onSubmit={this.EventPost} >
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
              onChange={this.onChange}
              name="eventName"
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
              onChange={this.onChange}
              name="eventDescription"
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
              onChange={this.onChange}
              name="eventDate"
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
              onChange={this.onChange}
              name="eventVenue"
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
              onChange={this.onChange}
              name="registrationLink"
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
                onChange={this.onChange}
                name="contactName1"
                className="eventinput"
                style={{ width: "60%", padding: "5px" }}
                type="text"
                placeholder="Person's Name"
                value={this.state.event.contactName1}
              ></input>
              &nbsp;
              <input
                onChange={this.onChange}
                name="contactNumber1"
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
                onChange={this.onChange}
                name="contactName2"
                className="eventinput"
                style={{ width: "60%", padding: "5px" }}
                type="text"
                placeholder="Person's Name"
                value={this.state.event.contactName2}
              ></input>
              &nbsp;
              <input
                onChange={this.onChange}
                name="contactNumber2"
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
        </form>
        <br></br>
        <br></br>
      </div>
    );
  }
}

export default withRouter(EventEdit);
