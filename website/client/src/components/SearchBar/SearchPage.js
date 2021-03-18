import React from "react";
import './Search.css'
import { MDBCol, MDBIcon } from "mdb-react-ui-kit";
// import SearchIcon from '@material-ui/icons/Search';

const SearchPage = () => {
  return (
    <MDBCol md="6" style={{margin : '0 auto'}}>
      <div className="input-group md-form form-sm form-1 pl-2">
        {/* <div className="input-group-prepend">
          <span className="input-group-text purple lighten-3" id="basic-text1">
            <MDBIcon className="text-white" icon="search" />
          </span>
        </div> */}
          
        <input className="form-control my-4 py-1 styling " type="text" placeholder="Search Committees" aria-label="Search" />
        
      </div>
    </MDBCol>

  );
}

export default SearchPage;