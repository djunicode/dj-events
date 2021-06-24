import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Button from "@material-ui/core/Button";

const useStyles = makeStyles((theme) => ({
  root: {
    "& > *": {
      margin: theme.spacing(1),
    },
  },
}));

class EventsReferralCountHeader extends React.Component {
  render() {
    var event_id = window.location.pathname.split("/")[2];
    const classes = useStyles;
    return (
      <div>
        <div className={classes.root}>
          <Button size="large" href="/events">
            <h5 style={{ color: "white", fontWeight: "bold" }}>Events</h5>
          </Button>
          &nbsp;&nbsp;&nbsp;&nbsp;
          <Button size="large" href={"/eventreferralcount/"+event_id}>
            <h5 style={{ color: "white", fontWeight: "bold" }}>
              Referral Count
            </h5>
          </Button>
        </div>
        <br></br>
        <br></br>
      </div>
    );
  }
}

export default EventsReferralCountHeader;
