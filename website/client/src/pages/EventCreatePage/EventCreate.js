import React from "react";
import EventsMembersHeader from "../../components/EventsMembersHeader/EventsMembersHeader";

class EventCreate extends React.Component{

    render(){
        return (
            <div>
                <br></br><br></br>
                <EventsMembersHeader/>
                <div className='row' style={{paddingLeft:'10%',paddingRight:'10%'}}>
                    <div className='col-sm-4'>
                        <h3 style={{textAlign:'left'}}>Name of the event:</h3>
                        <input style={{width:'100%',padding:'5px'}} type="text" placeholder="Enter the name of the event"></input>
                        <br></br><br></br>
                        <h3 style={{textAlign:'left'}}>Short Description:</h3>
                        <textarea style={{width:'100%',padding:'5px',height:'100px'}} type="text" placeholder="Enter a short description of the event"></textarea>
                        <br></br><br></br>
                        <h3 style={{textAlign:'left'}}>Date of the event:</h3>
                        <input style={{width:'100%',padding:'5px'}} type="date" placeholder="Choose a Date"></input>
                        <br></br><br></br>
                        <h3 style={{textAlign:'left'}}>Venue of the event:</h3>
                        <input style={{width:'100%',padding:'5px'}} type="text" placeholder="Enter the venue of the event"></input>
                        <br></br><br></br>
                    </div>
                    <div className='col-sm-4'>
                        <h3 style={{textAlign:'left'}}>Link to Register:</h3>
                        <input style={{width:'100%',padding:'5px'}} type="text" placeholder="Paste the link to register"></input>
                        <br></br><br></br>
                        <h3 style={{textAlign:'left'}}>Contact Details:</h3>
                        <div style={{width:'100%',display:'flex'}}>
                            <input style={{width:'60%',padding:'5px'}} type="text" placeholder="Person's Name"></input>&nbsp;
                            <input style={{width:'100%',padding:'5px'}} type="text" placeholder="Contact Number"></input>
                        </div><br></br>
                        <div style={{width:'100%',display:'flex'}}>
                            <input style={{width:'60%',padding:'5px'}} type="text" placeholder="Person's Name"></input>&nbsp;
                            <input style={{width:'100%',padding:'5px'}} type="text" placeholder="Contact Number"></input>
                        </div>
                        <br></br>
                        <h3 style={{textAlign:'left'}}>Upload Poster:</h3>
                        <input accept="image/*" type="file" style={{width:'100%',padding:'5px',border:'1px solid black'}}/>
                        <br></br><br></br>
                        <div style={{display:'flex',width:'100%'}}>
                        <h3 style={{textAlign:'left'}}>Add Referral?</h3>
                        <input style={{width:'35px',height:'35px',textAlign:'right'}} type="checkbox"></input>
                        </div>
                        <button style={{width:"100%",height:'38px',borderRadius:'5px'}} type="submit">Create the Event</button>
                        <br></br><br></br>
                    </div>
                    <div className='col-sm-4'>
                        <h3 style={{textAlign:'left'}}>Preview of the poster:</h3>
                        <img width='100%'/>
                        <br></br><br></br>
                    </div>
                </div>
            </div>
        );
    }
}

export default EventCreate;