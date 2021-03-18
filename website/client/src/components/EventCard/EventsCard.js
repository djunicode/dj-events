import React from 'react';
import './EventsCard.css';
import { MDBCard, MDBCardBody, MDBCardTitle, MDBCardText, MDBCardImage, MDBCardLink } from 'mdb-react-ui-kit';

const CustomCard = ({id,name,summary,committeeName}) => {
  return (
    <div >
    <MDBCard className="myCard">
      <MDBCardImage src='https://mdbootstrap.com/img/new/standard/nature/184.jpg' position='top' alt='...' />
      <MDBCardBody className="bgcolor">
        <MDBCardTitle>{name}</MDBCardTitle>
        <MDBCardText>
          {summary}
        </MDBCardText>
        
        <MDBCardLink classname="spacinglink"style={{ color: '#F54B64'}} href='#'>{committeeName}</MDBCardLink>
        <MDBCardLink style={{ color: '#F54B64'}} href='#'>KNOW MORE</MDBCardLink>
        
      </MDBCardBody>
    </MDBCard>
    </div>
  );

}
export default CustomCard;