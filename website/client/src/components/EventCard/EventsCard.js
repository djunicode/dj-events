import React from "react";
import "./EventsCard.css";
import {
  MDBCard,
  MDBCardBody,
  MDBCardTitle,
  MDBCardText,
  MDBCardImage,
  MDBCardLink,
} from "mdb-react-ui-kit";

const CustomCard = ({ id, name, summary, committeeName }) => {
  return (
    <div>
      <MDBCard className="myCard">
        <MDBCardImage
          src="https://wallpapercave.com/wp/wp2587127.jpg"
          position="top"
          alt="..."
        />
        <MDBCardBody className="bgcolor">
          <MDBCardTitle>{name}</MDBCardTitle>
          <MDBCardText>{summary}</MDBCardText>

          <MDBCardLink
            style={{ color: "#F54B64", marginLeft: "0px" }}
            href={"/event/" + id}
          >
            KNOW MORE
          </MDBCardLink>

          <MDBCardLink
            classname="spacinglink"
            style={{ color: "#F54B64" }}
            href="#"
          >
            {committeeName}
          </MDBCardLink>
        </MDBCardBody>
      </MDBCard>
    </div>
  );
};
export default CustomCard;
