import React from "react";
import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';

const useStyles = makeStyles((theme) => ({
  root: {
    '& > *': {
      margin: theme.spacing(1),
    },
  },
}));


class EventsMembersHeader extends React.Component{
    render(){
        const classes = useStyles;
        return (
            <div>
                <div className={classes.root}>
                    <Button size="large" href="#">Events</Button>&nbsp;&nbsp;&nbsp;&nbsp;
                    <Button size="large" href="#">Members</Button>
                </div>
                <br></br><br></br>
            </div>
        );
    }
}

export default EventsMembersHeader;