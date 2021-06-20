import React from "react";
import "./Search.css";
import { MDBCol, MDBIcon } from "mdb-react-ui-kit";
// import SearchIcon from '@material-ui/icons/Search';

const SearchPage = () => {
  return (
    <MDBCol md="6" style={{ margin: "0 auto" }}>
      <div className="input-group md-form form-sm form-1 pl-2">
        <input
          className="form-control my-4 py-1 styling "
          type="text"
          placeholder="Search Committees"
          aria-label="Search"
        />
      </div>
    </MDBCol>
  );
};

export default SearchPage;
