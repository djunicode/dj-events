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
        <div className='col-sm-3' >
            <Card className={classes.root} style={{display:'block',height:'240px',overflow:'hidden'}}>
              <CardActionArea>
                <CardMedia
                  component="img"
                  alt="{this.props.event.eventName}"
                  height="140"
                  image="https://wallpapercave.com/wp/wp2587127.jpg"
                  title="Contemplative Reptile"
                />
                <CardContent>
                  <div className="row" style={{width:'100%'}}>
                    <div style={{paddingLeft:'10px'}}>
                      <Typography gutterBottom variant="h5" component="h2">
                      {this.props.event.eventName}
                      </Typography>
                    </div>
                    <div align='right' style={{textAlign:'right'}}>
                      <Typography variant="body2" color="textSecondary" component="p">
                        <CreateIcon/>
                      </Typography>
                    </div>
                  </div>
                </CardContent>
              </CardActionArea>
            </Card>
            <br></br>
        </div>
      );
    }
}

export default EventCard;