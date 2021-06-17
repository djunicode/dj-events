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
            <div style={{background:'#1C2E4A'}}>
                <br></br><br></br>
                <EventsReferralCountHeader/>
                <h4 style={{color:'white'}}>Referral Counts</h4><br></br>
                <div className='container' style={{background:'#4E586E',borderRadius:'28.3946px',boxShadow:'0px 5.67892px 5.67892px rgba(0, 0, 0, 0.25)'}}>
                    <br></br>
                    <div className='row'>
                    {this.state.referrals.map((referral,index)=><ReferralCard key={index} referral = {referral}/>)}
                    </div>
                    <br></br>
                </div>
                <br></br><br></br>
            </div>
        );
    }
}

export default ReferralCountList;