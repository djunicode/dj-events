import React, { useEffect, useState } from 'react';
import axios from 'axios';
import '../../App.css';
import EventsCard from '../../components/EventCard/EventsCard';
import Carousel from "react-elastic-carousel";

const breakPoints = [
    { width: 1, itemsToShow: 1 },
    { width: 550, itemsToShow: 2 },
    { width: 768, itemsToShow: 3 },
    // { width: 1200, itemsToShow: 4 },
  ];

const EventCom = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/events/')
    .then(response => setEvents(response.data))
    .catch(err => console.error(err));
  }, []);


    return (
      <div>
          <div style={{marginTop : '80px'}} className="alignhead">
          </div>
          <div className="d-flex align-items-center mainCard">
            <Carousel breakPoints={breakPoints}>
            {events.map(event => (
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
    );
  }

  export default EventCom;