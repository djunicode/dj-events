import React, { useEffect, useState } from 'react';
import axios from 'axios';
import '../../App.css';
import Grid from '@material-ui/core/Grid';
import SearchPage from '../../components/SearchBar/SearchPage';
import CommitteeCard from '../../components/CommitteeCard/CommitteeCard.js';

const breakPoints = [
    { width: 1, itemsToShow: 1 },
    { width: 550, itemsToShow: 2 },
    { width: 768, itemsToShow: 3 },
    // { width: 1200, itemsToShow: 4 },
  ];


  
  
  const Committees = () => {
    const [committees, setCommittees] = useState([]);
  
    useEffect(() => {
      axios.get('http://127.0.0.1:8000/api/committees/')
      .then(response => setCommittees(response.data))
      .catch(err => console.error(err));
    }, []);
  
  
      return (
        <div>
            <div className="alignhead">
                <h1>Commitees To View</h1>
            </div>
            <SearchPage/>
            <div className="d-flex align-items-center mainCard">
            <Grid container spacing={2} justify="flex-start" alignItems="flex-start">
              {committees.map(committee => (
                  <Grid item xs={12} sm={12} md={4}  key={committee.id}>
                    <CommitteeCard 
                          key={committee.id}
                          id={committee.id}
                          name={committee.committeeName}
                    />
                  </Grid>
                ))}
            </Grid>
            </div>
        </div>
      );
    }
  
    export default Committees;