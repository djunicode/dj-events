import React from "react";
import axios from "axios";
import EventsReferralCountHeader from "../../components/EventsReferralCountHeader/EventsReferralCountHeader"
import ReferralCard from "../../components/ReferralCountCard/ReferralCard";

class ReferralCountList extends React.Component{
    state={
        referrals:[]
    }

    componentDidMount(){
        var event_id=window.location.pathname.split('/')[2];
        var token = localStorage.getItem("Token");
        var data=""
        var config = {
            method: "get",
            url:"http://aryan123456.pythonanywhere.com/api/referral_table/"+event_id+"/",
            headers: {
                Authorization: "Token " + token,
            },
            data: data,
        };
        axios(config)
            .then((response)=>this.setState({referrals:response.data}))
            .catch((err) => console.error(err));
    }
    render() {
        console.log(window.location.pathname.split('/')[2])
        return (
            <div>
                <br></br><br></br>
                <EventsReferralCountHeader/>
                <h4>Referral Count</h4>
                <div className='container'>
                    <div className='row'>
                    {this.state.referrals.map((referral,index)=><ReferralCard key={index} referral = {referral}/>)}
                    </div>
                </div>

            </div>
        );
    }
}

export default ReferralCountList;