import React from "react";

class ReferralCard extends React.Component{
    render(){
        console.log(this.props.referral)
        return (
                <div className='referralcard col-sm-4' style={{display:'flex',width:'100%',padding:'15px',fontFamily:'roboto'}}>
                    <div style={{display:'flex',width:'100%',borderRadius:'20px'}}>
                        <div style={{display:'block',float:'left',width:'100%',padding:'5px',textAlign:'center'}}><img style={{borderRadius:'50%'}} width="100%" height="100%" src='https://www.pngitem.com/pimgs/m/264-2640465_passport-size-photo-sample-hd-png-download.png'/></div>
                        <div style={{display:'block',float:'left',width:'100%',padding:'5px',paddingBottom:'0px',textAlign:'center'}}><p></p><p style={{color:'white',fontSize:'17px'}}>{this.props.referral["Name"]}</p><p style={{fontSize:'14px',color:'rgba(255, 255, 255, 0.55)'}}>{this.props.referral["SAP ID"]}</p></div>
                        <div style={{float:'right',width:'100%',padding:'5px'}}><p></p><p style={{float:'right',width:'fit-content',padding:'8px 15px',color:'white',background:'#1C2E4A',borderRadius:'50%',fontWeight:'bold'}}>{this.props.referral["Referral Count"]}</p></div>
                    </div>
                </div>
        );
    }
}

export default ReferralCard;