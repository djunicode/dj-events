import React from "react";
import Grid from "@material-ui/core/Grid";
import Button from "@material-ui/core/Button";
import Avatar from "@material-ui/core/Avatar";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  name: {
    fontFamily: "Roboto",
    fontWeight: "normal",
    fontStyle: "normal",
    lineHeight: "23px",
    fontSize: "19.6037px",
  },
  position: {
    fontFamily: "Roboto",
    fontWeight: "normal",
    fontStyle: "normal",
    lineHeight: "19.14px",
    fontSize: "16.34px",
  },
  btn: {
    margin: "5%",
  },
  avatar: {
    marginRight: "2%",
    marginTop: "2px",
  },
  part1: {
    display: "flex",
    flexDirection: "row",
    textAlign: "center",
  },
  part2: {
    float: "right",
  },
  colour: {
    backgroundColor: "green",
  },
}));

const DisplayMembers2 = ({ id, name, positionAssigned }) => {
  const removeCore = () => {
    var token = localStorage.getItem("Token");
    var myHeaders = new Headers();
    myHeaders.append("Authorization", `Token ${token}`);

    var requestOptions = {
      method: "POST",
      headers: myHeaders,
      redirect: "follow",
    };

    fetch(
      `http://aryan123456.pythonanywhere.com/api/delete_core_committee_member/${id}/`,
      requestOptions
    )
      .then((response) => response.text())
      .then((result) => console.log(result))
      .catch((error) => console.log("error", error));
  };
  const classes = useStyles();
  let substrings = name.split(" ");
  let f = substrings[0].charAt(0);
  let l = substrings[1].charAt(0);
  let initials = f + l;
  return (
    <div>
      <Grid container spacing={3}>
        <Grid item xs={9}>
          <div className={classes.part1}>
            <div className={classes.avatar}>
              <Avatar className={classes.colour}>{initials}</Avatar>
            </div>
            <div>
              <span className={classes.name}>John Smith</span>
              <br />
              <span className={classes.position}>60004190126</span>
            </div>
          </div>
        </Grid>
        <Grid item xs={3}>
          <div className={classes.part2}>
            <Button
              variant="outlined"
              onClick={removeCore}
              className={classes.btn}
            >
              Remove
            </Button>
          </div>
        </Grid>
      </Grid>
    </div>
  );
};
export default DisplayMembers2;
