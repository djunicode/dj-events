import React, { useEffect, useState } from "react";
import axios from "axios";
import DisplayMembers1 from "../../components/Members/DisplayMembers1";

const AddCo = () => {
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
      .then((response) => setStudents(response.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div>
      {students.map((x) => (
        <div>
          <p>
            {x.first_name} {x.last_name}
          </p>
          <p>{x.sap}</p>
        </div>
      ))}
    </div>
  );
};

export default AddCo;
