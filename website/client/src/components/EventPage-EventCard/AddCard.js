import React from "react";
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import CreateIcon from '@material-ui/icons/Create';
import AddCircleIcon from '@material-ui/icons/AddCircle';

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
            <Card className={classes.root} style={{display:'block',height:'240px',overflow:'hidden',background:'#4E586E',borderRadius:'15px'}}>
              <CardActionArea>
                <CardContent>
                    <Typography gutterBottom variant="h5" component="h5">
                        <AddCircleIcon style={{fontSize:'60px',borderRadius:'50%',background:'white'}}/>
                    </Typography>
                    <Typography gutterBottom variant="h5" component="p" style={{color:'white'}}>
                    CREATE<br></br>AN<br></br>EVENT
                    </Typography>
                </CardContent>
              </CardActionArea>
            </Card>
            <br></br>
        </div>
      );
    }
}

export default EventCard;