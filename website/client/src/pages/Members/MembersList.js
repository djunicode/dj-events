import React from "react";
import Co from "./Co";
import Core from "./Core";
import Grid from "@material-ui/core/Grid";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  memberlist: {
    marginTop: "1%",
  },
  border: {
    borderRight: "2px solid black",
  },
}));

const MembersList = () => {
  const classes = useStyles();
  return (
    <div className={classes.memberlist}>
      <Grid container spacing={3}>
        <Grid item xs={1}></Grid>
        <Grid item xs={10}>
          <Grid container spacing={5}>
            <Grid item xs={6} className={classes.border}>
              <Core />
            </Grid>
            <Grid item xs={6}>
              <Co />
            </Grid>
          </Grid>
        </Grid>
        <Grid item xs={1}></Grid>
      </Grid>
    </div>
  );
};

export default MembersList;
