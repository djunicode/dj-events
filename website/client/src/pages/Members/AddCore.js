import React, { useEffect, useState } from "react";
import axios from "axios";

const AddCore = () => {
  let a = [];
  const [students, setStudents] = useState([]);
  var id = localStorage.getItem("id");
  var data = "";
  var token = localStorage.getItem("Token");
  var config = {
    method: "get",
    url: `http://aryan123456.pythonanywhere.com/api/noncorecom_list/${id}`,
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

  console.log(students);
  return (
    <div>
      {students.map((x, index) => (
        <div>
          <p>
            {x.first_name} {x.last_name}
          </p>
          <p>{x.username}</p>
        </div>
      ))}
    </div>
  );
};

export default AddCore;
