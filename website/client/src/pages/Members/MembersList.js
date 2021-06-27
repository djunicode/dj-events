import React, { useState } from "react";
import Co from "./Co";
import Core from "./Core";
import AddCo from "./AddCo";
import AddCore from "./AddCore";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import AddCircleRoundedIcon from "@material-ui/icons/AddCircleRounded";
import { makeStyles } from "@material-ui/core/styles";
import Navbar from "../../components/Navbar/Navbar";
import LoggedHeader from "../../components/LoggedHeader/LoggedHeader";
import EventsMembersHeader from "../../components/EventsMembersHeader/EventsMembersHeader";

const useStyles = makeStyles((theme) => ({
  memberlist: {
    color: "white",
    overflowX: "hidden",
  },
  add: {
    backgroundColour: "#FFFFFF",
    borderRadius: "27.5px",
    color: "#1C2E4A",
    marginBottom: "20px",
    marginTop: "-30px",
  },
  icon: {
    colour: "#F54B64",
  },
  members: {
    marginTop: "0px",
  },
}));

const MembersList = () => {
  const [addCo, setAddCo] = useState(false);
  const [addCore, setAddCore] = useState(false);

  const addCoCommittee = () => {
    setAddCo(true);
  };

  const addCoreCommittee = () => {
    setAddCore(true);
  };

  const back1 = () => {
    if (addCo) setAddCo(false);
  };

  const back2 = () => {
    if (addCore) setAddCore(false);
  };

  const classes = useStyles();
  return (
    <div className={classes.memberlist}>
      <Navbar />
      <LoggedHeader />
      <br />
      <EventsMembersHeader />
      <Grid container spacing={3} className={classes.members}>
        <Grid item xs={1}></Grid>
        <Grid item xs={10}>
          <Grid container spacing={5}>
            {addCore ? (
              <Grid item xs={6} className={classes.border}>
                <Button
                  variant="contained"
                  className={classes.add}
                  onClick={back2}
                >
                  Back
                </Button>
                <AddCore />
              </Grid>
            ) : (
              <Grid item xs={6} className={classes.border}>
                <Button
                  variant="contained"
                  className={classes.add}
                  onClick={addCoreCommittee}
                  startIcon={<AddCircleRoundedIcon className={classes.icon} />}
                >
                  Add A Core Member
                </Button>
                <Core />
              </Grid>
            )}
            {addCo ? (
              <Grid item xs={6}>
                <Button
                  variant="contained"
                  className={classes.add}
                  onClick={back1}
                >
                  Back
                </Button>
                <AddCo />
              </Grid>
            ) : (
              <Grid item xs={6}>
                <Button
                  variant="contained"
                  className={classes.add}
                  onClick={addCoCommittee}
                  startIcon={<AddCircleRoundedIcon className={classes.icon} />}
                >
                  Add A Co-Committee Member
                </Button>
                <Co />
              </Grid>
            )}
          </Grid>
        </Grid>
        <Grid item xs={1}></Grid>
      </Grid>
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
    </div>
  );
};

export default MembersList;
