TO be added at the desired packages

///////////////////////////////////////////////////////////////////////////////////////////

P R O F I L E  P I C T U R E +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

///////////////////////////////////////////////////////////////////////////////////////////

HOW TO USE: 
  
At your UI(Main) thread ;

Kotlin;
pfp = ProfilePicture(ImageView iv, int owner_id, int target_id, int session_id)

Java;
ProfilePicture pfp = new ProfilePicture(ImageView iv, int owner_id, int target_id, int session_id);


owner_id : phone users own id
target_id : requested pfps owners id
session_id : placeholder for now
iv: UI element for image display


To resynch from the image server;

pfp.synch()


/////////////////////////////////////////////////////////////////////////////////////////////

WHAT IT DOES?

Asynchronously loads up initialized ImageViews targeting the profile pictures,
  
until the load displays the default picture
  
UI thread might freeze a little after the asynchronous task returns the result to ImageView

//////////////////////////////////////////////////////////////////////////////////////////////

USE PIPELINE:

Each ProfilePictures owner cannot be changed, in the case of relog, getting a new user list; 
one must also generate new UI Objects.

//////////////////////////////////////////////////////////////////////////////////////////////

TO DO:

Send the tokenized session id to otherwise stop unwanted requests taxing the image server. 



///////////////////////////////////////////////////////////////////////////////////////////

SET PROFILE PICTURE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

///////////////////////////////////////////////////////////////////////////////////////////

HOW TO USE: 
  
At your UI(Main) thread ;

PFPSetActivity setActivity = new PFPSetActivity( int user_id, int session_id, Bitmap bmp, AppCOmpatActivity watcher);
setActivity.execute();

owner_id : phone users own id
session_id : placeholder for now
watcher: listening UI object
