import React from "react";
import EventsMembersHeader from "../../components/EventsMembersHeader/EventsMembersHeader";
import EventCard from "../../components/EventPage-EventCard/EventCard";
import AddCard from "../../components/EventPage-EventCard/AddCard";
import axios from "axios"

class EventList extends React.Component {
    state = {
        events: []
    }
    componentDidMount(){
        var token = localStorage.getItem("Token");
        var committee_id = localStorage.getItem("id");
        var data=""
        var config = {
            method: "get",
            url:"http://aryan123456.pythonanywhere.com/api/eventfinder/"+committee_id+"/",
            headers: {
                Authorization: "Token " + token,
            },
            data: data,
        };
        axios(config)
            .then((response)=>this.setState({events:response.data}))
            .catch((err) => console.error(err));
    }
    render() {
      return (
        <div  style={{background:'#1C2E4A'}}>
            <div className='container'>
                <br></br><br></br>
                <EventsMembersHeader/>
                <div className='row'>
                <AddCard/>
                {this.state.events.map((event)=><EventCard event = {event}/>)}
                </div>
            </div>
            <br></br><br></br>
        </div>
      );
    }
}

export default EventList;