import React, { useEffect, useState } from 'react';
import '../../App.css';
import axios from 'axios';
import Events from './Events';
import Committees from './Committees';
import Header from '../../components/Header/Header' ;
import Footer from '../../components/Footer/Footer.js';

const breakPoints = [
    { width: 1, itemsToShow: 1 },
    { width: 550, itemsToShow: 2 },
    { width: 768, itemsToShow: 3 },
    // { width: 1200, itemsToShow: 4 },
  ];


  
  
const Home = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/events/')
    .then(response => setEvents(response.data))
    .catch(err => console.error(err));
  }, []);


    return (
      <div>
          <Header/>
          <Events />
          <Committees />
          <Footer/>
      </div>
    );
  }

  export default Home;