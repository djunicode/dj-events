import React, { useEffect, useState } from "react";
import axios from "axios";
import Button from "@material-ui/core/Button";
import Modal from "@material-ui/core/Modal";
import Backdrop from "@material-ui/core/Backdrop";
import Avatar from "@material-ui/core/Avatar";
import Fade from "@material-ui/core/Fade";
import { makeStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";

const useStyles = makeStyles((theme) => ({
  btn: {
    margin: "5%",
  },
  modal: {
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  },
  paper: {
    backgroundColor: "#4E586E",
    border: "1px solid #FFFFFF",
    borderRadius: "25px",
    padding: theme.spacing(2, 4, 3),
  },
  avatar: {
    marginRight: "2%",
    marginTop: "2px",
  },
  colour: {
    backgroundColor: "green",
  },
  userinfo: {
    display: "flex",
    flexDirection: "row",
    justifyContent: "center",
  },
  sap: {
    fontFamily: "Roboto",
    color: "#FFFFFF",
    fontSize: "11.2598px",
    lineHeight: "13px",
  },
  name: {
    fontFamily: "Roboto",
    color: "#FFFFFF",
    fontSize: "13.5118px",
    lineHeight: "16px",
  },
  input: {
    backgroundColor: "#1C2E4A",
    borderRadius: "90.6256px",
    height: "30px",
    width: "236px",
    color: "#FFFFFF",
    display: "flex",
    flexDirection: "row",
    justifyContent: "center",
    marginTop: "5%",
    marginBottom: "8%",
  },
  title: {
    display: "flex",
    flexDirection: "row",
    justifyContent: "center",
    fontFamily: "Roboto",
    color: "#FFFFFF",
    fontSize: "26.76px",
    lineHeight: "20px",
  },
  submit: {
    display: "flex",
    flexDirection: "row",
    justifyContent: "center",
  },
  done: {
    height: "35px",
    color: "linear-gradient(62.97deg, #F54B64 29.17%, #F78361 100%)",
    opacity: "0.5",
    borderRadius: "48px",
  },
}));

const ModalComponent = (username) => {
  const classes = useStyles();
  const [open, setOpen] = useState(false);
  const [designation, setDesignation] = useState("");

  const handleOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <div>
      <Button variant="outlined" onClick={handleOpen} className={classes.btn}>
        Add
      </Button>
      <Modal
        aria-labelledby="transition-modal-title"
        aria-describedby="transition-modal-description"
        className={classes.modal}
        open={open}
        onClose={handleClose}
        closeAfterTransition
        BackdropComponent={Backdrop}
        BackdropProps={{
          timeout: 500,
        }}
      >
        <Fade in={open}>
          <div className={classes.paper}>
            <p id="transition-modal-title" className={classes.title}>
              Choose Designation:
            </p>
            <div className={classes.userinfo}>
              <div className={classes.avatar}>
                <Avatar className={classes.colour}>
                  {username.first_name.charAt(0) + username.last_name.charAt(0)}
                </Avatar>
              </div>
              <div>
                <span
                  id="transition-modal-description"
                  className={classes.name}
                >
                  {username.first_name} {username.last_name}
                </span>
                <br />
                <span id="transition-modal-description" className={classes.sap}>
                  {username.username}
                </span>
              </div>
            </div>
            <input
              className={classes.input}
              label="position"
              placeholder="  Enter Designation"
              value={designation}
              onChange={(e) => setDesignation(e.target.value)}
            />
            <div className={classes.submit}>
              <Button
                variant="contained"
                color="secondary"
                className={classes.done}
              >
                Done
              </Button>
            </div>
          </div>
        </Fade>
      </Modal>
    </div>
  );
};

export default ModalComponent;
