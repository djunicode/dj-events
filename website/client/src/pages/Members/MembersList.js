import React from "react";
import Co from "./Co";
import Core from "./Core";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import AddCircleRoundedIcon from "@material-ui/icons/AddCircleRounded";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  memberlist: {
    marginTop: "1%",
  },
  border: {
    borderRight: "2px solid black",
  },
  add: {
    backgroundColour: "#FFFFFF",
    borderRadius: "27.5px",
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
              <Button
                variant="contained"
                className={classes.add}
                startIcon={<AddCircleRoundedIcon />}
              >
                Add A Core Member
              </Button>
              <Core />
            </Grid>
            <Grid item xs={6}>
              <Button
                variant="contained"
                className={classes.add}
                startIcon={<AddCircleRoundedIcon />}
              >
                Add A Co-Committee Member
              </Button>
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
