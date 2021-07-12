import React, { useEffect, useState } from "react";
import axios from "axios";
import Grid from "@material-ui/core/Grid";
import Button from "@material-ui/core/Button";
import Avatar from "@material-ui/core/Avatar";
import { makeStyles } from "@material-ui/core/styles";
import ModalComponent from "../../components/Members/ModalComponent";

const useStyles = makeStyles((theme) => ({
  name: {
    fontFamily: "Roboto",
    fontWeight: "normal",
    fontStyle: "normal",
    lineHeight: "23px",
    fontSize: "19.6037px",
  },
  sap: {
    fontFamily: "Roboto",
    fontWeight: "normal",
    fontStyle: "normal",
    lineHeight: "19.14px",
    fontSize: "16.34px",
  },
  btn: {
    margin: "5%",
    color: "white",
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

const AddCo = () => {
  const classes = useStyles();
  const [students, setStudents] = useState([]);
  const [open, setOpen] = React.useState(false);

  const user_type = "Co";

  const handleOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  var id = localStorage.getItem("id");
  var data = "";
  var token = localStorage.getItem("Token");
  var config = {
    method: "get",
    url: `http://aryan123456.pythonanywhere.com/api/noncocom_list/${id}`,
    headers: {
      Authorization: "Token " + token,
    },
    data: data,
  };
  useEffect(() => {
    axios(config)
      .then((response) => setStudents(response.data))
      .catch((err) => console.error(err));
  }, []);
  return (
    <div>
      {students.map((x, index) => (
        <div>
          <Grid container spacing={3}>
            <Grid item xs={9}>
              <div className={classes.part1}>
                <div className={classes.avatar}>
                  <Avatar className={classes.colour}>
                    {x.first_name.charAt(0) + x.last_name.charAt(0)}
                  </Avatar>
                </div>
                <div>
                  <span className={classes.name}>
                    {x.first_name} {x.last_name}
                  </span>
                  <br />
                  <span className={classes.sap}>{x.username}</span>
                </div>
              </div>
            </Grid>
            <Grid item xs={3}>
              <div className={classes.part2}>
                <ModalComponent
                  username={x.username}
                  id={x.id}
                  first_name={x.first_name}
                  last_name={x.last_name}
                  isCore={0}
                />
              </div>
            </Grid>
          </Grid>
        </div>
      ))}
    </div>
  );
};

export default AddCo;
