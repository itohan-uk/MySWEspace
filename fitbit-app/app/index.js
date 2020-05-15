import clock from "clock";
import document from "document";
import { preferences } from "user-settings";
import * as util from "../common/utils";
import { today } from "user-activity";

// Update the clock every minute
clock.granularity = "minutes";

// Get a handle on the <text> element
const myLabel = document.getElementById("myTimeLabel");
const myStepsLabel = document.getElementById("myStepsLabel");


// Update the <text> element every tick with the current time
clock.ontick = (evt) => {
  let mtoday = evt.date;
  let hours = mtoday.getHours();
  if (preferences.clockDisplay === "12h") {
    // 12h format
    hours = hours % 12 || 12;
  } else {
    // 24h format
    hours = util.zeroPad(hours);
  }
  let mins = util.zeroPad(mtoday.getMinutes());
  myLabel.text = `${hours}:${mins}`;
  
  myStepsLabel.text = today.adjusted.steps.toLocaleString("en-US");
  
}
