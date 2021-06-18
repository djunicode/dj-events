import React from "react";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  root: {
    display: "flex",
    flexDirection: "row",
    justifyContent: "center",
    borderBottom: "1px solid white",
  },
  right: {
    marginLeft: "-20%",
    fontFamily: "Roboto",
    fontWeight: "500px",
    fontStyle: "normal",
    lineHeight: "35px",
    fontSize: "36px",
    color: "white",
    marginTop: "30px",
  },
  left: {
    marginLeft: "-20%",
    marginTop: "20px",
  },
}));

export default function LoggedHeader() {
  const classes = useStyles();
  var CommitteeName = localStorage.getItem("CommitteeName");
  var CommitteeDepartment = localStorage.getItem("CommitteeDepartment");
  var ChairPerson = localStorage.getItem("CommitteeName");
  return (
    <div className={classes.root}>
      <div className={classes.left}>
        <img
          style={{ borderRadius: "50%" }}
          width="18%"
          height="75%"
          src="https://www.pngitem.com/pimgs/m/264-2640465_passport-size-photo-sample-hd-png-download.png"
        />
      </div>
      <div className={classes.right}>
        <div>{CommitteeName}</div>
        <div>{CommitteeDepartment}</div>
        <div>{ChairPerson}</div>
      </div>
    </div>
  );
}
