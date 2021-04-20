import React, { useEffect, useState } from "react";
import axios from "axios";
import DisplayMembers1 from "../../components/Members/DisplayMembers1";

const AddCore = () => {
  const [students, setStudents] = useState([]);
  var x = localStorage.getItem("id");
  var data = "";
  var token = localStorage.getItem("Token");
  var config = {
    method: "get",
    url: "http://aryan123456.pythonanywhere.com/api/students/",
    headers: {
      Authorization: "Token " + token,
    },
    data: data,
  };
  useEffect(() => {
    axios(config)
      .then((response) => console.log(response.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div>
      <h1>Hello</h1>
    </div>
  );
};

export default AddCore;
