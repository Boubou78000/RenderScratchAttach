import scratchattach as s3
import os

Secret=os.getenv("Secret")
Session=s3.login("Boubou78000", Secret)
Conn=Session.connect_cloud("26861174") #Sorry Griff
Conn.set_var("Cloud 1", "0")
Conn.set_var("Cloud 2", "0")
