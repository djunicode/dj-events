import React from "react";

class ReferralCard extends React.Component{
    render(){
        console.log(this.props.referral)
        return (
            <div className='col-sm-4' style={{display:'flex',width:'100%',padding:'15px'}}>
                <div style={{display:'flex',width:'100%',borderRadius:'20px'}}>
                <div style={{display:'block',float:'left',width:'100%',padding:'5px',textAlign:'center'}}><img width="100%" height="100%" src='https://image.freepik.com/free-icon/important-person_318-10744.jpg'/></div>
                <div style={{display:'block',float:'left',width:'100%',padding:'5px',textAlign:'center'}}><p></p>{this.props.referral["Name"]}<br></br><p style={{fontSize:'12px'}}>{this.props.referral["SAP ID"]}</p></div>
                <div style={{float:'right',width:'100%',padding:'5px'}}><p></p><p style={{border:'1px solid black'}}>{this.props.referral["Referral Count"]}</p></div>
                </div>
            </div>
        );
    }
}

export default ReferralCard;