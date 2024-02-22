import scratchattach as s3
import os

Secret=os.getenv("Secret")
Session=s3.login("Boubou78000", Secret)
Conn=Session.connect_cloud("26861174")
