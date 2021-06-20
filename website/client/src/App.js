import React from "react";
import Home from "./pages/HomePage/Home";
import Login from "./pages/Login/Login";
import MembersList from "./pages/Members/MembersList";
import EventsList from "./pages/EventsPage/EventsList";
import EventCreate from "./pages/EventCreatePage/EventCreate";
import ReferralCountList from "./pages/ReferralCountPage/ReferralCountList";
import CommitteePage from "./pages/CommiteePage/CommitteePage";
import DetailEvent from "./pages/DetailPage/DetailEvent";

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
          <Route path="/committee/:id" exact component={CommitteePage} />
          <Route path="/event/:id" exact component={DetailEvent} />
          <PrivateRoute path="/members">
            <MembersList />
          </PrivateRoute>
          <PrivateRoute path="/events">
            <EventsList />
          </PrivateRoute>
          <PrivateRoute path="/eventcreate">
            <EventCreate />
          </PrivateRoute>
          <PrivateRoute path="/eventreferralcount/:id">
            <ReferralCountList />
          </PrivateRoute>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
