import React, { useState } from "react";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  Login: {
    display: "flex",
    flexDirection: "row",
    justifyContent: "center",
    textAlign: "center",
  },
  form: {
    width: "40%",
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    textAlign: "center",
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const classes = useStyles();

  const signIn = () => {
    var myHeaders = new Headers();
    var formdata = new FormData();
    formdata.append("username", username);
    formdata.append("password", password);

    var requestOptions = {
      method: "POST",
      headers: myHeaders,
      body: formdata,
      redirect: "follow",
    };

    fetch(
      `http://aryan123456.pythonanywhere.com/api/committee_login/`,
      requestOptions
    )
      .then((response) => response.json())
      .then((result) => {
        console.log(result);
        console.log(result.Token);
      })
      .catch((error) => console.log("error", error));
  };

  return (
    <div className={classes.Login}>
      <form className={classes.form}>
        <TextField
          variant="outlined"
          margin="normal"
          required
          fullWidth
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          id="username"
          label="Username"
          name="username"
          autoFocus
        />
        <TextField
          variant="outlined"
          margin="normal"
          required
          fullWidth
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          name="password"
          label="Password"
          type="password"
          id="password"
        />
        <Button
          fullWidth
          variant="contained"
          color="primary"
          onClick={signIn}
          className={classes.submit}
        >
          Sign In
        </Button>
      </form>
    </div>
  );
}
