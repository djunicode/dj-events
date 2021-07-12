import React from "react";
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import CreateIcon from '@material-ui/icons/Create';

const useStyles = makeStyles({
  root: {
    maxWidth: 345,
  },
  media: {
    height: 140,
  },
});

class EventCard extends React.Component{
    render() {
      const classes = useStyles;
      return (
        <div className='col-sm-3' style={{}}>
          <a href={"/eventedit/"+this.props.event.id} style={{ textDecoration: "none" }}>
            <Card className={classes.root} style={{display:'block',height:'240px',overflow:'hidden',background:'#4E586E',borderRadius:'15px'}}>
              <CardActionArea>
                <CardMedia
                  component="img"
                  alt="{this.props.event.eventName}"
                  height="170"
                  image="https://wallpapercave.com/wp/wp2587127.jpg"
                  title="{this.props.event.eventName}"
                />
                <CardContent>
                  <div style={{width:'100%',display:'flex'}}>
                    <div style={{paddingLeft:'10px',width:'100%'}}>
                      <Typography gutterBottom variant="h5" component="h5" style={{color:'white',fontSize:'20px'}}>
                      {this.props.event.eventName}
                      </Typography>
                    </div>
                    <div align='right' style={{textAlign:'right'}}>
                      <Typography style={{color:'white',fontSize:'10px'}}>
                        <CreateIcon/>
                      </Typography>
                    </div>
                  </div>
                </CardContent>
              </CardActionArea>
            </Card>
            </a>
            <br></br>
        </div>
      );
    }
}

export default EventCard;