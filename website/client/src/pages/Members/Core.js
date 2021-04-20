import React, { useEffect, useState } from "react";
import axios from "axios";
import DisplayMembers2 from "../../components/Members/DisplayMembers2";

const Core = () => {
  const [core, setCore] = useState([]);
  var x = localStorage.getItem("id");
  var data = "";
  var token = localStorage.getItem("Token");
  var config = {
    method: "get",
    url:
      "http://aryan123456.pythonanywhere.com/api/get_core_committee_members/" +
      x,
    headers: {
      Authorization: "Token " + token,
    },
    data: data,
  };
  useEffect(() => {
    axios(config)
      .then((response) => setCore(response.data))
      .catch((err) => console.error(err));
  }, [core]);

  return (
    <div>
      {core.map((x) => (
        <DisplayMembers2
          key={x.id}
          id={x.id}
          name={x.student}
          positionAssigned={x.positionAssigned}
        />
      ))}
    </div>
  );
};

export default Core;
