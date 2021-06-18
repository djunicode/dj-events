import React, { useState } from "react";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import { makeStyles } from "@material-ui/core/styles";
import IconButton from "@material-ui/core/IconButton";
import Input from "@material-ui/core/Input";
import FilledInput from "@material-ui/core/FilledInput";
import OutlinedInput from "@material-ui/core/OutlinedInput";
import InputLabel from "@material-ui/core/InputLabel";
import InputAdornment from "@material-ui/core/InputAdornment";
import FormHelperText from "@material-ui/core/FormHelperText";
import FormControl from "@material-ui/core/FormControl";
import Visibility from "@material-ui/icons/Visibility";
import VisibilityOff from "@material-ui/icons/VisibilityOff";
import clsx from "clsx";

import { createMuiTheme, ThemeProvider } from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  Login: {
    display: "flex",
    flexDirection: "row",
    justifyContent: "center",
    textAlign: "center",
    height: "600px",
  },
  form: {
    width: "40%",
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    textAlign: "center",
    marginTop: theme.spacing(1),
    color: "white",
    backgroundColour: "red",
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
    backgroundColor: "linear-gradient(62.97deg, #F54B64 29.17%, #F78361 100%)",
    borderRadius: "12.1309px",
  },
  input: {
    color: "white",
  },
  forgotpwd: {
    color: "white",
  },
}));

const theme = createMuiTheme({
  palette: {
    primary: {
      main: "#F54B64",
    },
    secondary: {
      main: "#FFFFFF",
    },
  },
});

export default function Login() {
  const [username, setUsername] = useState("");
  const [msg, setMsg] = useState("");
  const [values, setValues] = React.useState({
    password: "",
    showPassword: false,
  });
  const handleChange = (prop) => (event) => {
    setValues({ ...values, [prop]: event.target.value });
  };

  const handleClickShowPassword = () => {
    setValues({ ...values, showPassword: !values.showPassword });
  };

  const handleMouseDownPassword = (event) => {
    event.preventDefault();
  };
  const classes = useStyles();

  const signIn = () => {
    var myHeaders = new Headers();
    var formdata = new FormData();
    formdata.append("username", username);
    formdata.append("password", values.password);

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
        if (result.Message) {
          setMsg("Invalid username or password");
        } else {
          setMsg("");
          const logged = true;
          localStorage.setItem("Token", result.Token);
          localStorage.setItem("CommitteeName", result.CommitteeName);
          localStorage.setItem(
            "CommitteeDepartment",
            result.CommitteeDepartment
          );
          localStorage.setItem("id", result.id);
          localStorage.setItem("logged", logged);
        }
      })
      .catch((error) => console.log("error", error));
  };

  return (
    <ThemeProvider theme={theme}>
      <div className={classes.root}>
        <div className={classes.Login}>
          <form className={classes.form}>
            <h1>Welcome Back!</h1>
            {msg === "" ? "" : <div style={{ color: "red" }}>{msg}</div>}
            <TextField
              variant="filled"
              color="secondary"
              margin="normal"
              required
              fullWidth
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              id="username"
              label="Username"
              name="username"
              autoFocus
              InputProps={{
                className: classes.input,
              }}
            />
            <FormControl
              className={clsx(classes.margin, classes.textField)}
              variant="filled"
              color="secondary"
            >
              <InputLabel htmlFor="filled-adornment-password">
                Password
              </InputLabel>
              <FilledInput
                id="filled-adornment-password"
                InputProps={{ className: classes.input }}
                type={values.showPassword ? "text" : "password"}
                value={values.password}
                onChange={handleChange("password")}
                endAdornment={
                  <InputAdornment position="end">
                    <IconButton
                      aria-label="toggle password visibility"
                      onClick={handleClickShowPassword}
                      onMouseDown={handleMouseDownPassword}
                      edge="end"
                    >
                      {values.showPassword ? <Visibility /> : <VisibilityOff />}
                    </IconButton>
                  </InputAdornment>
                }
              />
            </FormControl>
            <br />
            <a href="#" className={classes.forgotpwd}>
              Forgot Password?
            </a>
            <Button
              fullWidth
              variant="contained"
              color="primary"
              onClick={signIn}
              className={classes.submit}
            >
              LOGIN
            </Button>
          </form>
        </div>
      </div>
    </ThemeProvider>
  );
}
