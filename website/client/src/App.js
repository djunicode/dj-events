import React from "react";
import Home from "./pages/HomePage/Home";
import CommitteePage from "./pages/CommiteePage/CommitteePage";
import DetailEvent from "./pages/DetailPage/DetailEvent";
import Login from "./pages/Login/Login";
import MembersList from "./pages/Members/MembersList";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Redirect,
} from "react-router-dom";

function PrivateRoute({ children, ...rest }) {
  return (
    <Route
      {...rest}
      render={({ location }) =>
        localStorage.getItem("logged") ? (
          children
        ) : (
          <Redirect
            to={{
              pathname: "/login",
              state: { from: location },
            }}
          />
        )
      }
    />
  );
}

function SignedInRoute({ children, ...rest }) {
  return (
    <Route
      {...rest}
      render={({ location }) =>
        !localStorage.getItem("logged") ? (
          children
        ) : (
          <Redirect
            to={{
              pathname: "/",
              state: { from: location },
            }}
          />
        )
      }
    />
  );
}

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <SignedInRoute path="/login">
            <Login />
          </SignedInRoute>
          <Route path="/" exact component={Home} />
          <PrivateRoute path="/members">
            <MembersList />
          </PrivateRoute>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
